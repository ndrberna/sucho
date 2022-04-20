# SUCHO Libs


The repository contains libraries used for the SUCHO Project (Save Ucranian Cultural Heritage Online) https://www.sucho.org/ grouped in two main groups.

- Managing the output of the crawler Browsertrix
- Finding new cultural heritage candidates to crawl


## Browsetrix softare

To interact and explore the results of Browsertrix crawler 2 jupyter notebooks have been developed as:

- JSONL find duplicates.ipynb 
- WARC analysis.ipynb


## Finding new candidates to crawl

For identifying new domains to be crawled a procedure have been developed in order to analyze huge dataset of domains. 

A preliminary filtering based on data from filezones contains:

The filters (OR clause) used on the zonefiles are:

- ip_country" =="UA"
- html_country == "UA"
- domain endswith ".ua"



From each candidate it is extracted the the tag title, the lang attribuite and the page size from the homepage. Each title is passed to a translator library (Google translator) to convert from ukranian to english. 


Using a list of keywords of interest ("museum", "theatre", "church") a matching is made with the translated 
titles and with the words contained in the url.

The filters used on "title translate" - "url" are the presence of keywords from the SUCHO spreadsheet as

>"sciences","academy","gallery","archive",religi", "synagogue", "mosque", "temple", ".edu" "library","scientific","journal","education","school","institute","college" "lyceum","academy","seminary","church","cathedral","opera","music","theater","academic","culture","museum","ukraine", "art","collection","national","repository","geography","ethnographic","history","tour","virtual","cinema","national","memorial","festival","center"


If a corrispondence is found the url is selected and saved to a further step of manual investigation.


[output](test.png) 
