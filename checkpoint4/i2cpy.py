
from smbus import SMBus

I2C_ADDRESS = 0x08
I2C_BUS = 1

bus = SMBus(I2C_BUS) 
    print("Controle do LED via I2C")
    print("1 = ligar | 0 = desligar | qualquer outra tecla = sair")

    while True:
        comando = input("Comando: ").strip()

        if comando not in ("0", "1"):
            print("Encerrando.")
            break

        try:
            bus.write_byte(I2C_ADDRESS, int(comando))
            print(f"Comando {comando} enviado.")
        except OSError as erro:
            print(f"Erro na comunicacao I2C: {erro}")
