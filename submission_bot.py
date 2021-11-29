import praw
import time

from praw.reddit import Subreddit

x = 0
reddit = praw.Reddit("bot4")

Subreddit = reddit.subreddit("wholesomememes").top(limit=200)
for post in Subreddit:
    try:
        print('title=', post.title)
        reddit.subreddit("jsplayground").submit(title=post.title, url=post.url )
        x += 1
    except praw.exceptions.APIException as e:
        print(e)
        print(x)
        time.sleep(3000)
        pass

print(x)