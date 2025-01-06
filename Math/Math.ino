#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

int response = 0;
int add_button = 6;
int sub_button = 5;
int submit = 4;
int wait = 200;

int num1;
int num2;
int answer;
String question;

void setup() {
  randomSeed(analogRead(0));
  num1 = random(0,10);
  num2 = random(0,10);
  answer = num1*num2;
  question = String(num1) + "x" + String(num2) + "=?";
  lcd.begin(16, 2);
  lcd.print(question);
  pinMode(add_button, INPUT_PULLUP);
  pinMode(sub_button, INPUT_PULLUP);
  pinMode(submit, INPUT_PULLUP);
  lcd.setCursor(0,1);
}

void update(){
  lcd.setCursor(0,0);
  lcd.clear();
  lcd.print(question);
  lcd.setCursor(0,1);
  lcd.print(response);
}

void loop() {

  if (LOW == digitalRead(add_button)){
    response+=1;
    lcd.print(response);
    update();
    delay(wait);
  }
  if (LOW == digitalRead(sub_button)){
    response-=1;
    lcd.print(response);
    update();
    delay(wait);
  }
  if(digitalRead(submit) == LOW){
    if (response == answer){
      lcd.clear();
      lcd.print("Nice!");
      randomSeed(analogRead(0));
      num1 = random(0,10);
      num2 = random(0,10);
      answer = num1*num2;
      question = String(num1) + "x" + String(num2) + "=?";
      delay(2000);
      response = 0;
      update();

    }else{
      lcd.clear();
      lcd.print("Try Again!");
      delay(2000);
      update();
    }
  }

}


