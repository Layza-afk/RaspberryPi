# AUTOMAÇÃO DE LÂMPADAS COM RASPBERRY PI E VOZ

> Projeto desenvolvido para automatizar lâmpadas de diferentes cores utilizando um Raspberry Pi e comandos de voz, para 
> contribuir no aprendizado de física. Sob a liderança da Prof. Gislene Micarla Borges de Lima da UFersa angicos, professora de
> física e dona da sala escura, espaço voltado a expor diversos experimentos físicos.

## CONFIGURAÇÕES
Linguagens e bibiotecas que seram usadas para automatizar o raspberry pi B a receber comando por voz e a processa-los:

|Linguagem      |Biblioteca         |Descrição de uso                                   |
|:-------------:|:-----------------:|:-------------------------------------------------:|
|Python         |speech_recognition |trata a voz                                        |
|       -       |PyAudio            |Captura o audio                                    | 
|       -       |os                 |Auxilia com a interação com o Sistema Operacional  |

Abaixo estará listado os itens referentes a execução do projeto físico:

|item                   |Descrição de Uso                           |
|:---------------------:|:-----------------------------------------:|
|Raspberry Pi 3 Model B |Base de Controle                           |
|Microfone USB          |Enviar os sinais de comando                |
|Lâmpadas 220v          |                  -                        |
|Relé (1 a 5 canais)    |Controlará as lâmpadas, suportando 250v    |
|ProtoBoard             |                  -                        |

## CONFIGURANDO AMBIENTE
Para que possamos trabalhar com a captura do audio, iremos usar duas bibliotecas: PyAudio e speech_recognition. Para usa-las, precisamos instalar ambas no nosso ambiente.

### BIBLIOTECAS
Para a speech_recognition e o Pyaudio respectivamente:
```Bash
pip install SpeechRecognition
```
```Bash
pip install pyaudio
```
Verificar e instalação:
```Bash
pip show SpeechRecognition
```
```Bash
pip show pyaudio
```

### RASPBERRY PI
Com as dependencias instalada, precisamos também configurar e instalar um sistema operacional em nosso RaspBerry Pi. Para isso, usamos o __RaspBerry Pi Imager__ um software fornecido pela propria desenvolvedora do circuito:
[RaspBerry Pi Imager](https://www.raspberrypi.com/software/)

--- mostrar ikmagem do raspberry pi imager

Há duas formas de usarmos o nosso Raspberry pi. Uma pelo terminal do nosso proprio computador, usando SSH e a outra colocando um teclado, monitor e mouse no raspberry e usa-lo como um computador
**ATENÇÃO:** em versões mais antigas do RaspBerry, é um pouco desconfortavel trabalhar diretamente nele.

1. Primerio Método - Via SSH

## ORGANIZAÇÃO DOS ARQUIVOS

> ...

## LÓGICA 

## REFERÊNCIAS
+ [Carlos. Reconhecimento de voz com Python (Speech-to-text) no jarviz](https://www.dio.me/articles/reconhecimento-de-voz-com-python-speech-to-text-no-jarvis-3387c1aa2c31)
+ 