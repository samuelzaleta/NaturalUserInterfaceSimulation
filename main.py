import random
from nltk import word_tokenize
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

'''
Dispositivos por default
'''
dispositivos = [
    ['dispositivo 1', False],
    ['dispositivo 2', False],
    ['dispositivo 3', False],
    ['dispositivo 4', False]
]
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
    if 'configuraciones' in tokens:
        accion =1
        return accion
    elif 'mis' and 'dispositivos' in tokens:
        accion =2
        return accion
    elif 'buscar' and 'dispositivos' in tokens:
        accion =3
        return accion
    elif ('cerrar' or 'cierra') and 'aplicación' in tokens:
        accion = 4
        return accion
    else:
        accion = 5
        return accion

def configuracion():
    playaudio('¿Quieres subir o bajarle audio?')
    respuesta =word_tokenize(playmicrophone_10s())
    print(respuesta)
    if ('bajale' or 'bajar') and ('audio' or 'volumen') in respuesta:
        print('Bajando volumen')
        playaudio('se bajó el volumen')
    elif ('subele' or 'subir') and ('audio' or 'volumen') in respuesta:
        print('subiendo el volumen')
        playaudio('el volumen está más alto')
    playaudio('Regresando a menú')
    main()
def buscarDispositivo():
    x = random.choice(range(1,11))
    playaudio('Buscando dispositivos')
    if x%2 == 0:
        print('Hola')
    else:
        playaudio('No se encontro dispositivo')
        playaudio('Regresando a menu')
        main()

def misDispositivos():
    numdisposit = str(len(dispositivos))
    playaudio('Usted tiene ' + numdisposit + 'Dispositivo')
    playaudio('¿Que opcion desea? agregar dispositivo, eliminar dispositivo, activar dispositivo o desactivar dispositivo')
    respuesta  =playmicrophone_10s().split(" ")
    if 'agregar' and ('dispositivo' or 'dispositivos') in respuesta:
        agregarDispositivo()
    elif 'eliminar' and ('dispositivo' or 'dispositvos') in respuesta:
        eliminarDispositivo()
    elif 'activar' and ('dispositivo' or 'dispositvos') in respuesta:
        activarDispositivo()
    elif 'desactivar' and ('dispositivo' or 'dispositvos') in respuesta:
        desactivarDispositivo()
    else:
        playaudio('Su respuesta no coincide con la opciones por favor intente de nuevo')
        misDispositivos()
def agregarDispositivo():
    playaudio('¿Cual será el nombre del nuevo dispositivo?')
    respuesta = str(playmicrophone_10s())
    print(respuesta)
    dispositivos[len(dispositivos) -1] =[respuesta,False]
    playaudio('Se ha agregado el dispositivo ' + respuesta)
    print(dispositivos)
    main()

def eliminarDispositivo():
    playaudio('¡Que dispositivo elimino?')
    for i in range(len(dispositivos)):
        playaudio(dispositivos[i])
    respuesta =str(playmicrophone_10s())
    print(respuesta)
    for i in range(len(dispositivos)):
        if dispositivos[i] == respuesta:
            playaudio('Se ha eliminado ' + respuesta)
            del dispositivos[i]
            break

def activarDispositivo():
    playaudio('¿que dispositivo activo?')
    for i in range(len(dispositivos)):
        playaudio(dispositivos[i])
    respuesta = word_tokenize(playmicrophone_10s())
    print(respuesta)
    for i in range(len(dispositivos)):
        if dispositivos[i] == respuesta:
            dispositivos[i][1]= True

def desactivarDispositivo():
    playaudio('¿que dispositivo activo?')
    for i in range(len(dispositivos)):
        playaudio(dispositivos[i])
    respuesta = word_tokenize(playmicrophone_10s())
    for i in range(len(dispositivos)):
        if dispositivos[i] == respuesta:
            dispositivos[i][1] = False

def main():
    #playaudio('¿Que opciones de menú desea? Mis dispositivos; Buscar dispositivos; Configuraciones; Cerrar aplicación')
    respuesta1 = playmicrophone_10s()
    respuesta2 = opcionesMenu(respuesta1)

    if respuesta2 == 1:
        playaudio('Usted seleccionó configuración')
        configuracion()
    elif respuesta2 == 2:
        playaudio('Usted seleccionó mis dispositivos')
        misDispositivos()
    elif respuesta2 == 3:
        playaudio('Usted seleccionó buscar dispositivo')
        buscarDispositivo()
    elif respuesta2 == 4:
        playaudio('Cerrando aplicación')
    elif respuesta2 ==5:
        playaudio('Tu respuesta no coincide con las opciones del menú intenta otra vez')
        main()
if __name__ == '__main__':
    #playaudio('Bienvenido a mixisdomotic')
    #playaudio('Hola soy el señor mixi')
    main()
