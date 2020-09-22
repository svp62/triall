## Application for fetching qoutes related to food using the Twitter API.

##### 1.  To run this app you will need your own twitter API keys. 
    
        you can claim by signing up here:  https://developer.twitter.com/en/apply/user.html
        
        After you have applied twitter will review your application and once its approved they will send you an email. Later you can sign in through the link you recieved in approval email which will ask for you app name you can name it as "project" 
        and then you can go to " keys and Tokens " bar after opening " project ". 
        
        select "view keys" in "API Key & Secret" bar and save your cosumer key and consumer seceret. Now press "generate" in "Access Token & Secret" save those access token and access token secret.
        
        now open aws cloud9 and create a file with extention .env and save your api keys by replacing "your api"  
        

    
##### 2. Clone this repository by using git clone.

##### 3. In your local copy of this repository, create a new root-level file called twiter.env

##### 4.   Add the following line in twiter.env: 

**export CONSUMER_KEY=' your keys '
export CONSUMER_SECRET=' your keys'
export ACCESS_TOKEN=' your keys '
export ACCESS_TOKEN_SECRET=' your keys '**

Save twiter.env and make sure you save it in the same directory as the project.py exist


##### 5. Run the following in your terminal:
 
```bash
sudo pip install tweepy
```
or
```bash
sudo pip3 install tweepy
```
or
```bash
pip install tweepy
```
or
```bash
pip3 install tweepy
```
    
##### 6. Install flask using the same process as above.
```bash
[sudo] pip[3] install flask
```
 
##### 7. Install python-dotenv using the same process as above.
```bash
[sudo] pip[3] install python-dotenv
```

##### 8. To run the Application 
```bash
python project.py
```

##### 9. If on Cloud9, preview templates/index.html. This should successfully render the HTML!




### TECHNICAL DIFFICULTIES WHICH I RESOLVED LATER

##### 1. To fetch tweet we need to specify date a "since date" if you put datetime.now() you will not get any response as the date will be current and there is very minimal chance of a person tweeting at the current time. so we need a date atleast 4-5 week old.

##### 2. To fetch the author of a tweet we need to use tweet.user.screen_name() as the usernames are saved under user then under screen_name so if you put tweet.user() it wont work as user() alone is an object which have other object in it and it has data.

##### 3. under the method cursor which fetch tweets we need to keep "q", "lang", "since" as it is as they are the key which matches the data we are sending in it. I changed "q" with a ramdom variable name "abcd" and it didn't fetched any data because there is no key "abcd". "q" is a key which matched the random word from the wordlist to get the relevent data.


### Acknowledgement of a problem and how to address them if you had more time.

##### 1. Sometimes the same word is choosen from word list even after having random.choices() so, the app gets same data even after refreshing. we can try .pop() but that will delete the elements from list and when all the elements are deleted no data will be fetched from twitter.
