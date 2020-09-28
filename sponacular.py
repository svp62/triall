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