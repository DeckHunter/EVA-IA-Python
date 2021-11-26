import speech_recognition as sr
from math import frexp
import wikipedia
import datetime
import pyttsx3
import os


def Executar_Comando():
    #Habilitar Microfone
    microfone = sr.Recognizer()
    eva = pyttsx3.init()

    #Usar Microfone
    with sr.Microphone() as source:

        #Algoritomo De Reduçao de Ruidos 
        microfone.adjust_for_ambient_noise(source)

        #Frase Para O Ususario Dizer Algo
        print("Fale Alguma Coisa")

        #Armazena Oque Foi Dito 
        audio = microfone.listen(source)
    try:
        #Passa As Variaveis Para O Algoritimo Reconhecer Padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        frase = frase.lower()

        #Frase Que Voce Disse
        print("Você Disse -> "+ frase)
        
        if "eva" in frase:
            frase = frase.replace('eva','')
            if "apresente" in frase:
                    eva.say("Olá, eu sou a Eva, tenho atualmente, Duas horas,e 35 segundos de idade, como pode ver, ainda estou em desenvolvimento")
                    eva.runAndWait()
            elif "navegador" in frase:
                os.system("start Chrome.exe")
                eva.say("Navegador Aberto")
                eva.runAndWait()
            elif "hora" in frase:
                hora = datetime.datetime.now().hour
                minuto = datetime.datetime.now().minute
                eva.say("Agora são " + str(hora) + "Horas e" + str(minuto) + "minutos")
                eva.runAndWait()
            elif "procure por" in frase:
                procurar = frase.replace('procure por','')
                print("Procurar -> "+procurar)
                wikipedia.set_lang('pt')
                resultado = wikipedia.summary(procurar,2)
                print(resultado)
                eva.say(resultado)
                eva.runAndWait()

    #Não Reconheceu o Padrão Da Fala
    except sr.UnknownValueError:
        print("Não Entendi ")
    return frase

Executar_Comando()
