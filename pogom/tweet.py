import tweepy
import logging
import os
from datetime import datetime
from datetime import timedelta
from base64 import b64encode
import ConfigParser

from . import config

Config = ConfigParser.ConfigParser()
Config.read(os.path.join(os.path.dirname(__file__), '../config/twitter_config.ini'))
log = logging.getLogger(__name__)

#auth = tweepy.OAuthHandler(getConsumerKey(), getConsumerSecret())
#auth.set_access_token(getAccessToken(), getAccessSecret())
consumerKey = Config.get('Twitter_API', 'consumerKey')
consumerSecret = Config.get('Twitter_API', 'consumerSecret')
aToken = Config.get('Twitter_API', 'aToken')
aSecret = Config.get('Twitter_API', 'aSecret')
log.info('Twitter API Params geladen.')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(aToken, aSecret)
bot=tweepy.API(auth)

def sendTweet(tweet):
        try:
            bot.update_status(tweet)
            log.info('Tweet versendet.')
        except tweepy.TweepError as error:
            log.error(error.message[0]['message'])





