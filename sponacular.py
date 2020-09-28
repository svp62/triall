from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import requests
import os
import random
from os.path import join, dirname
from dotenv import load_dotenv
import json
import flask
load_dotenv()

app=flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

spoonacular_key = os.environ['SPOONACULAR_KEY']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth, wait_on_rate_limit=True)


@app.route('/')


def index():



app.run(   port=int(os.getenv('PORT',8080)),
            host=os.getenv('IP','0.0.0.0')
        )    
