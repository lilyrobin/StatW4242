require(ggplot2)
require(stringr)
require(RJSONIO)

ds <- read.delim(file="data/jobs/data_scientist_title.tsv",
                 stringsAsFactors=FALSE,
                 quote="",
                 fill=FALSE)

stat <- read.delim(file="data/jobs/stat_keyword.tsv",
                   stringsAsFactors=FALSE,
                   quote="",
                   fill=FALSE)

dataScienceRegex <- ignore.case("data scien")
ds$is.ds <- str_detect(ds$description, dataScienceRegex)

table(ds$is.ds)

names(ds)
nrow(ds)

table(ds$skillsAndExperience)
head(summary(as.factor(ds$company_name)))
head(summary(as.factor(ds$position_title)))
head(summary(as.factor(ds$position_location_name))/nrow(ds))
head(summary(as.factor(ds$position_experienceLevel_name))/nrow(ds))
head(summary(as.factor(ds$jobPoster_headline)))

head(summary(as.factor(stat$position_experienceLevel_name))/nrow(stat))
head(summary(as.factor(stat$company_name)))
head(summary(as.factor(stat$position_title)))
head(summary(as.factor(stat$position_location_name))/nrow(stat))

jobFunctions.ds <- apply(as.array(ds$position_jobFunctions_values), 1, fromJSON)

jobFunctions.ds.len <- length(jobFunctions.ds)
jobFunctions.ds.result <- array(dim=100)
for(i in 1:jobFunctions.ds.len) {
  for(j in 1:length(jobFunctions.ds[[i]])) {
    jobFunctions.ds.result[[i + j - 1 ]] <- jobFunctions.ds[[i]][[j]][["name"]]
  }
}

jobFunctions.ds.df <- data.frame(table(jobFunctions.ds.result))
names(jobFunctions.ds.df) <- c("Job_Functions", "Percentage_Of_Total")
jobFunctions.ds.df$Percentage_Of_Total <- jobFunctions.ds.df$Percentage_Of_Total / length(jobFunctions.ds.result)
jobFunctions.ds.df$Career <- array(data="Data Scientist", dim=nrow(jobFunctions.ds.df))

jobFunctions.stat <- apply(as.array(stat$position_jobFunctions_values), 1, fromJSON)

jobFunctions.stat.len <- length(jobFunctions.stat)
jobFunctions.stat.result <- array(dim=100)
for(i in 1:jobFunctions.stat.len) {
  for(j in 1:length(jobFunctions.stat[[i]])) {
    jobFunctions.stat.result[[i + j - 1 ]] <- jobFunctions.stat[[i]][[j]][["name"]]
  }
}

jobFunctions.stat.df <- data.frame(table(jobFunctions.stat.result))
names(jobFunctions.stat.df) <- c("Job_Functions", "Percentage_Of_Total")
jobFunctions.stat.df$Percentage_Of_Total <- jobFunctions.stat.df$Percentage_Of_Total / length(jobFunctions.stat.result)
jobFunctions.stat.df$Career <- array(data="Statistician", dim=nrow(jobFunctions.stat.df))

jobFunctions <- rbind(jobFunctions.ds.df, jobFunctions.stat.df)
jobFunctions.sig <- jobFunctions[which(jobFunctions$Percentage_Of_Total > 0.1),]
jobFunctions.sig <- jobFunctions.sig[order(jobFunctions.sig$Percentage_Of_Total, decreasing=T),]

jobFunctions.sig$Job_Functions <- factor(jobFunctions.sig$Job_Functions,
                          levels=c("Information Technology", "Engineering", "Analyst", "Research", "Science"),
                    ordered=TRUE)

# colors from http://wiki.stdout.org/rcookbook/Graphs/Colors%20(ggplot2)/
ggplot(jobFunctions.sig, aes(x=Job_Functions, y=Percentage_Of_Total, fill=Career)) + 
  geom_bar(stat="identity", alpha=0.5, position="identity") +
  xlab("Job Functions") +
  ylab("% of Total Postings") +
  ggtitle("Data Scientist and Statistician Skills Comparison") +
  theme(legend.position="bottom", panel.background=element_rect("white"), text=element_text(size=20)) +
  scale_fill_manual(values=c("#66CC99", "#9999CC")) 
  theme_get()
