# Gesture-Controlled Drone

This project enables controlling a drone using hand gestures. It utilizes **OpenCV** for gesture detection and **Arduino** to communicate with Electronic Speed Controllers (ESCs) for motor control. The system translates hand gestures into commands, which are sent to the Arduino to regulate the drone's movements.

## Requirements
Ensure you have the following installed before proceeding:

### Python Libraries:
- **PyFirmata**: Enables communication between Python and Arduino.
- **OpenCV**: Used for accessing the camera (internal/external) for gesture detection.
- **Mediapipe**: Recognizes and marks hand landmarks for gesture recognition.
- **PySerial**: Enables serial communication with the Arduino.

### Arduino Library:
- **Servo.h**: Used to control ESCs via Arduino's PWM pins.

### Installation
Run the following commands to install the required Python libraries:
```sh
pip install pyfirmata
pip install opencv-python
pip install mediapipe
pip install pyserial
```
For the Arduino library:
1. Open the Arduino IDE.
2. Navigate to **Sketch** > **Include Library** > **Manage Libraries**.
3. Search for **Servo** and install it.
![image](https://github.com/user-attachments/assets/cc7a076c-84c5-4f44-b931-d97642484676)
## Wiring Connections
Connect the ESCs to the Arduino as follows:

| ESC Pin  | Arduino Pin |
|----------|------------|
| GND      | GND        |
| Signal   | ~5 / ~6 / ~9 / ~10 |

## Getting Started
1. Ensure Python is installed and added to the system PATH.
2. Connect your Arduino to the computer.
3. Upload the required Arduino sketch (provided in the repository) using the Arduino IDE.
4. Run the Python script for gesture detection and drone control.

## Troubleshooting
- **Python Not Recognized?** Ensure Python is added to the system PATH.
![image](https://github.com/user-attachments/assets/5a1a4058-9acc-45d1-ac7d-c6c5e7f4fed2)
- **Mediapipe Installation Error?** Try using Python **3.12 or lower** if you encounter issues.
- **Arduino Connection Issues?** Verify that the correct COM port is specified in the Python script.



