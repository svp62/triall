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
    
    Hashtags = ["cheese", "beef", "crepes", "cake", "fish", "lasagne", "ravioli", "shrimp", "bread", "meatball", "burger", "pasta", "chicken"]
    random_word=(random.choices(Hashtags))
    
    url = "https://api.spoonacular.com/recipes/search?query="+str(random_word)+"&number=1&apiKey={}".format(spoonacular_key)
    image_url = "https://api.spoonacular.com/recipes/complexSearch?query="+str(random_word[0])+"&number=1&apiKey={}".format(spoonacular_key)

    response_i = requests.get(image_url)
    json_body_i = response_i.json()
    print(json_body_i)
    image_i = (json.dumps(json_body_i["results"][0]["image"]))
    image = image_i.replace('"', '')
    
    response = requests.get(url)
    json_body = response.json()
    
    
    if json_body["totalResults"] == 0:
        print("recipes not found with {}".format(random_word[0]) )
        
    else:
        a = (json.dumps(json_body))
        
        title = (json.dumps(json_body["results"][0]["title"]))
        
        prep_time = (json.dumps(json_body["results"][0]["readyInMinutes"]))
        
        serve = (json.dumps(json_body["results"][0]["servings"]))
        
        source = (json.dumps(json_body["results"][0]["sourceUrl"]))
        
        
        print("the title is ", title)
        
        print("the prep time is ", prep_time)
        
        print("the serving size is ", serve)
        
        print("the original source is ", source)
        
        recipeID = (json.dumps(json_body["results"][0]["id"]))
        
        print("id number", recipeID)
        
        ingredients_url = "https://api.spoonacular.com/recipes/"+str(recipeID)+"/information?includeNutrition=false&apiKey={}".format(spoonacular_key)
        
        respons = requests.get(ingredients_url)
        
        json_bod = respons.json()
        
        
        b = (json.dumps(json_bod))
        
        y = json.loads(b)
        
        x = y["extendedIngredients"]
        
        print("\n\n")
        ingredients = []
        for i in x:
            ingredients.append(i["original"])



app.run(   port=int(os.getenv('PORT',8080)),
            host=os.getenv('IP','0.0.0.0')
        )    
