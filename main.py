#What you want the bot to look for NOTE: this needs to be lowercase
searchterm = 'we did it reddit'
#What subreddit you want the bot to post to
postsubreddit = ''

#Tries to load log, if no log is present it makes a new one
try:
    logr = open('log.txt', 'r')
    new = logr.read()
    logr.close()
except:
    logrf = open('log.txt', 'w')
    logrf.write('\n')
    logrf.close()


#Logs in to reddit
import praw
print('Logging in...')
reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='We Did It Reddit bot alpha(v1.5)',
                     username='')

#Defines which subreddit you want to search for comments, 'all' is all comments
subreddit = reddit.subreddit('all')
print('Searching')
#Gets a submission from the subreddit
for submission in subreddit.hot(limit=None):
    #Gets the comments from such submission
    for comment in submission.comments:
        #Makes it all lower case
        try:
            textstr = str(comment.body)
            text = textstr.decode('utf-8').lower()
        except:
            continue
        #Sees if we did it reddit is in the comment
        if searchterm in text:
            #Checks whether comment is in log
            f = open('log.txt', 'r')
            logcheck = f.read()
            f.close()
            #Converts the comment to a string
            strcomment = str(comment)
            if strcomment in logcheck:
                continue
            #If comment is not in log it writes it to the log
            g = open('log.txt', 'a')
            g.write(strcomment)
            g.close()
            
            #Gets the author of the comment
            writer = str(comment.author)
            #Gets the url of the comment. Has to build own permalink as the praw permalink is broken
            permalink = ('http://www.reddit.com/comments/%s/writtenbyenter_cool_user_here/%s' % (submission.id, comment.id))
            print(permalink)
            #Saves the title that it'll post
            title = ('We did it reddit by %s' % writer)
            #Submits the submission
            newsub = reddit.subreddit(postsubreddit)
            newsub.submit(title, permalink)
            
        
