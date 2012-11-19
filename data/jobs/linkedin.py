import oauth2 as oauth
import httplib2
import time, os, sys
import simplejson as json
 
# Fill the keys and secrets you retrieved after registering your app
api_key = sys.argv[1]
secret_key = sys.argv[2]
user_token = sys.argv[3]
user_secret = sys.argv[4]
 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(api_key, secret_key)
 
# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)
 
client = oauth.Client(consumer, access_token)
 
# Make call to LinkedIn

max_requests = 240 
count_increment = 20

request_url = "http://api.linkedin.com/v1/job-search:(jobs:(id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,expiration-timestamp,company:(id,name),position:(title,location,job-functions,industries,job-type,experience-level),skills-and-experience,description,salary,job-poster:(id,first-name,last-name,headline),referral-bonus,site-job-url,location-description))?format=json&count=20&keywords=quantitative&sort=DD&start="

for i in range(max_requests):
  response,content = client.request(request_url + str(i * count_increment), "GET", "")
  print content.replace("\n", " ")
