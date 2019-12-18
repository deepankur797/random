"""
Created on Sun Oct 04 23:10:41 2015
@author: ujjwal.karn
"""

#first, install pip by following instructions here: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows 
#then to install tweepy, go to command prompt and type: pip install tweepy
#once tweepy is installed, run the codes below:

import tweepy    #this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
 
#provide your access details below 
access_token = "72530556-lciXhI3MNNDqVWMIrMedkSJiy1KJbEExK7rmGb3Uq"
access_token_secret = "x2IHPJbxDGdnHPboxCZiFD6EKfuFlwUMDsjq8cwiDv1qe"
consumer_key = "m0c5PKS3ZkMOzRKpLRU3HfFxS"
consumer_secret = "iG7gbwFXvFnbxREMvPQwkrCwNnUPVrPZ9svZht8ChslVFJMT95"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('C:\\Users\\500038478\\PycharmProjects\\myAPP_1.0\\python.json', 'a') as f:  #change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#cricket'])

#references:
#http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#https://github.com/tweepy/tweepy
