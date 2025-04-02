#include <Keypad.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const byte ROWS = 4;
const byte COLS = 4;
int cursor = 0;
String password = "D";
String code = "D1111";
int pass_len = 0;

char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2}; 

Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS))
  {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.display();
  delay(1000);
  display.clearDisplay();
  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(0, 0); 
  display.print("Please Enter Code");
}

void loop(){
  char customKey = customKeypad.getKey();
  if (customKey){
    if (password == code){
      display.clearDisplay();
      display.setCursor(0, 0);
      display.print("Correct!");
      display.display();
    }else{
      if (customKey == 'D'){
        display.clearDisplay();
        display.setCursor(0, 0); 
        display.print("Please Enter Code");
        pass_len = 0;
        cursor = 0;
        password = "";
        display.display();
      }
      display.setCursor(cursor, 10);
      if (pass_len < 4){
        //display.clearDisplay();
        display.print(customKey);
        password = password + customKey;
        display.display();
        Serial.println(password);
        cursor += 10;
        pass_len += 1;
    }else{
      Serial.println("Password To Long");
  }
  delay(100);
  }
  }
}