import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


# twitter-credentials
access_token = "72530556-lciXhI3MNNDqVWMIrMedkSJiy1KJbEExK7rmGb3Uq"
access_token_secret = "x2IHPJbxDGdnHPboxCZiFD6EKfuFlwUMDsjq8cwiDv1qe"
consumer_key = "m0c5PKS3ZkMOzRKpLRU3HfFxS"
consumer_key_secret = "iG7gbwFXvFnbxREMvPQwkrCwNnUPVrPZ9svZht8ChslVFJMT95"

auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StdOutListner(StreamListener):
    def on_data(self, data):
        try:
            with open('C:\\Users\\500038478\\PycharmProjects\\myAPP_1.0\\twitter_data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("error on data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListner()
    stream = Stream(auth, l)
    # below line will help to filter data
    stream.filter(track=['#python', '#javascript', '#ruby'])
