import RPi.GPIO as GPIO
import time
import sys

# Configuração do pino do LED utilizando numeração BCM
LED = 17

# Define o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Configura o LED como saída
GPIO.setup(LED, GPIO.OUT)

# Garante que o LED comece apagado
GPIO.output(LED, GPIO.LOW)


# Função responsável pela contagem regressiva
def contagem_regressiva(tempo):
    for restante in range(tempo, 0, -1):
        # Divide o tempo restante em minutos e segundos
        minutos, segundos = divmod(restante, 60)

        # Exibe a contagem no formato MM:SS, sempre na mesma linha
        sys.stdout.write(
            "\rTempo restante: {:02d}:{:02d}".format(minutos, segundos)
        )
        sys.stdout.flush()

        time.sleep(1)

    # Exibe 00:00 ao finalizar
    sys.stdout.write("\rTempo restante: 00:00\n")
    sys.stdout.flush()

    # Acende o LED ao final da contagem
    GPIO.output(LED, GPIO.HIGH)
    print("Contagem finalizada! LED aceso.")


try:
    while True:
        try:
            # Recebe o valor digitado pelo usuário
            entrada = input("Digite o tempo da contagem em segundos: ")

            # Type casting para inteiro
            tempo = int(entrada)

            # Verifica se o tempo informado é válido
            if tempo <= 0:
                print("Erro: o número deve ser positivo.")
                continue

            break

        except ValueError:
            # Impede que uma entrada não numérica encerre o programa
            print("Erro: o valor digitado deve ser um número inteiro.")

    # Executa a função de contagem regressiva
    contagem_regressiva(tempo)

    # Mantém o LED aceso após o fim da contagem
    print("Pressione CTRL+C para encerrar o programa.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    # Libera os pinos quando o programa for encerrado
    GPIO.cleanup()
    print("GPIO liberada com sucesso.")
