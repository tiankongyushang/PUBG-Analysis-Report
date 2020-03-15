import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id ='Fi4gDecAhoiEgA',
client_secret ='cr2EjZXSD62Bn-plan2eiUmrICQ',
username ='tiankongyushang',
password ='tiankongyu',
user_agent ='web analytic')

submission = reddit.submission(url='https://www.reddit.com/r/FortNiteBR/comments/a2potr/fortnite_season_7/')

submission.comments.replace_more(limit=None) #a limit of None means that all MoreComments objects will be replaced until there are none left
for comment in submission.comments.list(): #commentForest
    print(comment.body)

    with open('Reddit Fortnite.txt','a',encoding = 'utf-8') as f:  #output, can try Pandas
        for each in comment.body:
            f.write(each)
