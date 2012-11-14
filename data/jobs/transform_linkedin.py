#!/usr/bin/python

import simplejson as json
import sys

filename = sys.argv[1]

jobs = []

for line in file(filename):
  try:
    jobs = json.loads(line)["jobs"]["values"]
  except KeyError:
    pass

  for job in jobs:
    print json.dumps(job)
