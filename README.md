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

Abaixo estará listado os itens referentes a execução do proejto físico:

|item                   |Descrição de Uso                           |
|:---------------------:|:-----------------------------------------:|
|Raspberry Pi B         |Base de Controle                           |
|Microfone USB          |Enviar os sinais de comando                |
|Lâmpadas 220v          |                  -                        |
|Relé (1 a 5 canais)    |Controlará as lâmpadas, suportando 250v    |
|ProtoBoard             |                  -                        |

## CONFIGURANDO AMBIENTE
Para que possamos trabalhar com a captura do audio, iremos usar duas bibliotecas: PyAudio e speech_recognition. Para usa-las, precisamos instalar ambas no nosso ambiente.

Para a speech_recognition se usa no terminal:
> pip install SpeechRecognition
e para verificar a instalação:
> pip show SpeechRecognition

Para o PyAudio:
> pip install pyaudio
e verificar sua instalação e versão:
> pip show pyaudio

## ORGANIZAÇÃO DOS ARQUIVOS

> ...

## REFERÊNCIAS
+ [Carlos. Reconhecimento de voz com Python (Speech-to-text) no jarviz](https://www.dio.me/articles/reconhecimento-de-voz-com-python-speech-to-text-no-jarvis-3387c1aa2c31)
+ 