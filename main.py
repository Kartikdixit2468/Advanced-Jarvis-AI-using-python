from brain.bard_integration import bard_chatbot, start_chat
from featuers.image_detection import identify_img
from featuers.speak import speak
from featuers.jarvis_features import welcome, time, date, check_speed, take_screenshot
from featuers.jarvis_features import open_website, play_first_youtube_video
from featuers.jarvis_features import youtube_search
from brain.train_model import process_query_response_ml
# from body.speech_recognition_online import recognize_voice
from time import sleep
import webbrowser
import threading
import sys


def chat():
    """ This is the main function which starts the Jarvis when called """

    ai_categories = ['chat', 'joke', 'story', 'fact']
    answer = ""
    
    sleep(3)
    with open("body\\SpeechRecognition.txt", 'w') as file:
        file.write("")
    print("Jarvis 2.0: Started listening....")

    while True:
        # query = input("Enter your Query -: \n")


        query_file = open('body\\SpeechRecognition.txt', 'r') # path: body\SpeechRecognition.txt
        query = query_file.read()
        query = query.lower()
        query_file.close()

        query_file = open('body\\SpeechRecognition.txt', 'w') # path: body\SpeechRecognition.txt
        data_write = query.replace('jarvis', '')
        query_file.write(data_write)
        query_file.close()


        history_file = open('brain\\HistoryChat.txt', 'r')
        last_query = history_file.read()
        history_file.close()
        

        ai_res_history = open('brain\\response_hist.txt', 'r')
        res_hist = ai_res_history.read()
        ai_res_history.close()
        # print(res_hist)


        quit_list = ["exit jarvis", "jarvis quit", "bye jarvis"]
        res = process_query_response_ml(query)


        if res[0] in 'identity':
            answer = res[1]

        
        elif 'jarvis' in query.lower():
            if (query == last_query) or (query == ""):
                sleep(0.5)
                pass
            if  (query in res_hist):
                sleep(0.5)
                pass
            else:

                print(f"You : {query}")
                print("Jarvis 2.0: Thinking...")
                # answer = bard_chatbot(query=query)
                # print(f"Bard: {answer}")
                res2 = process_query_response_ml(query)

                history_file = open('brain\\HistoryChat.txt', 'w')
                last_query = history_file.write(query)
                history_file.close()

                query = (query.lower()).replace('jarvis', '')
                
                if res2[0] in ai_categories:
                    answer = bard_chatbot(query=query)
                
                else:
                    
                    if res2[0] == "date_time":
                        date()
                        time()
                    
                    elif res2[0] == "speed_check":
                        check_speed()
                    
                    elif res2[0] == "open_website":
                        answer = 'OK Sir'
                        open_website(query=query)
                    
                    elif res2[0] == "play music":
                        answer = 'Trying to play some music you like sir'
                        query = query.replace("play", '')
                        query = query.replace("listen", '')
                        query = query.replace("hear", '')
                        query = query.replace("want", '')
                        play_first_youtube_video(query)                    

                    elif res2[0] == "youtube search":
                        answer = 'Searching on youtube sir'
                        query = query.replace("search ", '')
                        query = query.replace("look up", '')
                        query = query.replace("find ", '')
                        query = query.replace("channel ", '')
                        youtube_search(query)                  

                    elif res2[0] == "screenshot":
                        take_screenshot()
                    
                    elif res2[0] == "exit":
                        answer = "Exiting sir, nice to talk you, hope you will have a great day."
                        speak(answer)
                        sys.exit()
                    
                    elif res2[0] == "image_detect":
                       img_path = input("Enter the image relative or absolute path-:\n")
                       identify_img(img_path)

                    
                    else:
                            answer = "I'm still working on it"
                            print(res2[0])
        
        if (answer) and (answer != res_hist):
            ai_res_history = open('brain\\response_hist.txt', 'w')
            ai_res_history.write(answer)
            ai_res_history.close()

            speak(answer)


if __name__ == '__main__':

    
    welcome()
    chat()
 