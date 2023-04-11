import praw
import config
import subprocess
import os
import sys

def scrapeReddit():
    reddit = praw.Reddit(client_id="LeTTpiQYWxT0qxLn9p4kLA", client_secret = "7zqYcktc7onS9qalUHcfarPZyY9DKg", user_agent="macos:com.example.myredditapp:v1.2.3 (by /u/murjo06)")
    posts = []
    for subreddit in config.SUBREDDITS:
        for submission in reddit.subreddit(subreddit).hot(limit = 10):
           if(submission.is_video):
                old = sys.stdout
                sys.stdout = open(os.devnull, "w")
                process = subprocess.Popen(["youtube-dl", submission.url], cwd=os.getcwd() + os.sep + config.DOWNLOAD_PATH)
                process.wait()
                sys.stdout = old
                posts.append(f"{submission.title} @ {submission.url}")
    return posts