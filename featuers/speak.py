# Made by Kartik
import pyttsx3

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('vooices',voices[0].id)
    engine.setProperty('rate', 175)
except Exception as e:
    print(" Sorry this program is unable to initialize speaking device"
    "or voices in your pc, \ntherefore Jarvis can't speak. ")
    print(f"Error message: {e}")

def speak(query):

    """ This function gives ability to speak to our jarvis. """
    try:
        engine.say(text=query)
        print(f"Jarvis 2.0: {query}")
        engine.runAndWait()
    
    except Exception as e:
        print(" Sorry, Unfortunately jarvis can't speak. ")
        print(f"Error message: {e}")
        print(f"\nJarvis 2.0: {query}")

def save_audio_file(query, filename):

    """ This  function contert text to speech and then save it to a given file. """
    
    engine.save_to_file(query, filename)

if __name__ == '__main__':
    speak("Hello Sumang")
    pass
