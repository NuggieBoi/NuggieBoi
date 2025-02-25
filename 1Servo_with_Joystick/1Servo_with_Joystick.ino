#include <Servo.h>

Servo servo1;

const int X_pin = 0; // analog pin connected to X output

void setup() {
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {
  int X_pos = analogRead(X_pin);

  if (X_pos >= 800){
    servo1.write(180);
    Serial.println("Turning Down");
  }else if (X_pos <= 300){
    servo1.write(0);
    Serial.println("Turning Up");
  }else{
    servo1.write(90);
    Serial.println("Idle");
  }

  delay(100);
}
