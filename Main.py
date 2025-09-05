# Arquivo principal do projeto. Iniciara o sistema e ajudara na concatenização dos outros scripts.
# Autor: Layza Vitoria
# Since: 04-09-2025
# Version: 0.0.1~

from confi.Audio import ouvir_microfone

class Main:
    def __init__(self):
        print("Iniciando o sistema...")
        ouvir_microfone()

if __name__ == "__main__":
    Main()