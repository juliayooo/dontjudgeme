# from bs4 import BeautifulSoup
# import requests
# import random
import praw
import json 
from credentials import CLIENT_ID
from credentials import CLIENT_SECRET 
from credentials import USERNAME
from credentials import PASSWORD    
# datapath = open("mydata2.json", "w")


reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent='bigdata2 by u/yooser_1234',
    username =USERNAME,
    password=PASSWORD,
    read_only=True
    
)

subreddit = reddit.subreddit('askphilosophy')

with open("./mydata3.txt", "w", encoding="utf-8") as datapath:
    for post in subreddit.top(limit=100):  
        print(f"Title: {post.title}")
        datapath.write(post.title + "\n")



