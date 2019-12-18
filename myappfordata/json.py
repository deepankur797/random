import json


tweets_data_path='C:\\Users\\500038478\\PycharmProjects\\myappfordata\\twitter_data.json'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
        print("hi")
    except:
        continue

print(len(tweets_data))