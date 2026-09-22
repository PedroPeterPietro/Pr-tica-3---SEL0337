import RPi.GPIO as GPIO
import time

# Configuração dos pinos utilizando a numeração BCM
LED = 17
BOTAO = 27

# Define o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Configura o LED como saída
GPIO.setup(LED, GPIO.OUT)

# Configura o botão como entrada com resistor Pull-Up interno
GPIO.setup(BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Garante que o LED comece apagado
GPIO.output(LED, GPIO.LOW)


# Função chamada sempre que ocorre mudança de estado no botão
def evento_botao(canal):
    # Com Pull-Up, botão pressionado corresponde ao nível LOW
    if GPIO.input(BOTAO) == GPIO.LOW:
        GPIO.output(LED, GPIO.HIGH)
        print("Botão pressionado - LED aceso")
    else:
        GPIO.output(LED, GPIO.LOW)
        print("Botão solto - LED apagado")


# Detecta tanto a borda de descida quanto a borda de subida
GPIO.add_event_detect(
    BOTAO,
    GPIO.BOTH,
    callback=evento_botao,
    bouncetime=50
)

print("Programa iniciado.")
print("Pressione o botão para acender o LED.")
print("Pressione CTRL+C para encerrar.")

try:
    # Mantém o programa em execução enquanto os eventos são detectados
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    # Desliga o LED e libera os pinos GPIO
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO liberada com sucesso.")
