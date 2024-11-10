import serial
import time
from datetime import datetime

arduino = serial.Serial('COM4', 9600, timeout=1)  

while True:

    if arduino.in_waiting > 0:
        linha = arduino.readline().decode('utf-8').strip()

        if linha == "Bomba acionada":
            hora_acionamento = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Bomba acionada em: {hora_acionamento}")

            with open("registro_acionamentos.txt", "a") as arquivo:
                arquivo.write(f"Bomba acionada em: {hora_acionamento}\n")
    
    time.sleep(1)