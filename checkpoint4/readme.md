# Checkpoint 1 — Comunicação I²C

O objetivo desta atividade é estabelecer a comunicação entre um Raspberry Pi e um Arduino Uno utilizando o protocolo I²C. O Raspberry Pi executa um programa em Python que envia comandos ao Arduino, configurado no endereço `0x08`, para ligar e desligar o LED integrado à placa.

A montagem utiliza as conexões SDA e SCL para a comunicação I²C, além de um GND comum entre as placas. No Raspberry Pi, o SDA corresponde ao pino físico 3 (GPIO 2) e o SCL ao pino físico 5 (GPIO 3). No Arduino Uno, são utilizados os pinos SDA (A4) e SCL (A5). Um conversor bidirecional de nível lógico deve ser utilizado entre as placas, pois o Raspberry Pi opera com sinais de 3,3 V e o Arduino Uno com sinais de 5 V.

O firmware do Arduino foi desenvolvido em C/C++ utilizando a biblioteca `Wire`, responsável pela comunicação I²C. O script Python utiliza a biblioteca `smbus` para enviar os comandos ao dispositivo.

A demonstração consiste em executar o programa no Raspberry Pi e verificar se o LED do Arduino liga e desliga conforme os comandos enviados. O Monitor Serial também pode ser utilizado para acompanhar os comandos recebidos.

