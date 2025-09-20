#import RPi.GPIO as GPIO; # biblit5eca do raspberry pi que cuida dos pinos - ainda não importada kkk

def setup(comando):
    print("Setup iniciado...");
    comando = comando.lower();

    try:
        match comando:
            case "ligar luz azul":
                #GPIO.output(18, GPIO.HIGH);
                print("Luz azul ligada");
            
            case "ligar luz vermelha":
                #GPIO.output(23, GPIO.HIGH);
                print("luz vermelha ligada");

            case "ligar luz laranja":
                #GPIO.output(24, GPIO.HIGH);
                print("luz vermelha laranja");
            
            case "desligar luzes":
                #GPIO.output(18, GPIO.LOW);
                #GPIO.output(23, GPIO.LOW);
                #GPIO.output(24, GPIO.LOW);
                print("luzes desligadas");

            case _:
                print("Comando não reconhecido");
    except Exception as e:
        print(f"Erro no setup: {e}");