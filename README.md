Data Acquisition: 
The data gathering part of this assignment was supposed to be extracted from Stack Exchange. Stack Exchange is a place where people can ask questions from any background and the people across the internet answer the questions or share their thoughts. These answers are then ranked/scored by other users visiting such answers. The data for the stack exchange is available here. The target was to retrieve the data of the top 200,000 posts based on the view count, but the site allows only 50,000 records at once to be viewed/downloaded. The motive behind this query is to achieve the top 50,000 posts and is achieved by getting the max of view count and getting the rest of the posts. The rest of the posts which were queried was achieved by referring the last view count from the first query. Similarly, the rest 100,000 posts were retrieved by referring the last view count from the previous query.




Technologies Used:

DataProc on Google Cloud Platform, Microsoft Excel, Python 3, Hive and PyHive

ETL:


The queries which were executed in the first task were downloaded in the form of CSV. Since, each query had a limit of 50,000 rows, 4 files were downloaded. These 4 files were then transformed into one using Microsoft SQL and one CSV file was created, which can be used in further steps to clean and eventually load the data. The CSV file which was compiled and which had all the 200,000 posts from stack exchange was then cleaned using Python Pandas Data Frame. The cleaned data was moved to the Google Cloud DataProc. Hive was used to create tables and load the data. Since, while loading the data SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' was used, a view was also created to ensure the datatypes are changed for the needed columns.

TF-IDF:

TF-IDF stands for term frequency-inverse document frequency. TF-IDF was found out using PyHive for the top 10 words for the top 10 users from all the posts. A hive connection was established via python to load the data into a dataframe in python and performing various tasks to achieve the TF-IDF. sklearn.feature_extraction.text package has a function called TfidfVectorizer which allows us to perform various actions on a specific keyword. PyHive was used as it allows us to query your hive database from python




