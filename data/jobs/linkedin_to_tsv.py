#!/usr/bin/python

import types
import re
import simplejson as json
import sys

fields = (
  ('id',),
  ('customerJobCode',),
  ('active',),
  ('postingDate','year'),
  ('postingDate','month'),
  ('postingDate','day'),
  ('expirationDate','year'),
  ('expirationDate','month'),
  ('expirationDate','day'),
  ('postingTimestamp',),
  ('expirationTimestamp',),
  ('company','id'),
  ('company','name'),
  ('position','title'),
  ('position','location','country','code'),
  ('position','location','name'),
  ('position','jobFunctions','values'),
  ('position','industries','values'),
  ('position','jobType','code'),
  ('position','jobType','name'),
  ('position','experienceLevel','code'),
  ('position','experienceLevel','name'),
  ('skillsAndExperience',),
  ('descriptionSnippet',),
  ('description',),
  ('salary',),
  ('jobPoster','id'),
  ('jobPoster','firstName'),
  ('jobPoster','lastName'),
  ('jobPoster','headline'),
  ('referralBonus',),
  ('siteJobUrl',),
  ('locationDescription',)
)

filename = sys.argv[1]
null_value = "NA"
r = [null_value] * len(fields)
blank_literal = re.compile('[\t\r\n]')
ascii_chars = re.compile('[ -~]') 
parsed_line = json.loads('{}')
i = 0

def nested_get(obj, key):
  """Get up to 5-nested values by name"""
  if type(key) is not types.TupleType:
    raise Exception("The key object must be a tuple")

  l = len(key)

  if l == 1:
    return obj[key[0]]
  elif l == 2:
    return obj[key[0]][key[1]]
  elif l == 3:
    return obj[key[0]][key[1]][key[2]]
  elif l == 4:
    return obj[key[0]][key[1]][key[2]][key[3]]
  elif l == 5:
    return obj[key[0]][key[1]][key[2]][key[3]][key[4]]

  # Ensure that the key is not nested more than five times
  elif l > 5:
    raise Exception("Objects nested more than five times are not supported")

  # Ensure that the key has a length greater than zero
  elif l == 0:
    raise Exception("Key has a length of zero")
  else:
    raise Exception("Key is less than length of zero")

def print_json(item):
  """Special printing rules JSON to TSV"""

  result = ''
  if type(item) is types.ListType or type(item) is types.DictType:
    result = json.dumps(item)
  else:
    result = "".join(re.findall(ascii_chars, unicode(item)))
  # Remove newlines and tabs
  return blank_literal.sub(' ', result)

def print_header(field):
  """Special printing rules for the header"""
  l = len(field)

  if l > 1:
    return "_".join(field)
  else:
    return field[0]

print("\t".join(map(print_header,fields)))

for line in file(filename):
  i = 0
  r = [null_value] * len(fields)

  parsed_line = json.loads(line)

  for field in fields:
    try:
      r[i] = nested_get(parsed_line, field)
    except KeyError:
      pass
    i = i + 1

  print("\t".join(map(print_json,r)))  
