//www.elegoo.com
//2016.12.12

/************************
Exercise the motor using
the L293D chip
************************/

#define ENABLE 5
#define DIRA 3
#define DIRB 4

const int button1Pin = 8;
const int button2Pin = 9;
 
void setup() {
  //---set pin direction
  pinMode(ENABLE,OUTPUT);
  pinMode(DIRA,OUTPUT);
  pinMode(DIRB,OUTPUT);
  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
    int button1State = digitalRead(button1Pin);
    int button2State = digitalRead(button2Pin);

    if (button1State == LOW) {
      digitalWrite(ENABLE, LOW);
      Serial.println("Turning Fan Off!");
    }

    if (button2State == LOW) {
      digitalWrite(DIRB, HIGH);
      digitalWrite(DIRA, LOW);
      digitalWrite(ENABLE, HIGH);
      Serial.println("Cooling You Off!");
    }

    delay(50); 
}