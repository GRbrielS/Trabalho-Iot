import serial
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de email
EMAIL_REMETENTE = "ard####@gmail.com"
EMAIL_SENHA = "bfsg####rwmmtc" 
EMAIL_DESTINO = "na#####@gmail.com"


# Configuração da porta serial
porta = serial.Serial('COM6', 9600)  # Não esquecer de colocar a porta certa do usb
time.sleep(2)  # Aguarda conexão estabilizar

def dentro_do_horario():
    agora = datetime.now().time()
    return agora.hour >= 8 or agora.hour < 5# ALTERAR O HORARIO PRA MOSTRAR O PROJETO FUNCINANDO (BASED)

def enviar_email():
    agora = datetime.now()
    assunto = "🚨 Alerta: Porta Aberta"
    corpo = f"O sensor Hall detectou que a porta foi aberta às {agora.strftime('%H:%M:%S')} do dia {agora.strftime('%d/%m/%Y')}."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINO
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_REMETENTE, EMAIL_SENHA)
        server.send_message(msg)
        server.quit()
        print("Email enviado")
    except Exception as e:
        print("Erro ao enviar o email:", e)

# Loop que escuta o Arduino
while True:
    if porta.in_waiting > 0:
        linha = porta.readline().decode('utf-8').strip()
        print("Arduino:", linha)

        if "ALERTA: Porta aberta" in linha:
            if dentro_do_horario():
                enviar_email()
            else:
                print("⚠️ Porta aberta fora do horário de vigilância. Nenhum e-mail enviado.")
