# Librería para el reconocimiento de voz
import speech_recognition as sr
# Librería para abrir el navegador
import webbrowser as wb
# Librería para realizar la síntesis de voz
import pyttsx3 as pt

recongnizer =sr.Recognizer()

engine = pt.init()

def hablar():
    mic = sr.Microphone()
    with mic as source:
        print("Di algo...")
        audio = recongnizer.listen(source)
    texto = recongnizer.recognize_sphinx(audio,language='ES')
    print(f'Has dicho {texto}')

    return texto.lower()

try :
    
    if 'amazon' in hablar():
        engine.say('Qué quieres comprar en Amazon')
        engine.runAndWait()
        text = hablar()
        wb.open(f'https://www.amazon.es/s?k={text}')
except Exception as e:
    print(f'No has dicho nada, error: {e}')
