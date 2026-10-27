#include <Wire.h>

const byte I2C_ADDRESS = 0x08;
const byte LED_PIN = LED_BUILTIN;

void receberComando(int quantidadeBytes) {
  while (Wire.available() > 0) {
    byte comando = Wire.read();

    if (comando == 1) {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("Comando recebido: LED ligado");
    } else if (comando == 0) {
      digitalWrite(LED_PIN, LOW);
      Serial.println("Comando recebido: LED desligado");
    } else {
      Serial.print("Comando desconhecido: ");
      Serial.println(comando);
    }
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(9600);
  Wire.begin(I2C_ADDRESS);
  Wire.onReceive(receberComando);

  Serial.println("Checkpoint 1: Arduino pronto.");
  Serial.println("Endereco I2C: 0x08");
}

void loop() {
  // Os comandos recebidos via I2C são tratados em receberComando().
}
