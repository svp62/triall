from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import random
from dotenv import load_dotenv

load_dotenv()


import flask
import os


app=flask.Flask(__name__)



consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth, wait_on_rate_limit=True)

@app.route('/')


def index():


        Hashtags = ["#chocolates", "#icecream", "#brownies", "#cake", "#dosa", "#idlis", "#corn", "#beans", "#salad", "#soup", "#coffee", "#pumpkinspice", "#bread", "#rice", "#veggieburger", "#pasta", "#falafel"]
        
        
        
        random_word=(random.choices(Hashtags))
        tweets_from = "2020-01-11"
        
        #if you put datetime.now() you will not get any response as the date will be current and there is very minimal chance of a person tweeting at the current time.
        
        
        tweets = Cursor(auth_api.search,
                      q=random_word,
                      lang="en",
                      since=tweets_from).items(5)
                      
                      
   
        
        
        
        username=[]
        tweeting_time=[]
        tweet_content=[]
        
                      
        for tweet in tweets:
           
            
            username.append(tweet.user.screen_name)
            tweeting_time.append(tweet.created_at)
            tweet_content.append(tweet.text)
            #print("\n\n\n")
            
            
        return flask.render_template("index.html", stree=random_word[0], username=username, tweeting_time=tweeting_time, tweet_content=tweet_content, lengthh = len(tweet_content))
            
            
            
            
            
app.run(   port=int(os.getenv('PORT',8080)),
            host=os.getenv('IP','0.0.0.0')
        )    