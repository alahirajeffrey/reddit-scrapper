import praw
import pandas as pd
from dotenv import load_dotenv
import os

# load environmental varilables form .env file
load_dotenv()

# instantiate redit
reddit = praw.Reddit(
    client_id=os.environ.get('client_id'),
    client_secret=os.environ.get('client_secret'),
    user_agent=os.environ.get('user_agent'),
    username=os.environ.get('username'),
    password=os.environ.get('password')
)

keyword = input("Type keyword and press enter to search  : ")

num_entries = input("\nHow man entries would you like to save : ")

# create empty lists to hold the data
title, author, num_comments, num_upvotes, upvote_ratio = [], [], [], [], []

# append data to lists
for submission in reddit.subreddit(keyword).top(limit=int(num_entries)):
    title.append(submission.title)
    author.append(submission.author)
    num_comments.append(submission.num_comments)
    num_upvotes.append(submission.score)
    upvote_ratio.append(submission.upvote_ratio)

# save data to pandas dataframe
df = pd.DataFrame(data=list(zip(title, author, num_comments, num_upvotes, upvote_ratio)), columns=[
                  'title', 'author', 'num_comments', 'num_upvotes', 'upvote_ratio'])

# set index to start from 1
df.index += 1

# export dataframe to csv file
df.to_csv(f'{keyword}.csv', encoding='utf-8')
