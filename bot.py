import praw

print "Hello Reddit"

reddit = praw.Reddit('myBot')

subreddit = reddit.subreddit("DenverBroncos")

print "Subreddit: %s" % subreddit.display_name
print "Title: %s" % subreddit.title
#print "Description: %s" % subreddit.description

print "Hot Posts:"

for submission in subreddit.hot(limit=1):
    print "   %s (%d)" % (submission.title, submission.score)

    top_level_comments = list(submission.comments)
    print "   Top-level comments:"
    for comment in top_level_comments:
        print "      %s" % comment

    all_comments = submission.comments.list()
    print "   All comments:"
    for comment in all_comments:
        print "      %s" % comment

