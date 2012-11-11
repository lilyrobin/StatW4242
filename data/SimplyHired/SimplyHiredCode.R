require(XML)  
require(plyr)

## Read in the xml files

theCall <- "http://api.simplyhired.com/a/jobs-api/xml-v2/q- data+science /ws-100/pn-%d?pshid=46719&ssty=2&cflg=r&jbd=xz.jobamatic.com&clip=160.39.149.160" 
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

save(simply.hired.data, file = "simplyHiredJob.rda")

#https://www.jobamatic.com/a/jbb/partner-dashboard-advanced-xml-api
