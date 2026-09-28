import RPi.GPIO as GPIO

LED = 23

FREQUENCIA_PWM = 1000

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, FREQUENCIA_PWM)

pwm.start(0)

print("Controle de brilho do LED por PWM")
print("Digite um duty cycle entre 0 e 100.")
print("Digite 'sair' para encerrar o programa.")

try:
    while True:
        entrada = input("\nDuty cycle (%): ")

        # Permite encerrar o programa digitando "sair"
        if entrada.lower() == "sair":
            break

        try:
            # Converte o valor digitado para número decimal
            duty_cycle = float(entrada)

            # Verifica se o valor está dentro da faixa válida
            if duty_cycle < 0 or duty_cycle > 100:
                print("Erro: digite um valor entre 0 e 100.")
                continue

            # Altera o duty cycle do sinal PWM
            pwm.ChangeDutyCycle(duty_cycle)

            print(
                "Duty cycle ajustado para {:.1f}%.".format(duty_cycle)
            )

        except ValueError:
            # Impede o encerramento do programa caso seja digitado texto inválido
            print("Erro: digite um número entre 0 e 100.")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    # Encerra o PWM e libera os pinos GPIO
    pwm.stop()
    GPIO.cleanup()
    print("PWM encerrado e GPIO liberada.")
