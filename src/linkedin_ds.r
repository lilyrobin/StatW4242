ds <- read.delim(file="data/jobs/linkedin_ds.tsv",
                 stringsAsFactors=FALSE,
                 quote="",
                 fill=FALSE)

head(summary(as.factor(ds$position_location_name))/nrow(ds))
head(summary(as.factor(ds$position_title)))/nrow(ds)