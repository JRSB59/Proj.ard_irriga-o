import serial
import time
from datetime import datetime

# Configure a porta serial (substitua 'COM3' pela porta do seu Arduino, ou '/dev/ttyUSB0' no Linux)
arduino = serial.Serial('COM3', 9600, timeout=1)

# Arquivo de log
log_file = "irrigacao_log.txt"

print("Monitorando irrigação...")

while True:
    # Ler dados da serial
    if arduino.in_waiting > 0:
        line = arduino.readline().decode().strip()
        
        if line == "Irrigacao iniciada":
            # Obter data e hora atuais
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"Irrigação iniciada em: {timestamp}\n"
            
            # Escrever no arquivo de log
            with open(log_file, "a") as file:
                file.write(log_entry)
            
            print(log_entry)
    
    # Pequeno atraso para evitar uso excessivo de CPU
    time.sleep(0.5)
