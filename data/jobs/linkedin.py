import oauth2 as oauth
import httplib2
import time, os, simplejson
 
# Fill the keys and secrets you retrieved after registering your app
api_key      =   'jy0hfbp6e2bx'
secret_key  =   'kDP7wZaJuCrUPceK'
user_token           =   'ea4c862a-af29-4047-b351-c438d0934ebf'
user_secret          =   'c5cc9437-265b-4886-a16f-91b99e266ebb'
 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(api_key, secret_key)
 
# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)
 
client = oauth.Client(consumer, access_token)
 
# Make call to LinkedIn to retrieve your own profile
#resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")

#resp,content = client.request("http://api.linkedin.com/v1/jobs/1337:(id,company,posting-date)", "GET", "")


response,content = client.request("http://api.linkedin.com/v1/jobs/1337:(id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,company:(id,name),position:(title,location,job-functions,industries,job-type,experience-level),skills-and-experience,description-snippet,description,salary,job-poster:(id,first-name,last-name,headline),referral-bonus,site-job-url,location-description)?format=json", "GET", "")


print content
 
# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request(""http://api.linkedin.com/v1/people/~?format=json", "GET", {})

