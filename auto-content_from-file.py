#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import requests
 
content_file = 'content.txt'	# content file where tweets are separated by "\n"
sleep_time = 300	# time between tweets
 
# Twitter account secrets and tokens
CONSUMER_KEY = 'consumer_key'	#keep the quotes, replace this with consumer key
CONSUMER_SECRET = 'consumer_secret'	#keep the quotes, replace this with consumer secret key
ACCESS_KEY = 'access_key'	#keep the quotes, replace this with access token
ACCESS_SECRET = 'access_secret'	#keep the quotes, replace this with token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(content_file,'r')
f=filename.readlines()
filename.close()

for line in f:
	if 'http://' in line:		# check if you're sharing a URL
		message = line.split("http://")[0]
		url = line.split("http://")[1]
		requests = requests.get(url, stream=True)
		api.update_status(status = (message + requests))
	else:		# if no URL, update status with text
		api.update_status(line)
    time.sleep(sleep_time)	    # Tweet every 15 minutes

