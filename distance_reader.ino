const int TRIG_PIN = 13;
const int ECHO_PIN = 12;
const int BUZZER = 11; // use an active buzzer for this project
const int greenLED = 10;
const int redLED = 9;

unsigned long duration;
double distanceCm;

const double MAX_RANGE = 30.0; // in centimetres
const double ALERT_THRESHOLD = MAX_RANGE * 0.33; // ~10cm

void setup() {
  pinMode(TRIG_PIN, OUTPUT); 
  pinMode(ECHO_PIN, INPUT); 
  pinMode(BUZZER, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

  digitalWrite(BUZZER, LOW); 
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);

  Serial.begin(9600); 
}

void loop() {
  // Trigger ultrasonic pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // Read echo pulse duration
  duration = pulseIn(ECHO_PIN, HIGH);
 distanceCm = (duration * 0.0343) / 2.0;

// Ignore high readings above max sensor range (~400 cm)
if (distanceCm > 400 || distanceCm <= 0) {
  return; // skip this loop cycle
}

  // Visual/audible indicators
  digitalWrite(greenLED, distanceCm < MAX_RANGE ? HIGH : LOW);

  if (distanceCm < ALERT_THRESHOLD) {
    digitalWrite(redLED, HIGH);
    digitalWrite(BUZZER, HIGH);
  } else {
    digitalWrite(redLED, LOW);
    digitalWrite(BUZZER, LOW);
  }

  // Structured serial output (Python-friendly)
  Serial.print("{\"distance_cm\":");
  Serial.print(distanceCm);
  Serial.println("}");
  //Serial.println(distanceCm);

  delay(100); // limit to ~10 readings/sec
}