import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import json
nltk.download ('vader_lexicon')
print(os.environ['CONDA_DEFAULT_ENV'])


# from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
# text = "I hate you!!"
# sentiment_scores = sid.polarity_scores(text)
# print(sentiment_scores)


# uncomment to use file 
# filename = "mydata3.txt"
# scores_dict = {}
# question_dict = {}

with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        if not line or line.strip() == "":
            continue
        sentiment_scores = sid.polarity_scores(line.strip())
        scores_dict[line] = sentiment_scores

sorted_scores = dict(sorted(scores_dict.items(), key=lambda item: item[1]['neg'], reverse=True))
# print("\nSorted by negative sentiment:")
# for line, scores in sorted_scores.items():
#     print(f"'{line.strip()}': {scores}")




questions_to_extract = []

for itm in sorted_scores.items():
    if '?' in itm[0]:
        
        question_dict[itm[0]] = itm[1]
        questions_to_extract.append(itm[0])
        # print(f"Question: {itm[0].strip()} - Sentiment: {itm[1]}")


# Now remove those from the original dictionary
for key in questions_to_extract:
    sorted_scores.pop(key)

with open('questions2.json', 'w', encoding='utf-8') as qfile:
    for question, sentiment in question_dict.items():
    
            json.dump({question: sentiment}, qfile, indent=4, sort_keys=False)

with open('statements3.json', 'w', encoding='utf-8') as sfile:

    for statement, sentiment in sorted_scores.items():
        json.dump({statement: sentiment}, sfile, indent=4, sort_keys=False)


# for itm in sorted_scores.items():
#     # print(itm, itm[0])
#     if '?' in itm[0]:
#         question_dict[0] = itm[1]
#         sorted_scores.pop(itm[0])
#         print(f"Question: {itm[0].strip()} - Sentiment: {itm[1]}")


# for text in sentiment_texts:
#     sentiment_scores = sid.polarity_scores(text)
#     print(f"The statement '{text}' has sentiment scores: {sentiment_scores}")