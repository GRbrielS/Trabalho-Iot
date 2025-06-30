const int sensorHall = 2;      // Pino do sensor Hall
const int ledVermelho = 13;    // LED vermelho
const int buzzer = 12;         // Buzzer ativo

int estadoAnterior = HIGH;
bool portaFechada = true;

unsigned long ultimoTempoPiscar = 0;
const unsigned long intervaloPiscar = 1000;
bool estadoLed = false;

void setup() {
  pinMode(sensorHall, INPUT_PULLUP);
  pinMode(ledVermelho, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int estadoAtual = digitalRead(sensorHall);

  if (estadoAtual != estadoAnterior) {
    if (estadoAtual == LOW) {
      // Porta fechada
      digitalWrite(ledVermelho, LOW);    // LED apagado
      digitalWrite(buzzer, LOW);        // Desliga buzzer
      portaFechada = false;
      Serial.println("Porta fechada");
    } else {
      // Porta aberta
      digitalWrite(buzzer, HIGH);         // Liga buzzer
      portaFechada = true;
      Serial.println("ALERTA: Porta aberta");
    }
    estadoAnterior = estadoAtual;
  }

  // Piscar o LED se a porta estiver aberta
  if (portaFechada) {
    if (millis() - ultimoTempoPiscar >= intervaloPiscar) {
      estadoLed = !estadoLed;
      digitalWrite(ledVermelho, estadoLed);
      ultimoTempoPiscar = millis();
    }
  } else {
    digitalWrite(ledVermelho, LOW); // Garante LED desligado se porta fechar
  }
}

  delay(100); // Pequeno atraso para estabilidade
}
