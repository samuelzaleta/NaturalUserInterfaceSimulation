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
    audio = gTTS(text=text, lang='es', tld='com.mx')
    audio.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')

def playmicrophone_10s():
    recog = sr.Recognizer()
    mic = sr.Microphone()
    with mic as audio_file:
        print('Empienza hablar')
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
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
        accion = 1
        return accion
    elif 'mis' in tokens:
        accion = 2
        return accion
    elif 'buscar' in tokens:
        accion = 3
        return accion
    elif 'cerrar' in tokens:
        accion = 4
        return accion
    else:
        accion = 5
        return accion

def configuracion():
    playaudio('¿Quieres subir o bajarle audio?')
    respuesta = word_tokenize(playmicrophone_10s())
    print(respuesta)
    if 'bajar' in respuesta:
        print('Bajando volumen')
        playaudio('se bajó el volumen')
        playaudio('Regresando a menú')
        main()
    elif 'subir' in respuesta:
        print('subiendo el volumen')
        playaudio('el volumen está más alto')
        playaudio('Regresando a menú')
        main()
    else:
        playaudio('Las respuestas no coinciden, trata de nuevo')
        configuracion()

def buscarDispositivo():
    x = random.choice(range(1,11))
    playaudio('Buscando dispositivos')
    if x % 2 == 0:
        playaudio('Dispositivo encontrado')
        agregarDispositivo()
    else:
        playaudio('No se encontro dispositivo')
        playaudio('Regresando a menu')
        main()

def misDispositivos():
    numdisposit = str(len(dispositivos))
    playaudio('Usted tiene ' + numdisposit + 'Dispositivos')
    playaudio('¿Que opcion desea? agregar dispositivo, '
              + 'eliminar dispositivo, activar dispositivo o desactivar dispositivo')
    respuesta = word_tokenize(playmicrophone_10s())
    print(respuesta)
    if 'agregar' in respuesta:
        agregarDispositivo()
    elif 'eliminar' in respuesta:
        eliminarDispositivo()
    elif 'activar' in respuesta:
        activarDispositivo()
    elif 'desactivar' in respuesta:
        desactivarDispositivo()
    else:
        playaudio('Su respuesta no coincide con la opciones por favor intente de nuevo')
        misDispositivos()
def agregarDispositivo():
    playaudio('¿Cual será el nombre del nuevo dispositivo?')
    respuesta = str(playmicrophone_10s())
    print(respuesta)
    dispositivos.append([respuesta,False])
    playaudio('Se ha agregado el dispositivo ' + respuesta)
    print(dispositivos)
    main()

def eliminarDispositivo():
    playaudio('¿Que dispositivo elimino?')
    for i in range(len(dispositivos)):
        dis = str(dispositivos[i][0])
        playaudio(dis)
    respuesta =str(playmicrophone_10s())
    print(respuesta)
    for i in range(len(dispositivos)):
        print(dispositivos[i])
        if dispositivos[i][0] == respuesta:
            del dispositivos[i]
            print(dispositivos)
            playaudio('eliminando dispositivo')
            playaudio('regresando a menú')
            main()

def activarDispositivo():
    playaudio('¿que dispositivo activo?')
    for i in range(len(dispositivos)):
        dis =str(dispositivos[i])
        playaudio(dis)
    respuesta = str(playmicrophone_10s())
    print(respuesta)
    for i in range(len(dispositivos)):
        if dispositivos[i][0] == respuesta:
            dispositivos[i][1] = True
            print(dispositivos)
            playaudio('Se ha activado dispositivo' + str(dispositivos[i][0]))
            playaudio('Regresando a menú')
            main()

def desactivarDispositivo():
    playaudio('¿que dispositivo desaactivo?')
    for i in range(len(dispositivos)):
        dis = str(dispositivos[i])
        playaudio(dis)
    respuesta = str(playmicrophone_10s())
    for i in range(len(dispositivos)):
        if dispositivos[i][0] == respuesta:
            dispositivos[i][1] = False
            print(dispositivos)
            playaudio('Se ha desactivado dispositivo' + str(dispositivos[i][0]))
            playaudio('Regresando a menú')
            main()

def main():
    playaudio('¿Que opciones de menú desea? Mis dispositivos; Buscar dispositivos; Configuraciones; Cerrar aplicación')
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
    playaudio('Bienvenido a mixisdomotic')
    playaudio('Hola soy el señor mixi')
    main()
