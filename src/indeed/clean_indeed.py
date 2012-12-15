#!/usr/bin/python

import os
from lxml import html

prefix = 'viewjob?jk='

fields = ['title','company','city','state','zip_code','date','desc']

# Print header
print "\t".join(fields)


def by_class(html, class_name):
  return html.find_class(class_name)[0].text_content().replace("\n", " ").replace("\t", " ")

def by_xpath(html, path):
  return html.xpath(path)[0].text_content().replace("\n", " ").replace("\t", " ")

def by_id(html, id_name):
  return html.get_element_by_id(id_name).text_content().replace("\n", " ").replace("\t", " ")

def uni(input):
  r = ''
  try:
    r = unicode(input).encode('ascii', 'ignore')
  except Exception, e:
    raise e
  return r


def clean(input_filename, f):
  """Used to clean the html output from Indeed"""
  r = ["NA"] * len(f)
  job = html.fromstring(file(input_filename).read())
  # Title
  r[0] = by_xpath(job, '/html/body/p[1]/b/font')
  # Company
  r[1] = by_class(job, 'source')
  # Location
  l = by_class(job, 'location').split(',')
  # City
  r[2] = l[0].strip()
  # State
  try:
    l1 = l[1].strip().split(' ')
    r[3] = l1[0].strip()
  # Zip Code
    r[4] = l1[1].strip()
  except Exception, e:
    pass
  # Date
  r[5] = by_class(job, 'date')
  # Description
  r[6] = by_id(job, 'desc')
  return "\t".join(map(uni, r))



files = os.listdir('./')

for filename in files:
   if filename.startswith(prefix):
    print clean(filename, fields)
