# Here we have integrated our chatbot with bard 
import sys
import json
import bardapi 
import datetime
import keyboard
import pyperclip
import pyautogui
import webbrowser
from time import sleep

# bard_cookies = {
#     "__Secure-1PSID": "dQg97B-r2usmXaeXhyxf7KhhjtREGxCb9BtiHaiGHsClHkMMFTZX4zxQzjJgqawmnjnZdA.",
#     "__Secure-1PSIDTS": "sidts-CjEBNiGH7iSaYx-9JVKjHzYenvcgvk4VVSu2uwwYzIJue7YmLQYQLfmvLRG1HkP9cALyEAA",
#     "__Secure-1PSIDCC": "ACA-OxMGpI9IyHfoFnxiULpdjloJm2AHKiXQ_50HXO-oMpzkYJdxJlY_WU0bnas3QXYt9Ta_8w"
# }


def CookieScrapper():
    webbrowser.open("https://bard.google.com")
    sleep(2.5)
    pyautogui.click(x=1695, y=85)
    sleep(1)
    pyautogui.click(x=1410, y=117)
    sleep(1)
    keyboard.press_and_release('ctrl + w')

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue ,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }

    return cookie_dict

bard_cookies = CookieScrapper()


def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

def bard_chatbot(query):
    """ 
    This function takes query as a input and return response from Google Bard. 
    query: {Your Quey};
    .
    It uses bard API to take your query to bard and return response in the form of String <str> 
    """
    
    bard = bardapi.BardCookies(cookie_dict=bard_cookies)
    response = bard.get_answer(query)
    answer = response['content']

    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "brain\\data\\" + filenamedate
    if len(answer) > 500: 
        final_answer = split_and_save_paragraphs(answer, filename=filenamedate)
    else:
        split_and_save_paragraphs(answer, filename=filenamedate)
        return answer


    return final_answer


def start_chat():
        
        while True:
            # query = input("Enter your Query -: \n")
            
            query_file = open('body\\SpeechRecognition.txt', 'r')
            query = query_file.read()
            query_file.close()

            history_file = open('brain\\HistoryChat.txt', 'r')
            last_query = history_file.read()
            history_file.close()
            
            quit_list = ["exit", "quit", "bye"]
            
            if 'jarvis' in query.lower():
                if query.lower() in quit_list:
                    print("Bye... :)")
                    break
                    sys.exit()
                else:
                    if (query == last_query) or (query == ""):
                        sleep(0.5)
                        pass
                    else:
                        print(f"You : {query}")
                        answer = bard_chatbot(query=query)
                        print(f"Bard: {answer}")
                    
                        history_file = open('brain\\HistoryChat.txt', 'w')
                        history_file.write(query)
                        history_file.close()
                        
                        ai_res_history = open('brain\\response_hist.txt', 'w')
                        ai_res_history.write(answer)
                        ai_res_history.close()


if __name__ == '__main__':

    start_chat()
