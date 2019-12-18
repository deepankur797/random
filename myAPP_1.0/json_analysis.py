import json
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

tweets_data_path = 'C:\\Users\\500038478\\PycharmProjects\\myAPP_1.0\\twitter_data.json'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
#print("hi")
#print(len(tweets_data))

tweets=pd.DataFrame()
tweets['text'] = list([tweet['text'] for tweet in tweets_data])
tweets['lang'] = list([tweet['lang'] for tweet in tweets_data])
tweets['country'] = list([tweet['place']['country'] if tweet['place'] != None else None for tweet in tweets_data])
# analysis by sentiment analysis
arr=[]
for twi in tweets['text']:
    analysis=TextBlob(twi)

    if(analysis.sentiment.subjectivity>0.5):
        arr.append(analysis.sentiment.polarity)
count1=0
count2=0
count3=0
for i in arr:
    if i>=0.5:
        count1=count1+1
    elif i>-0.5 and i<0.5:
        count2=count2+1
else:
    count3=count3+1
labels = 'Happy', 'neutral', 'sad'
sizes=[count1,count2,count3]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
#Analying json by lang
tweets_by_lang = tweets['lang'].value_counts()
fig, ax =plt.subplots()
ax.tick_params(axis='x',labelsize=15)
ax.tick_params(axis='y',labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 lang',fontsize=15,fontweight='bold')
tweets_by_lang[:5].plot(ax=ax,kind='bar',color='red')
plt.show()
#analying json by country
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.show()

