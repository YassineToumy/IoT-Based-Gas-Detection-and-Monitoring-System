const int gasPin = A0; // Analog input pin connected to the sensor's AOUT pin
int gasLevel = 0;      // Variable to store the gas level reading

const int ledPin = 12;    // LED connected to pin 13
const int buzzerPin = 11; // Buzzer connected to pin 12

void setup() {
  Serial.begin(9600);        // Start the serial communication
  pinMode(gasPin, INPUT);    // Set the gas sensor pin as an input
  pinMode(ledPin, OUTPUT);   // Set the LED pin as an output
  pinMode(buzzerPin, OUTPUT);// Set the buzzer pin as an output
}

void loop() {
  // Read the analog value from the gas sensor
  gasLevel = analogRead(gasPin);
  Serial.print("Gas Level: ");
  Serial.println(gasLevel); // Print the gas level to the Serial Monitor

  // Simple threshold detection
  if (gasLevel > 500) { // Adjust this threshold as needed
    Serial.println("Gas detected! High concentration.");
    
    // Turn on the LED and buzzer
    digitalWrite(ledPin, HIGH);
    digitalWrite(buzzerPin, HIGH);

    delay(550); // Wait for 350ms for a warning pulse

    // Turn off the LED and buzzer
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
  } else {
    Serial.println("Gas level normal.");

    // Ensure both LED and buzzer are off
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
  }

  delay(3000); // Wait for 1 second before reading again
  Serial.println(gasLevel);
}
