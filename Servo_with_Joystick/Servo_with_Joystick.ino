#include <Servo.h>

Servo servo1;
Servo servo2;

const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output

void setup() {
  servo1.attach(9);
  servo2.attach(10);
  Serial.begin(9600);
}

void loop() {
  int X_pos = analogRead(X_pin);
  int Y_pos = analogRead(Y_pin);

  if (X_pos >= 800){
    servo1.write(180);
    Serial.println("Turning Down");
  }else if (X_pos <= 300){
    servo1.write(0);
    Serial.println("Turning Up");
  }else if (Y_pos >= 800){
    servo2.write(180);
    Serial.println("Turning Left");
  }else if (Y_pos <= 300){
    servo2.write(0);
    Serial.println("Turning Right");
  }else{
    servo1.write(90);
    servo2.write(90);
    Serial.println("Idle");
  }

  delay(100);
}
