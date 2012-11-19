#  Copyright (c) 2012, Adam Obeng
#  All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#      * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#      * Neither the name of the <organization> nor the
#        names of its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL Adam Obeng BE LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import urllib2
import pickle
import string
from BeautifulSoup import BeautifulSoup
import pandas as pa
import re

num_pages = 30 # Change this to fetch more pages
pages = []

for n in range(1, num_pages + 1):
    url = 'http://www.kaggle.com/users?page=%s' % n
    print url
    pages.append({'url': url,
        'page': urllib2.urlopen(url).read()})

pickle.dump(pages, open('pages.pickle', 'w'))
#pages = pickle.load(open('pages.pickle'))

profile_urls = []
for p in pages:
    soup = BeautifulSoup(p['page'])
    for l in  soup.findAll('a', 'profilelink'):
        profile_urls.append(l['href'])

pickle.dump(profile_urls, open('profile_urls.pickle', 'w'))
#profile_urls = pickle.load(open('profile_urls.pickle'))


profile_pages = []
for i, u in enumerate(profile_urls):
    url = 'http://www.kaggle.com%s' % u
    print i, len(profile_urls), url
    profile_pages.append({'url': url,
        'page': urllib2.urlopen(url).read()})
    if (i%100) == 0: pickle.dump(profile_pages, open('profile_pages.pickle', 'w'))
pickle.dump(profile_pages, open('profile_pages.pickle', 'w'))
#profile_pages = pickle.load(open('profile_pages.pickle'))

profiles = []
for i, p in enumerate(profile_pages):
    print i, len(profile_pages), p['url']
    soup = BeautifulSoup(p['page'])
    profile = soup.find('div', 'profile-inside')
    profile = dict(zip(map(lambda x: string.lower(x.text), profile.findAll('dt')), map(lambda x: x.text, profile.findAll('dd'))))

    profile['url'] = p['url']

    profiles.append(profile)
    if (i%100) == 0: pickle.dump(profiles, open('profiles.pickle', 'w'))
pickle.dump(profiles, open('profiles.pickle', 'w'))
#profiles = pickle.load(open('profiles.pickle'))

for p in profiles:
    for k, v in p.iteritems():
        # http://stackoverflow.com/questions/1342000/how-to-replace-non-ascii-characters-in-string
        p[k] = string.join([i for i in v if ord(i)<128], '')
    
df =  pa.DataFrame(profiles)
df.to_csv('kaggle_profiles.tsv', sep = '\t')
