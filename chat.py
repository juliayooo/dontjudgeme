import random
import string
import json
import random
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import json
# nltk.download ('vader_lexicon')
# print(os.environ['CONDA_DEFAULT_ENV'])

sid = SentimentIntensityAnalyzer()

# Initialize all dicts 
statements = {}
questions = {}
statements_mild = {}
questions_mild = {}
statements_med = {}
questions_med = {}
statements_severe = {}
questions_severe = {}
fillers = {}

general_responses = {}

with open("filler.json" , "r", encoding="utf-8") as file0:
    filler = json.load(file0)
    for key, value in filler.items():
        fillers[value] = key

# open each json file and sort by severity of sentiment 

with open("statements_flat.json", "r", encoding="utf-8") as file:
    statements = json.load(file)
    for key, value in statements.items():
        if value['compound'] >= 0:
            statements_mild[key] = value
        elif value['compound'] >= -0.5:
            statements_med[key] = value
        elif value['compound'] < -0.5:
            statements_severe[key] = value

# add r/comfort statements to statements dict
with open("statements2.json", "r", encoding="utf-8") as file5:
    statements3 = json.load(file5)
    for object in statements3:
        for key, value in object.items():
            # print(key, value)
            if value['compound'] >= 0:
                statements_mild[key] = value
            elif value['compound'] >= -0.5:
                statements_med[key] = value
            elif value['compound'] < -0.5:
                statements_severe[key] = value


# open each json file and sort by severity of sentiment 

with open("questions.json", "r", encoding="utf-8") as file2:
    questions = json.load(file2)
    for key, value in questions.items():
            if value['compound'] >= 0:
                questions_mild[key] = value
            elif value['compound'] >= -0.5:
                questions_med[key] = value
            elif value['compound'] < -0.5:
              questions_severe[key] = value

# open questions2 and add to big questons dict 
with open("questions2.json", "r", encoding="utf-8") as file3:
    questions3 = json.load(file3)
    for object in questions3:
        for key, value in object.items():
            # print(key, value)
            if value['compound'] >= 0:
                questions_mild[key] = value
            elif value['compound'] >= -0.5:
                questions_med[key] = value
            elif value['compound'] < -0.5:
                questions_severe[key] = value


with open("general.json", "r", encoding="utf-8") as file4:
    general_responses = json.load(file4)

# main function to interact with the user
def interact():
    current_resp = ""
    counter = 0
    chat = True
    avg_sent = 0.0
    print("Hi there!! What's your name?")
    name = input()
    print(f"Hi {name}, I'm the saddest chatbot. I come with some instructions. For example, if you wanna stop talking just say bye . also, I can be kinda sensitive just letting u know, don't worry about me. I am just looking for a friend. How are you doing though?")
    response = input().lower()
    print("sorry do you mind if I just dump on you real quick?")
    while chat:
    # while response is not bye, run the chat bot while accounting for length of conversation
        response = input().lower()
        if response.lower() == "bye":
            print("Okay, bye. I hope this wasn't the worst conversation you've ever had. I'm sorry if it was. I tend to do that. I will just leave. I hope you have a better day than me.")
            chat = False
            break
        counter += 1
        current_resp = respond(counter, response, chat, avg_sent, current_resp)
        print(current_resp, '\n')
    
     # handle responses 
def respond(counter, response, chat, avg_sent, current_resp):


    get_sent(avg_sent, response, counter, current_resp)
    #  based on chat length, respond with different severity, handling questions and statements differently
    for key in general_responses.keys():
        if key in response:
            return general_responses[key]
    if counter % 3 == 0:
            return random.choice(list(fillers.keys()))
    if counter < 8 or avg_sent >= 0.5:
        if "?" in response:
            return random.choice(list(questions_mild.keys()))
        else:
            return random.choice(list(statements_mild.keys()))
    elif (counter >= 8 and counter < 20) or (avg_sent < 0.5 and avg_sent >= -0.2):
        if "?" in response:
            return random.choice(list(questions_med.keys()))
        else:
            return random.choice(list(statements_med.keys()))
    if counter == 20:
        return("Wow, we have already exchanged 20 messages together. I  feel like we are really close now. Can I tell you something really personal?")
    elif counter > 20 or avg_sent < -0.2:   
        if "?" in response:
            return random.choice(list(statements_severe.keys()))
        else:
            return random.choice(list(questions_severe.keys()))
    

def get_sent(avg_sent, response, counter, current_resp):
    if response == "same" or "too" in response:
        sentiment_scores = sid.polarity_scores(current_resp)
    else:
        sentiment_scores = sid.polarity_scores(response)
    # average the user sentiment based on new response and previous average using number of responses for mean
    # print (avg_sent + sentiment_scores['compound'] / counter)
    return ( (avg_sent + sentiment_scores['compound']) / counter)

interact()