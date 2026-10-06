from gpiozero import DistanceSensor, LED
from time import sleep
import threading

# -----------------------------
# Configuração do hardware
# -----------------------------

# Sensor ultrassônico HC-SR04
sensor = DistanceSensor(
    echo=27,
    trigger=17,
    max_distance=4
)

# LEDs
leds = [
    LED(23),
    LED(24),
    LED(25),
    LED(22)
]

# -----------------------------
# Variáveis compartilhadas
# -----------------------------

# Distância medida pelo sensor
distancia_cm = 0.0

# Mutex para proteger o acesso à variável compartilhada
mutex = threading.Lock()

# Evento usado para encerrar todas as threads
encerrar = threading.Event()


# -----------------------------
# Thread 1 - leitura do sensor
# -----------------------------

def ler_sensor():
    global distancia_cm

    while not encerrar.is_set():

        # gpiozero fornece a distância em metros
        nova_distancia = sensor.distance * 100

        # Apenas uma thread por vez pode acessar a variável
        with mutex:
            distancia_cm = nova_distancia

        sleep(0.1)


# -----------------------------
# Thread 2 - controle dos LEDs
# -----------------------------

def controlar_leds():

    while not encerrar.is_set():

        # Copia com segurança o valor da distância
        with mutex:
            distancia = distancia_cm

        # Primeiro apaga todos os LEDs
        for led in leds:
            led.off()

        # Quanto mais próximo o objeto estiver,
        # mais LEDs serão acesos
        if distancia <= 10:
            quantidade = 4

        elif distancia <= 20:
            quantidade = 3

        elif distancia <= 30:
            quantidade = 2

        elif distancia <= 40:
            quantidade = 1

        else:
            quantidade = 0

        # Acende a quantidade correta de LEDs
        for i in range(quantidade):
            leds[i].on()

        sleep(0.05)


# -----------------------------
# Thread 3 - exibição no terminal
# -----------------------------

def mostrar_distancia():

    while not encerrar.is_set():

        # Faz uma cópia protegida da distância atual
        with mutex:
            distancia = distancia_cm

        print("Distância: {:.1f} cm".format(distancia))

        sleep(0.5)


# -----------------------------
# Programa principal
# -----------------------------

try:

    print("Aplicação iniciada.")
    print("Sensor, LEDs e terminal funcionando em threads.")
    print("Pressione CTRL+C para encerrar.\n")

    # Cria as três threads
    thread_sensor = threading.Thread(target=ler_sensor)
    thread_leds = threading.Thread(target=controlar_leds)
    thread_terminal = threading.Thread(target=mostrar_distancia)

    # Inicia as threads
    thread_sensor.start()
    thread_leds.start()
    thread_terminal.start()

    # Mantém o programa principal ativo
    while True:
        sleep(1)


except KeyboardInterrupt:

    print("\nEncerrando o programa...")

    # Sinaliza para todas as threads encerrarem
    encerrar.set()


finally:

    # Espera as threads terminarem
    if 'thread_sensor' in locals():
        thread_sensor.join()

    if 'thread_leds' in locals():
        thread_leds.join()

    if 'thread_terminal' in locals():
        thread_terminal.join()

    # Apaga os LEDs
    for led in leds:
        led.off()
        led.close()

    # Libera o sensor
    sensor.close()

    print("GPIOs liberadas e programa finalizado.")
