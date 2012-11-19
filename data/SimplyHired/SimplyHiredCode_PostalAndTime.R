require(XML)  
require(plyr)

## Read in the xml files from simplyhired

theCall <- "http://api.simplyhired.com/a/jobs-api/xml-v2/q- data+science /ws-100/pn-%d?pshid=46719&ssty=2&cflg=r&jbd=XiaokunAngela.jobamatic.com&clip=160.39.149.160" 
                                                                                    ## Put your own pshid, ssty, cflg, jbd and clip at here
i <- 1
while(TRUE){
    xml_names <- sprintf(theCall, i)
    xml.list <- xmlToList(xml_names, addAttributes = T, simplify = T)  
    if(is.matrix(xml.list) && is.null(unlist(xml.list[1:4,1]))){
        break
    }

    xml.df <- ldply(xml.list[-1], data.frame)  #Drop the first column which demonstrate the parameters for your calling
    xml.df <- xml.df[, -1]  

    if(i == 1){
        simply.hired.data <- xml.df
    }else{
        simply.hired.data <- cbind(simply.hired.data, xml.df)
    }
    
    i <- i + 1
}

row.names(simply.hired.data) <- c("Job.Title", "Company.Name", "Source",
                       "Job.Type", "Location", "last.Seen.Date", "first.Posted.Date", "Job.Description")

save(simply.hired.data, file = "simplyHiredJob.rda")  #This is the original data

require(stringr)
Location <- simply.hired.data[5, ]
PostedDate <- simply.hired.data[7, ]
PostedDate <- str_extract(unlist(PostedDate),"2\\d{3}-\\d{2}-\\d{2}")
PostedDate <- as.Date(PostedDate, format="%Y-%m-%d")  #Posted date

City <- vector("character", 683)
State <- vector("character", 683)
Postal <- vector("numeric", 683)
PostedDate <- vector("character", 683)
for(i in 1:683){
    City[i] <- Location[1, i]$loc$.attrs[1]
    State[i] <- Location[1, i]$loc$.attrs[2]
    Postal[i] <- as.numeric(Location[1, i]$loc$.attrs[3])
}

SHD <- data.frame(City, State, Postal,PostedDate)
SHD <- address[!is.na(Postal), ]  #drop date that has no postal numbers

save(SHD, file = "simplyHiredJob_PostalAndPostedTime.rda")  #This is the original data
write.csv(SHD, "data.csv")


