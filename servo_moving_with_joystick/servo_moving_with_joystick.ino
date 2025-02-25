#include <Servo.h>

Servo servo1;

const int X_pin = 0; // analog pin connected to X output

void setup() {
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {
  int X_pos = analogRead(X_pin);
  // the 670 in the map function might have to be 1023
  // depending on the type of joystick your using
  long servo_pos = map(X_pos, 0, 670, 0, 180);
  servo_pos = constrain(servo_pos, 0, 180);
  Serial.println(servo_pos);
  servo1.write(servo_pos);

  delay(100);
}
