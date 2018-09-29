import praw
import config

# reddit authentication
reddit = praw.Reddit(username=config.username,
                     password=config.password,
                     client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)

lookingFor = "[GPU]"

subreddit = reddit.subreddit('buildapcsales')                     
for submission in subreddit.stream.submissions():
    if submission.title.startswith(lookingFor):
        print(submission.title)
        reddit.redditor(config.message_to).message(lookingFor, submission.title)