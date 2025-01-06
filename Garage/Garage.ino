#include <Stepper.h>

const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution
const int rolePerMinute = 15;         // Adjustable range of 28BYJ-48 stepper is 0~17 rpm
int button1 = 7;
int button2 = 6;

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  myStepper.setSpeed(rolePerMinute);
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  if (LOW==digitalRead(button1)){
    Serial.println("Opening the Garage!");
    myStepper.step(stepsPerRevolution);
  }
  if (LOW==digitalRead(button2)){
    Serial.println("Garage door is closing!");
    myStepper.step(-stepsPerRevolution);
  }
  delay(50);
}
