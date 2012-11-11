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
#response,content = client.request("http://api.linkedin.com/v1/jobs/1337:(id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,company:(id,name),position:(title,location,job-functions,industries,job-type,experience-level),skills-and-experience,description-snippet,description,salary,job-poster:(id,first-name,last-name,headline),referral-bonus,site-job-url,location-description)?format=json", "GET", "")

request_url = "http://api.linkedin.com/v1/job-search:(jobs:(id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,expiration-timestamp,company:(id,name),position:(title,location,job-functions,industries,job-type,experience-level),skills-and-experience,description-snippet,description,salary,job-poster:(id,first-name,last-name,headline),referral-bonus,site-job-url,location-description))?format=json&job-title=Data+Scientist"

response,content = client.request(request_url, "GET", "")

content_json = json.loads(content)

total = content_json["jobs"]["_total"]

print content
 
# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request(""http://api.linkedin.com/v1/people/~?format=json", "GET", {})

