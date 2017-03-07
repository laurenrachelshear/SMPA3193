from twython import Twython
import csv

CONSUMER_KEY = '3uhYB5dlRHQQQzqdKdMimgBzv'
CONSUMER_SECRET = 'UHUikor3PZp2zSiDk7aRsjvlplhEzSHkbdHRQzsoPi1LUfDvZD'
ACCESS_TOKEN = '839152664852246532-oBYxBwtLRz30RER6lyqWjuNq1IZOOfL'
ACCESS_TOKEN_SECRET = 'mDowqjzFrj7oSWmeMxFAmj4vakYV9Ch5O3Cd3JUcRjWiM'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='Washington Capitals', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Washington Capitals', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Washington Capitals', result['text'].encode('utf-8'), url]]
        a.writerows((text))
