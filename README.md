# DJM 

A chabot program written in Python and Javascript, with data from Reddit and NLTK Sentiment Analysis plugin 

https://github.com/juliayooo/dontjudgeme

Anne Anlin Cheng, in her review of ‘Ghost in the Shell’ (2017), writes that “Freud told us that the most unsettling effects for human ontology is to be confronted by a machine that comes to life… What happens to the human element when the brain gets reduced to a series of electrical impulses, and, conversely, along a more sentimental line, can machines have feelings, too?” (Cheng, 129). I am constantly fascinated by the idea of the “ghost in the machine”, the empathy we project upon tech, and the things that make us sentient.

I was heavily inspired by Joseph Weizenbaum’s Eliza, considered to be the first ever chatbot, communicating using keywords, patterns and substitutions, long before the existence of Language Learning Models. I decided to take these ideas and create the saddest chatbot in the world. I was interested in seeing the lengths and limits of fabricating a smooth conversationalist without using a complete LLM. I also wanted to incorporate more contemporary ideas and methods into the creation. 



# first_crawl.py
This file contains the functions used to scrape reddit for top posts, from 3 different subreddits. 

# parse.py
This file contains the code necessary to parse the JSON data from the web crawl and censor curse words/slurs, and change the positionality of the statements and questions to work optimally for one on one conversation. 

# sentiment.py
This file takes JSON data and uses the NLTK plugin to assign a negative, compound and positive sentiment score, which is then added to the JSON. 

# chat.py 
This is the main program. To beign, the program loads all data, and separates questions, statements and filler into mild, medium and severe categories based on their sentiment score. 
Then, the interact() loop starts the chat process, calling respond() after each interaction until the program is quit or 'bye' is entered. 
respond() uses the functon get_sent() which returns the calculation of the average sentiment of the user's responses to match user's tone. Then, based on that sentiment score, or conversation lenghth, an appropriately severe question or statement is proposed. Every third response, the bot returns a filler statement (from filler.json) to aid conversation flow, and responses containing keywords are responded to with statements attached to each keyword (in general.json)

My chatbot responds with 200+ responses scraped from r/depression, r/comfort and r/askphilosophy. Reddit is the most vulnerable place on earth (lol), where (presumably) real people post their deepest thoughts behind anonymous avatars. With some parsing, these posts become the language of this chatbot: an incredibly hopeless, depressed and nihilistic personality. Sentiment analysis is run on all preloaded responses as well as user input, in order to match the user’s feelings, but ultimately devolve into a severely devastating conversation as the conversation lengthens. With additional filler and keyword responses, the chatbot takes shape. 

All the data used for this project is publicly available and not attached to names. DJM explores our empathetic yet authoritarian relationships to technology, our online behaviours, as well as the refuge we find within technology. How do our treatments of currently non-agentic tech symbiotically contribute to our treatment of the world’s most vulnerable?

