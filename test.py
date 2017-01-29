from __future__ import print_function

import praw

def df_print(comments,level=1):
    for comment in comments:
        print(str(level)+level*' '+' '.join(comment.body.split()).encode('utf-8').strip(), file=open("output.txt", "a"))
        if comment.replies:
            df_print(comment.replies,level+1)
            

reddit = praw.Reddit(client_id='_NB5qTsb_eQwsw',
                     client_secret='PxvvcG-piCu6jD-_jdblXcJXt4c',
                     user_agent='script for reddit')

if reddit.read_only:
    print('read only mode entered')


"""
for submission in reddit.redditor(name='driscollis').submissions.new(limit=3):
    print(submission.title)
    print(submission.id)
    print(submission.url)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        print(comment.body)
    print(len(submission.comments.list()))
    print(submission.duplicates())
    print(submission.fullname)
    print(submission.shortlink)
    print(submission)
"""

submission = reddit.submission(url='https://www.reddit.com/r/learnpython/comments/5bmaz0/python_101_book_free_for_48_hours/')
submission.comments.replace_more(limit=0)
file=open("output.txt", "w")
df_print(submission.comments)

