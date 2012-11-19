LinkedIn Job Search
===================

__Description:__

This directory contains the scripts that were used to retrieve data science related jobs from LinkedIn's api. Data science jobs are defined as the results of a keyword search for "data+science" from the job search api. The output is sorted by date posted in descending order.


__HOWTO:__

1. Sign up for a developer key with linkedin:

https://www.linkedin.com/secure/developer


2. Get the script and execute it replacing the keys with your own:

```bash

python linkedin.py 'api_key' 'secret_key' 'user_token' 'user_secret' > raw_output.json &
```

3. Transform the raw output of the api calls into a file of json objects, where each line represents a job.

```bash

python linkedin_to_tsv.py 'raw_output.json' > linkedin_jobs.tsv &
```

4. Load the data into an R dataframe.

```R

ds <- read.delim(file="data/jobs/linkedin_ds.tsv",
                 stringsAsFactors=FALSE,
                 quote="",
                 fill=FALSE)
```
