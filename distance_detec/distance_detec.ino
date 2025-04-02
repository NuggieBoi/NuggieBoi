#include "LedControl.h"
#include "SR04.h"

#define TRIG_PIN 9
#define ECHO_PIN 8

SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
LedControl lc=LedControl(12,10,11,1);

long a;
unsigned long delaytime1=500;
unsigned long delaytime2=50;
byte row = B11111111;

void setup() {
  Serial.begin(9600);
  lc.shutdown(0,false);
  lc.setIntensity(0,4);
  lc.clearDisplay(0);
}

void loop(){
  a=sr04.Distance();
  Serial.print(a);
  Serial.println("cm");
  if (a<=32 && a>28){
    lc.setColumn(0,0,row);
  }
  if (a<=28 && a>24){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
  }
  if (a<=24 && a>20){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
  }
  if (a<=20 && a>16){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
    lc.setColumn(0,3,row);
  }
  if (a<=16 && a>12){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
    lc.setColumn(0,3,row);
    lc.setColumn(0,4,row);
  }
  if (a<=12 && a>8){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
    lc.setColumn(0,3,row);
    lc.setColumn(0,4,row);
    lc.setColumn(0,5,row);
  }
  if (a<=8 && a>4){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
    lc.setColumn(0,3,row);
    lc.setColumn(0,4,row);
    lc.setColumn(0,5,row);
    lc.setColumn(0,6,row);
  }
  if (a<=4){
    lc.setColumn(0,0,row);
    lc.setColumn(0,1,row);
    lc.setColumn(0,2,row);
    lc.setColumn(0,3,row);
    lc.setColumn(0,4,row);
    lc.setColumn(0,5,row);
    lc.setColumn(0,6,row);
    lc.setColumn(0,7,row);
  }
  lc.clearDisplay(0);
  delay(10);
}
