import praw
import pushbullet
import config

#pushbullet authentication
pb = pushbullet.Pushbullet(config.pushbulletAuth)

#reddit authentication
reddit = praw.Reddit(client_id=config.redditID,
                     client_secret=config.redditSecretKey,
                     user_agent='bot')

subreddit = reddit.subreddit('buildapcsales')                     
for submission in subreddit.stream.submissions():
    if submission.title.startswith("[GPU]"):
        print(submission.title)
        pb.push_note("",submission.title)

