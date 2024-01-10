# Made by Kartik
# from speak import speak
# from listen import listen
from youtubesearchpython import VideosSearch
import webbrowser
import random

flag_trans = True
flag_wiki = True
flag_speedt = True
flag_pywkh = True
flag_pywhatkit = True
flag_pyatg = True
flag_dt = True

# try:
#     from googletrans import Translator
# except ModuleNotFoundError:
#     flag_trans = False
try:
    import datetime
except ModuleNotFoundError:
    flag_dt = False
try:
    import wikipedia as wk
except ModuleNotFoundError:
    flag_wiki = False
try:
    from pywikihow import search_wikihow
except:
    flag_pywkh = False
try:
    import pyautogui as pg
except:
    flag_pyatg = False
try:
    from pywhatkit import search
except:
    flag_pywhatkit = False
try:
    import speedtest
except ModuleNotFoundError:
    flag_speedt = False


exit_res_list = [
                "Bye",
                "I am Going.",
                "Bye Sir",
                "Good Bye",
                "goodbye",
                "It'll be Nice To Meet You Again",
                "See You Later"
            ]

# speak function
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




# Welcome function
def welcome():
    """ this function will help jarvis to greet the user """
    msg = "Good Morning sir, Jarvis 2.0 here, please wait few seconds while i set up the environment"
    speak(msg)

# Non-Input Functions

def time():
    """ This function tells jarvis time. """
    if flag_dt:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"and It's {time}")
    else:
        speak("Sorry, dependencies are not installed "
        "at this moment \n Please install all the modules "
        "listed in requirements.txt.")


def date():
    " This function tell jarvis date. "
    if flag_dt:
        date = datetime.date.today()
        speak(f"todays is {date} ")
    else:
        speak("Sorry, dependencies are not installed at "
        "this moment \n Please install all the modules "
        "listed in requirements.txt.")

def check_speed():
    """ This function helps jarvis to calculate the upload and download speed """

    if flag_speedt:
        speak("Checking speed...")
        try:
            speed = speedtest.Speedtest()
            speak("Running speed test...")
            download_speed = speed.download()
            upload_speed = speed.upload()
            download_speed = int(download_speed/800000)
            upload_speed = int(upload_speed/800000)
            # print(download_speed)
            # print(upload_speed)
            speak(f"Your Download speed is {download_speed} Megabit per second and")
            speak(f"Your upload speed is {upload_speed} Megabit per second.")
        except speedtest.ConfigRetrievalError or Exception as e:
            speak("Something wrong happened,\nI'm unable to connect to internet at this time. ")
    else:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the modules "
        "listed in requirements.txt.")

def day():
    " This function tell jarvis day. "
    if flag_dt:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}")
    else:
        speak("Sorry, dependencies are not installed "
        "at this moment \n Please install all the "
        "modules listed in requirements.txt.")

def non_input_functions(function):
    """ 
    This function returns the non input function  when called in program.

    function: Non-Input function name. (Only string input)

    """
    function = str(function)
    if function.lower() == "time":
        time()
    
    elif function.lower() == "date":
        date()
    
    elif function.lower() == "day":
        day()
    elif function.lower() == "screenshot":
        take_screenshot()
    
    elif function.lower() == "internet_speed":
        check_speed()
      
    # elif function == "translate":
    #     translate_()

# Input Functions

def how_todo_with_steps(s_query):
    """"

    This function returns the searched text
    about query from wikipedia.

    s_query: Query to search.
    tag: Wikipedia (Needed)

    """
    
    if flag_pywkh:
        s_query = str(s_query).lower()
        removable_words = ["jarvis", "hii", "hello",
                           "please", "please tell me",
                           "tell me", "ok tell me", "ok"]
        for i in removable_words:
            s_query = str(s_query).replace(i, "")
        print(s_query)

        result = search_wikihow(s_query)
        result = result[0].summary
        speak(f"According to wikipedia:  {str(result)}")
    else:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the "
        "modules listed in requirements.txt.")


def wikipedia_(s_query):
    """"

    This function returns the searched text 
    about query from wikipedia.

    s_query: Query to search.
    tag: Wikipedia (Needed)

    """

    if flag_wiki:
        s_query = str(s_query).replace("what is ","")
        s_query = str(s_query).replace("Search on wikipedia","")
        s_query = str(s_query).replace("wikipedia","")
        s_query = str(s_query).replace("Search ","")
        s_query = str(s_query).replace("meaning of","")
        s_query = str(s_query).replace("who is","")
        s_query = str(s_query).replace("who","")
        s_query = str(s_query).replace("is","")
        s_query = str(s_query).replace("Jarvis","")
        try:
            result = wk.summary(s_query, sentences=2)
        except:
            search(s_query)
            result = "I found this on the web."
        speak(result)
    else:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the modules"
        " listed in requirements.txt.")

def google_search(s_query):
    """"

    This function returns the searched text about query from google.
    s_query: Query to search.

    """

    if flag_pywhatkit:

        query = str(s_query)
        query = query.replace('jarvis', "")
        query = query.replace('google', "")
        query = query.replace('search', "")
        query = query.replace('the', "")
        query = query.replace('on', "")
        search(query)

    else:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the modules"
        " listed in requirements.txt.")

# def translate_(query='None' ,lang='hi' ,TransLang='en'):
#     """
#      This function translate line hindi to english.
    
