# Checkpoint 1 — Comunicação I²C

O objetivo desta atividade é estabelecer a comunicação entre um Raspberry Pi e um Arduino Uno utilizando o protocolo I²C. O Raspberry Pi executa um programa em Python que envia comandos ao Arduino, configurado no endereço `0x08`, para ligar e desligar o LED integrado à placa.

O firmware do Arduino foi desenvolvido em C/C++ utilizando a biblioteca `Wire`, responsável pela comunicação I²C. O script Python utiliza a biblioteca `smbus` para enviar os comandos ao dispositivo.

A demonstração consiste em executar o programa no Raspberry Pi e verificar se o LED do Arduino liga e desliga conforme os comandos enviados. O Monitor Serial também pode ser utilizado para acompanhar os comandos recebidos.

