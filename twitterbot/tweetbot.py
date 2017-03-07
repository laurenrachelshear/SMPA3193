from twython import Twython, TwythonError

CONSUMER_KEY = '3uhYB5dlRHQQQzqdKdMimgBzv'
CONSUMER_SECRET = 'UHUikor3PZp2zSiDk7aRsjvlplhEzSHkbdHRQzsoPi1LUfDvZD'
ACCESS_TOKEN = '839152664852246532-oBYxBwtLRz30RER6lyqWjuNq1IZOOfL'
ACCESS_TOKEN_SECRET = 'mDowqjzFrj7oSWmeMxFAmj4vakYV9Ch5O3Cd3JUcRjWiM'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv
