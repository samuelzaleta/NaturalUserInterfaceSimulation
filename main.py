import nltk
from dispositivos import dispositivo
import random
from nltk import word_tokenize
from nltk.corpus import stopwords
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def playaudio(text):
    audio =gTTS(text=text, lang='es', tld='com.mx')
    audio.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')

def playmicrophone_10s():
    recog = sr.Recognizer()
    mic = sr.Microphone()
    with mic as audio_file:
        print('Empienza hablar')
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file,timeout=10)
        print("Convietiendo tu speech a Texto...")
        try:
            transcript = recog.recognize_google(audio, language='es-us')
            transcript_raw = str(format(transcript))
            trans_lower = transcript_raw.lower()
            print(trans_lower)
        except Exception as e:
            print("Error: " + str(e))
    return trans_lower

def opcionesMenu(respuesta):
    tokens = word_tokenize(respuesta)
    print(tokens)
    palabras_vacias = set(stopwords.words('spanish'))
    tokens = [w for w in tokens if not w in palabras_vacias]
    print(tokens)
    accion = 0
    for w in range(len(tokens)):
        if tokens[w] == 'configuraciones':
            accion =1
        elif tokens[w] =='dispositivos':
            accion +=2
        elif tokens[w] =='buscar':
            accion +=1
        elif tokens[w] =='cerrar':
            playaudio('Cerrando aplicacion')
            break
        else:
            playaudio('Tu respuesta no coincide con las opciones del menú intenta otra vez')
            main()
    return accion

def configuracion():
    playaudio('¿Quieres subir o bajarle audio?')
    respuesta =word_tokenize(playmicrophone_10s())
    print(respuesta)
    if ('bajale' or 'bajar') and 'audio' in respuesta:
        print('Bajando volumen')
        playaudio('se bajó el volumen')

def buscarDispositivo():
    x = random.choice(range(0,11))
    if x%2 == 0:
        playaudio('No se encontro dispositivo')
    else:
        pass

def main():
    # playaudio('¿Que opciones de menú desea? Mis dispositivos; Buscar dispositivos; Configuraciones')
    respuesta1 = playmicrophone_10s()
    respuesta2 = opcionesMenu(respuesta1)

    if respuesta2 == 1:
        configuracion()
    elif respuesta2 == 2:
        pass
    elif respuesta2 == 3:
        playaudio('Usted seleccionó buscar dispositivo')
        buscarDispositivo()
if __name__ == '__main__':
    # playaudio('Bienvenido a mixisdomotic')
    # playaudio('Hola soy el señor mixis')
    main()