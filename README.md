Data Acquisition: 
The information for this project was supposed to be gathered from Stack Exchange. Stack Exchange is a website where people from all walks of life may ask questions and have people from all around the world answer them or contribute their ideas. Other users who view such replies rank and score these responses. The information for the stack exchange can be found here. The goal was to extract data from the top 200,000 posts based on the number of views, but the site only enables 50,000 records to be viewed/downloaded at a time. The goal of this query is to acquire the top 50,000 posts by getting the highest view count and then getting the remainder of the posts. The rest of the posts that were queried were found by referencing to the first query's last view count. Similarly, the remaining 100,000 posts were fetched by referencing to the preceding query's last view count.




Technologies Used:

DataProc on Google Cloud Platform, Microsoft Excel, Python 3, Hive and PyHive

ETL:


The first task's queries were downloaded as a CSV file. Each query had a 50,000-row limit, thus four files were downloaded. These four files were then combined using Microsoft SQL, resulting in a single CSV file that can be used in further processes to clean and load the data. The produced CSV file, which contained all 200,000 posts from Stack Exchange, was cleaned using Python Pandas Data Frame. The data was cleansed and transferred to Google Cloud DataProc.

TF-IDF:

The phrase term frequency-inverse document frequency (TF-IDF) stands for term frequency-inverse document frequency. PyHive was used to discover TF-IDF for the top 10 terms for the top 10 users across all posts. The data was loaded into a dataframe in python and several operations were performed to produce the TF-IDF using the sklearn.feature extraction.text package's TfidfVectorizer function, which allows us to conduct numerous actions on a single term. PyHive was chosen because it allows us to query your Hive database from a Python script.




