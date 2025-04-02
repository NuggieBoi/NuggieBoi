#include <Servo.h>
#include "SR04.h"
#include "pitches.h"
#define TRIG_PIN 12
#define ECHO_PIN 11

Servo myservo;
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
int duration = 100;
long a;
int pos = 0;

void check_dis(){
  a=sr04.Distance();
  Serial.print(a);
  Serial.println("cm");
  if(a<=20){
    tone(10, NOTE_C6, duration);
    delay(100);
    tone(10, NOTE_E5, duration);
  }
}

void setup() {
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);
    check_dis();
    delay(10);
  }

  for (pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    check_dis();
    delay(10);
  }
}