#     TransLang: language to which you want to translate. (Default: English)
#     TransLang: language given in input. (Default: hindi)

#     """
    
#     if flag_trans:

#         query = str(query)
#         if query == 'None':
#             speak("Tell Me The Text!")
#             query = str(listen())
#         if lang == 'hi' and TransLang == "en":
#             traslate = Translator()
#             result = traslate.translate(src='hi', text=query)
#             text = result.text
#         speak(f"Translated text is : {text}.")

#     else:
#         speak("Sorry, dependencies are not installed at"
#         " this moment \n Please install all the modules"
#         " listed in requirements.txt.")



def play_first_youtube_video(search_query):
    try:
        # Perform YouTube search
        videos_search = VideosSearch(search_query, limit = 1)
        results = videos_search.result()

        # Get the video URL of the first result
        video_url = results['result'][0]['link']

        # Open the video URL in the default web browser
        webbrowser.open(video_url)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def open_website(query):
    speak("Opening website sir..")
    if 'youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'google' in query:
        webbrowser.open("https://www.google.com")
    elif 'instagram' in query:
        webbrowser.open("https://www.instagram.com")
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com")
    elif 'geekforgeeks' in query or 'geeksforgeeks' in query:
        webbrowser.open("https://www.geeksforgeeks.org")
    elif 'github' in query:
        webbrowser.open("https://www.github.com")
    elif 'twitter' in query:
        webbrowser.open("https://www.twitter.com")
    elif 'linkedin' in query:
        webbrowser.open("https://www.linkedin.com")
    elif 'reddit' in query:
        webbrowser.open("https://www.reddit.com")
    elif 'stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com")
    elif 'wikipedia' in query:
        webbrowser.open("https://www.wikipedia.org")
    elif 'amazon' in query:
        webbrowser.open("https://www.amazon.com")
    elif 'ebay' in query:
        webbrowser.open("https://www.ebay.com")
    elif 'microsoft' in query:
        webbrowser.open("https://www.microsoft.com")
    elif 'apple' in query:
        webbrowser.open("https://www.apple.com")
    elif 'netflix' in query:
        webbrowser.open("https://www.netflix.com")
    elif 'spotify' in query:
        webbrowser.open("https://www.spotify.com")
    elif 'quora' in query:
        webbrowser.open("https://www.quora.com")
    elif 'udemy' in query:
        webbrowser.open("https://www.udemy.com")
    elif 'coursera' in query:
        webbrowser.open("https://www.coursera.org")
    elif 'pinterest' in query:
        webbrowser.open("https://www.pinterest.com")
    elif 'aliexpress' in query:
        webbrowser.open("https://www.aliexpress.com")
    elif 'stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com")
    elif 'gmail' in query:
        webbrowser.open("https://mail.google.com")
    elif 'outlook' in query:
        webbrowser.open("https://outlook.live.com")
    elif 'yahoo' in query:
        webbrowser.open("https://mail.yahoo.com")
    elif 'bing' in query:
        webbrowser.open("https://www.bing.com")
    elif 'duckduckgo' in query:
        webbrowser.open("https://duckduckgo.com")
    elif 'weather' in query:
        webbrowser.open("https://weather.com")
    elif 'bbc news' in query:
        webbrowser.open("https://www.bbc.com/news")
    else:
        speak("Website not recognized.")


def youtube_search(query):
    try:
        # Perform YouTube search
        search_url = f"https://www.youtube.com/results?search_query={'+'.join(query.split())}"
        
        # Open the search results in the default web browser
        webbrowser.open(search_url)

        # Alternatively, if you want to open the first video directly:
        # videos_search = VideosSearch(query, limit=1)
        # results = videos_search.result()
        # if results['result']:
        #     first_video_url = results['result'][0]['link']
        #     webbrowser.open(first_video_url)
        # else:
        #     print("No search results found.")

    except Exception:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the modules"
        " listed in requirements.txt.")


def take_screenshot():
    """ This function helps jarvis to take the screenshot. """
    
    if flag_trans:
 
        speak("Ok Sir")
        file_name = f"screenshot - {random.randint(1, 100000)}"
        file_name = file_name + ".png"
        path1 = file_name
        ss = pg.screenshot()
        ss.save(path1)
        speak("ScreenShot Saved, In current directory") 

    else:
        speak("Sorry, dependencies are not installed at"
        " this moment \n Please install all the modules"
        " listed in requirements.txt.")


def input_functions(function, query):
    """ 
    This function returns the input function  when called in program.

    function: Input function name. (Only string input)
    query: input of function.

    """
    function = str(function).lower()
    if function == "wiki":
        wikipedia_(query)
    
    elif function == "google_search":
        google_search(query)
    
        
    elif function == "wikipedia":
        wikipedia_(query)

    
    elif function == "how_to":
        how_todo_with_steps(query)
    
        
    elif function == "feedback":
        feedback()


# # other functions
# def feedback():
#     """ This function helps jarvis to take the feedback """
#     speak('Thank You, for helping us let me know your feedback,\n ')
#     feedback = str(listen())
#     speak('Please tell me your name also.')
#     name = str(listen())

#     with open("feedback.txt", 'a') as file:
#         data = f'\nFEEDBACK: {feedback}\nDATE: {datetime.date.today()}\nUSER: {name}'
#         data = str(data)
#         file.write(data)


if __name__ == "__main__":
    pass
