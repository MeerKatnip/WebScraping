# WebScraping 101

Exercise 1:
Accessed coreyms.com, extracted out headline, summary, and youtube link. Youtube link is the video ID extracted from the embedded video and inserted into a new link to directly access each video. Added try/except block for when videos are no available, set variable as None. Exported scraped content as .csv file.

Followed tutorial here: https://www.youtube.com/watch?v=ng2o98k983k

Exercise 2:

Accessed forecast.weather.gov, located div class 'tombstone-container', extracted elements for classes 'period-name', 'short-desc', and 'temp. Created new variable for array of element items extracted from each class. Printing data with pandas in a table format.

Followed tutorial here: https://www.youtube.com/watch?v=E5cSNSeBhjw