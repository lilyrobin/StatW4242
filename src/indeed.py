#!/usr/bin/python

import requests
from lxml import html

job_link_prefix = 'viewjob?jk='
base_url = 'http://www.indeed.com/m/'
indeed_jobs = 'http://www.indeed.com/m/jobs?q=data+scientist&start='

max_requests = 680
count_increment = 10
offset = 0

rel_link = ''

for i in range(max_requests):

  jobs = requests.get(indeed_jobs + str(offset + i * count_increment))

  jobs_xml = html.fromstring(jobs.text)

  for link in jobs_xml.iterlinks():
     rel_link = link[2]

     if rel_link.startswith(job_link_prefix):
       print base_url + rel_link
