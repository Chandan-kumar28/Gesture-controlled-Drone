import cv2
import serial
import time
import numpy as np
from mediapipe import solutions

# Connect to Arduino (Update COM port for Windows, /dev/ttyUSBx for Linux)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)
time.sleep(2)  # Allow time for connection

# Initialize MediaPipe Hands
mp_hands = solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_hand_open_ratio(landmarks):
    """ Improved hand openness detection based on finger distances. """
    thumb_tip = np.array([landmarks[4][0], landmarks[4][1]])
    index_tip = np.array([landmarks[8][0], landmarks[8][1]])
    middle_tip = np.array([landmarks[12][0], landmarks[12][1]])
    ring_tip = np.array([landmarks[16][0], landmarks[16][1]])
    pinky_tip = np.array([landmarks[20][0], landmarks[20][1]])
    palm_base = np.array([landmarks[0][0], landmarks[0][1]])

    # Compute distances between finger tips and palm base
    distances = [
        np.linalg.norm(thumb_tip - palm_base),
        np.linalg.norm(index_tip - palm_base),
        np.linalg.norm(middle_tip - palm_base),
        np.linalg.norm(ring_tip - palm_base),
        np.linalg.norm(pinky_tip - palm_base),
    ]

    max_dist = max(distances)
    openness_ratio = max_dist / 200  # Normalize (adjust this based on your camera)
    
    # Improved fist detection: if fingers are very close together, treat as fist
    avg_finger_distance = np.mean(distances[1:])  # Ignore thumb
    if avg_finger_distance < 30:  # If fingers are close, treat as fist
        openness_ratio = 0
    
    return min(max(openness_ratio, 0), 1)  # Keep between 0 and 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(frame_rgb)

    throttle_value = 1000  # Default: stopped (fist)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, solutions.hands.HAND_CONNECTIONS)

            landmarks = [(lm.x * frame.shape[1], lm.y * frame.shape[0]) for lm in hand_landmarks.landmark]
            openness = get_hand_open_ratio(landmarks)

            if openness < 0.1:  # Fist detected (more strict)
                throttle_value = 1000  # Stop motors
            else:
                throttle_value = int(1000 + (openness * 1000))  # Scale to 1000-2000 µs

            print(f"Throttle: {throttle_value}")
            arduino.write(f"{throttle_value}\n".encode())

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
