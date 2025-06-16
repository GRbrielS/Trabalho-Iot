---

# 🔐 Sistema de Monitoramento de Segurança com Arduino

Este é um projeto de **Internet das Coisas (IoT)** desenvolvido para monitorar portas em ambientes físicos. Utilizando sensores magnéticos, o sistema é capaz de indicar o status de uma porta (aberta ou fechada) e emitir alertas sonoros em caso de abertura indevida.

---

## 📌 Objetivo

Atender à demanda de uma empresa por um sistema de monitoramento noturno simples e funcional, utilizando Arduino e sensores de baixo custo para detectar a abertura de portas de forma imediata e visual/sonora.

---

## 🛠️ Materiais Utilizados

* **Arduino Uno**
  Microcontrolador responsável por processar os sinais recebidos e controlar os dispositivos de saída.

* **Sensor Hall A3144**
  Sensor magnético que detecta a presença de um campo magnético. Utilizado para identificar se a porta está aberta ou fechada com base na posição de um ímã.

* **LED Vermelho**
  Acende quando a porta está **fechada**, fornecendo uma indicação visual do status seguro.

* **Buzzer Ativo**
  Emite um som sempre que a porta é **aberta**, funcionando como alarme imediato.

* **Mini Breadboard**
  Placa de ensaio para montagem dos circuitos, dispensando a necessidade de solda e facilitando modificações.

* **Fios Jumpers**
  Utilizados para fazer as conexões entre os componentes e o Arduino.

---

## 🧩 Diagrama Esquemático

Visualização da montagem do sistema no circuito:

![Diagrama esquemático Arduino](https://github.com/user-attachments/assets/364f6f3b-ae68-4b62-9702-c044c7d255f7)

---

## ⚙️ Funcionamento

* Quando a porta está **fechada** (ímã próximo ao sensor Hall):

  * O **LED vermelho** permanece aceso.
  * O **buzzer** permanece desligado.

* Quando a porta está **aberta** (ímã afastado do sensor):

  * O **LED se apaga**.
  * O **buzzer** é ativado, alertando sobre a abertura.

---

## 🧪 Protótipo

Imagem do protótipo montado:

![Protótipo](https://github.com/user-attachments/assets/2b33848f-1434-4978-b54c-3577bb666950)

---

## 👨‍💻 Colaboradores

* Gabriel Sinis da Silva
* Jorge Luiz de França Mendes da Silva Júnior
* Eduardo Scarpini Lessa Fonseca

---
