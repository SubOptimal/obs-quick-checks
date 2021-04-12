// A simple test sketch to verify the function of the ultrasonic sensors.

const int TRIG_PIN = 2;
const int ECHO_PIN = 5;

long duration;
float distance;

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  noInterrupts();

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(3);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(20);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  
  // distance calculation: (duration in µs) / 2 * (speed of sound in cm/µs)
  distance= (duration/2) * 0.03436;

  interrupts();

  if (distance < 800 and distance >= 21) {
    Serial.printf("distance: %.2f cm\n", distance);
  } else {
    Serial.printf("*");
  }

  delay(500);
}
