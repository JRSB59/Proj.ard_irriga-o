#define rele 3          // Pino do relé conectado à bomba de água
#define sensor 2        // Pino do sensor de umidade do solo

bool soloSeco = false;            // Variável para monitorar o estado do solo
unsigned long tempoAtual = 0;     // Armazena o tempo atual do loop
unsigned long tempoAnterior = 0;  // Armazena o tempo do último acionamento
const unsigned long intervalo = 10000; // Intervalo de 5 minutos (em milissegundos)
const unsigned long duracao = 2000;     // Duração da irrigação de 3 segundos

void setup() 
{
  pinMode(rele, OUTPUT);      // Define o pino do relé como saída
  pinMode(sensor, INPUT);      // Define o pino do sensor como entrada
  digitalWrite(rele, HIGH);    // Inicializa o relé desligado
}

void loop() {
  tempoAtual = millis();                 // Obtém o tempo atual
  soloSeco = digitalRead(sensor);        // Lê o estado do sensor de umidade

  // Verifica se já passou o intervalo de 5 minutos e se o solo está seco
  if (soloSeco && (tempoAtual - tempoAnterior >= intervalo)) {
    tempoAnterior = tempoAtual;          // Atualiza o tempo do último acionamento
    digitalWrite(rele, LOW);             // Liga a bomba
    delay(duracao);                      // Aguarda 3 segundos
    digitalWrite(rele, HIGH);            // Desliga a bomba
  }

  delay(500); // Pequeno delay para reduzir leituras rápidas desnecessárias
}
