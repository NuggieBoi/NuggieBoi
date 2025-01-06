#include <SR04.h>
#define TRIG_PIN 12
#define ECHO_PIN 11
#include <Servo.h>

Servo myservo;
SR04 sr04=SR04(ECHO_PIN, TRIG_PIN);
int pos=Serial.read();
long distance;

void setup(){
  Serial.begin(9600);
  myservo.attach(9);
}

void loop(){
  //use myservo.write(number0-180)
  distance=sr04.Distance();
  Serial.print(distance);
  Serial.println("cm");
  if (distance<5){
    Serial.println("Come on in!");
    myservo.write(90);
    delay(4000);
    Serial.println("Closing up");
    myservo.write(0);
  }
  delay(100);
}