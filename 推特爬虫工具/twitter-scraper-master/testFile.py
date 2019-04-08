from twitter_scraper import get_tweets
#
# for tweet in get_tweets('kennethreitz', pages=1):
#     print(tweet['text'])
#

import markovify

tweets = '\n'.join([t['text'] for t in get_tweets('kennethreitz', pages=25)])
text_model = markovify.Text(tweets)

print(text_model.make_short_sentence(140))