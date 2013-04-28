#include <Esplora.h>  
#define LED_PIN 13

void setup()
{
	pinMode(LED_PIN, OUTPUT);
	Serial.begin(9600);
}

void loop()
{
	Serial.println(Esplora.readLightSensor(), DEC);
	delay(500);
	digitalWrite(LED_PIN, HIGH);
	delay(500);
	digitalWrite(LED_PIN, LOW);
}
