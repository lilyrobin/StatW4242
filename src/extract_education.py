from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
import itertools
import pandas as pa
import string

df = pa.read_csv('../data/kaggle_profiles.tsv', sep='\t')
#print df['education']

df['education'] = df['education'].fillna('')

df['ed_sentences'] =  df['education'].apply(sent_tokenize)
#print df['ed_sentences']
df['ed_words'] = df['ed_sentences'].apply(lambda x: list(itertools.chain.from_iterable([word_tokenize(s) for s in x])))
#print df['ed_words']

vectorizer = CountVectorizer(binary = True)

f = vectorizer.fit_transform(df['ed_words'].apply(str))
w = pa.DataFrame(f.todense(), columns = vectorizer.get_feature_names())

for c in w.columns:
    print string.join([str(c), str(w[c].mean()), str(w[c].sum())], '\t')
