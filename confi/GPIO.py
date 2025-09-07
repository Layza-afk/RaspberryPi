#import RPi.GPIO as GPIO; # biblit5eca do raspberry pi que cuida dos pinos

def setup(comando):
    print("Setup iniciado...");
    comando = comando.lower();

    try:
        match comando:
            case "ligar luz azul":
                #GPIO.output(18, GPIO.HIGH);
                print("Luz azul ligada");
            
            case "ligar luz vermelha":
                print("luz vermelha ligada");

            case "ligar luz laranja":
                print("luz vermelha laranja");
            
            case "desligar luzes":
                print("luzes desligadas");

            case _:
                print("Comando não reconhecido");
    except Exception as e:
        print(f"Erro no setup: {e}");