int  sensorAnalogPin = A0;
int  sensorDigitalPin = 3; 
int  analogValue = 0;      
int  LedPin = 4;
int digitalValue;
                              
void setup()
{
  Serial.begin(9600);           
  pinMode(sensorDigitalPin,INPUT); 
  pinMode(LedPin,OUTPUT);           
}

void loop(){
  analogValue = analogRead(sensorAnalogPin); 
  digitalValue=digitalRead(sensorDigitalPin); 
  Serial.println(analogValue); 
  
  if(digitalValue==LOW)      
  {
    digitalWrite(LedPin,HIGH);
    delay(1000);
  }
  else
  {
    digitalWrite(LedPin,LOW);
  }
  
  delay(50);                 
}