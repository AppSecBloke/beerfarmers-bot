import os
import random
import tweepy

consumer_key = (os.environ['consumer_key'])
consumer_secret = (os.environ['consumer_secret'])
access_token = (os.environ['access_token'])
access_token_secret = (os.environ['access_token_secret'])
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  



def rline (filename):
	with open(filename) as f:
		lines = f.readlines()
		random_int = random.randint(0,len(lines)-1)
		b = lines[random_int]
		v = b.strip()
		return v
    	
    	
twit = rline ("users.txt")
malware = rline("malware.txt")
C = rline("countries.txt")
noun = rline("nouns.txt")
animal = rline("animals.txt")

msg = "."+twit+" is accused of creating "+malware+" & working as a proxy of "+C+" APT group known as "+noun+" "+animal+" "
print (msg)
api.update_status(status=msg)
