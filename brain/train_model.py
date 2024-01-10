import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from data import training_data as td
from time import sleep

# Download NLTK data (uncomment the line below if not downloaded)
# nltk.download('punkt')

def process_query_response_ml(user_query):
    # Define a dataset for training the model
    training_data = td

    # Prepare training data
    train_x, train_y = zip(*training_data)

    # Create a pipeline with a TF-IDF vectorizer and a Naive Bayes classifier
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # Train the model
    model.fit(train_x, train_y)

    # Predict the class probabilities of the user query
    predicted_classes = model.classes_
    predicted_probabilities = model.predict_proba([user_query])

    # Get the index of the class with the highest probability
    max_prob_index = predicted_probabilities.argmax()

    # Get the predicted class and its probability
    predicted_class = predicted_classes[max_prob_index]
    max_probability = predicted_probabilities[0, max_prob_index]

    ai_response = ""

    # Check if the probability of the predicted class is more than 80%
    # if max_probability > 0.10:
    if predicted_class == "identity":
        # If the predicted class is "identity", modify the AI response
        ai_response = "I'm Jarvis, a A.I voice assistant. Developed by Kartik Dixit."

    # Return a list of two elements: predicted class and modified AI response
    return [predicted_class, ai_response, max_probability]



if __name__ == '__main__':

    # Example usage:
    # user_query1 = "tell me a story"
    # ai_response1 = "..."

    # output1 = process_query_response_ml(user_query1, ai_response1)
    # print(output1)

    # user_query2 = "search harry bhai youtube"
    # ai_response2 = "..."

    # output2 = process_query_response_ml(user_query2, ai_response2)
    # print(output2)
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
                    # answer = bard_chatbot(query=query)
                    # print(f"Bard: {answer}")
                    print(process_query_response_ml(query, "..."))
                
                    history_file = open('brain\\HistoryChat.txt', 'w')
                    last_query = history_file.write(query)
                    history_file.close()

    start_chat()
