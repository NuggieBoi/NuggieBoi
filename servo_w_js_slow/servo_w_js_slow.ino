#include <Servo.h>

Servo servo1;

const int X_pin = 0; // analog pin connected to X output
int servo_pos = 0;

void setup() {
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {
  int X_pos = analogRead(X_pin);
  if (X_pos >= 800){
    servo_pos++;
  }else if (X_pos <= 300){
    servo_pos--;
  }

  servo1.write(servo_pos);
  delay(50);
}
