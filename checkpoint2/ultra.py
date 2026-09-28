from gpiozero import DistanceSensor, LED
from time import sleep

# Sensor ultrassônico HC-SR04
sensor = DistanceSensor(
    echo=27,
    trigger=17,
    max_distance=4
)

# LEDs
led1 = LED(23)
led2 = LED(24)
led3 = LED(26)
led4 = LED(22)

leds = [led1, led2, led3, led4]


def atualizar_leds(distancia_cm):

    # Primeiro apaga todos os LEDs
    for led in leds:
        led.off()

    # Quanto mais perto, mais LEDs acendem
    if distancia_cm <= 10:
        quantidade = 4

    elif distancia_cm <= 20:
        quantidade = 3

    elif distancia_cm <= 30:
        quantidade = 2

    elif distancia_cm <= 40:
        quantidade = 1

    else:
        quantidade = 0

    for i in range(quantidade):
        leds[i].on()

    return quantidade


try:

    print("Sensor ultrassônico iniciado.")
    print("Quanto mais próximo o objeto, mais LEDs acendem.")
    print("CTRL+C para encerrar.\n")

    while True:

        distancia_cm = sensor.distance * 100

        quantidade = atualizar_leds(distancia_cm)

        print(
            "Distância: {:.1f} cm | LEDs acesos: {}".format(
                distancia_cm,
                quantidade
            )
        )

        sleep(0.2)


except KeyboardInterrupt:

    print("\nPrograma encerrado.")


finally:

    for led in leds:
        led.off()

    sensor.close()

    for led in leds:
        led.close()

    print("GPIOs liberadas.")
