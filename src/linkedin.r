ds <- read.delim(file="data/jobs/linkedin_ds.tsv",
                 stringsAsFactors=FALSE,
                 quote="",
                 fill=FALSE)

stat <- read.delim(file="data/jobs/linkedin_stat.tsv",
                   stringsAsFactors=FALSE,
                   quote="",
                   fill=FALSE)

names(ds)
nrow(ds)

head(summary(as.factor(ds$company_name)))
head(summary(as.factor(ds$position_title)))
head(summary(as.factor(ds$position_location_name))/nrow(ds))
head(summary(as.factor(ds$position_experienceLevel_name))/nrow(ds))
head(summary(as.factor(ds$jobPoster_headline)))

head(summary(as.factor(stat$position_experienceLevel_name))/nrow(stat))
head(summary(as.factor(stat$company_name)))
head(summary(as.factor(stat$position_title)))
head(summary(as.factor(stat$position_location_name))/nrow(stat))

