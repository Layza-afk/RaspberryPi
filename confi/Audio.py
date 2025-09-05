# Arquivo que cuidara de receber e tratar o audio do microfone. 
# Autor: Layza Vitoria
# Since: 04-09-2025

import speech_recognition as sr; # biblioteca que auxilia no reconhecimento de voz
import os; # biblioteca responsavel por auxiliar na conversa com o Sistema Operacional.

r = sr.Recognizer(); 

def ouvir_microfone():
    
    with sr.Microphone() as source:
        print("Raspberry pi: apto para ouvir...");
        r.adjust_for_ambient_noise(source, duration=1.0);
        audio = r.listen(source, timeout=5);
    try:
        comando = r.recognize_google(audio, language="pt-BR");
        print("Você falou: " + comando);
        return comando;

    except sr.UnknownValueError:
        print("Raspberry Pi: desculpe, não entendi");
    except  sr.RequestError as e:
        print("Raspberry Pi: problemas ao se conectar com o servidor {0}".format(e));