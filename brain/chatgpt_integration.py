# Here we have integrated our chatbot with ChatGBT 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings

warnings.simplefilter("ignore")

link_to_gpt4 = "https://chatgbt.one/"

chrome_driver_path = 'brain\chromedriver.exe'
chrome_options = Options()
chrome_options.headless = False
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
# chrome_options.add_argument('--headless')
chrome_options.add_argument('executable_path=' + chrome_driver_path)  # Pass executable_path here

driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()
driver.get(link_to_gpt4)


def FileReader():
    File = open("brain\\Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("brain\\Chatnumber.txt","w")
    File.write(Data)
    File.close()


def ChatGPT_chatbot(Query):

    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div/main/article/div/div[1]/section[3]/div/div/div/div/div/div/div/div[3]/input").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div/main/article/div/div[1]/section[3]/div/div/div/div/div/div/div/div[3]/span[2]").click()
    Data = str(FileReader())

    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/div/main/article/div/div[1]/section[3]/div/div/div/div/div/div/div/div[2]/ul/li[3]/p/span"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/div/main/article/div/div[1]/section[3]/div/div/div/div/div/div/div/div[2]/ul/li[3]/p/span"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

print("Starting The GPT4-Model.")
FileWriter(Data='3')

while True:
        
    try:
        Query = input("Enter Your Query : ")
        print(ChatGPT_chatbot(Query=Query))
    
    except:
        print("An Unknown Error occured")

