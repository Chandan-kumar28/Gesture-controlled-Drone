#include <Servo.h>

Servo esc1, esc2, esc3, esc4;

const int esc1Pin = 5;
const int esc2Pin = 6;
const int esc3Pin = 9;
const int esc4Pin = 10;

int throttle = 1000;  // Default: Stopped

void setup() {
    Serial.begin(9600);

    esc1.attach(esc1Pin);
    esc2.attach(esc2Pin);
    esc3.attach(esc3Pin);
    esc4.attach(esc4Pin);

    armESCs();
}

void loop() {
    if (Serial.available()) {
        int receivedThrottle = Serial.parseInt(); // Read incoming throttle value

        if (receivedThrottle >= 1000 && receivedThrottle <= 2000) {
            throttle = receivedThrottle;
        }
    }

    esc1.writeMicroseconds(throttle);
    esc2.writeMicroseconds(throttle);
    esc3.writeMicroseconds(throttle);
    esc4.writeMicroseconds(throttle);

    Serial.print("Throttle Set To: ");
    Serial.println(throttle);

    delay(20);
}

void armESCs() {
    Serial.println("Arming ESCs...");
    
    esc1.writeMicroseconds(1000);
    esc2.writeMicroseconds(1000);
    esc3.writeMicroseconds(1000);
    esc4.writeMicroseconds(1000);
    
    delay(5000);
    Serial.println("ESCs Armed!");
}
