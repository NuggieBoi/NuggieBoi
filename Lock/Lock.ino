//www.elegoo.com
//2016.12.08

int ledPin = 5;
int buttonApin = 9;
int buttonBpin = 8;

void setup() 
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(2, INPUT);
  digitalWrite(2, HIGH);
  pinMode(buttonApin, INPUT_PULLUP);  
  pinMode(buttonBpin, INPUT_PULLUP);  
}

void loop() 
{
  int tilt_val = digitalRead(2);
  Serial.println(tilt_val);
  if (digitalRead(buttonApin)==LOW){
    if(HIGH == tilt_val){
      digitalWrite(ledPin, HIGH);
      Serial.println("Unlocked!");
  }
  }
  if (digitalRead(buttonBpin) == LOW)
  {
    digitalWrite(ledPin, LOW);
    Serial.println("Locked!");
  }
  delay(200);
}
