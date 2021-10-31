#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install sasl')
get_ipython().system('pip install thrift')
get_ipython().system('pip install thrift-sasl')
get_ipython().system('pip install Pyhive')
get_ipython().system('pip install tabulate')


# In[ ]:


from pyhive import hive
from tabulate import tabulate


# In[ ]:


import pandas as pd


# In[ ]:


connect = hive.Connection(host='localhost',port=10000,username='kashish_kishinchandani2',password='5321936804810879349',database='default',auth='CUSTOM')


# In[ ]:


x = connect.cursor()


# In[ ]:


x.execute('SELECT owneruserid from top10users')


# In[ ]:


top10users = x.fetchall()


# In[ ]:


top10users


# In[ ]:


data = pd.read_sql('SELECT Distinct OWNERUSERID, BODY, TITLE FROM TOP10USERPOSTS', connect)


# In[ ]:


data.head()


# In[ ]:


data["post"] = data["title"] +" "+ data["body"]
top10_users = list(data["owneruserid"].unique())
from sklearn.feature_extraction.text import TfidfVectorizer
top10_users


# In[ ]:


def calculate_tfidf(data):
   vect = TfidfVectorizer(stop_words='english', lowercase=True) 
   reply = vect.fit_transform(data["owneruserid"])                
   df_tfidf = pd.DataFrame(reply.toarray(), columns=vect.get_feature_names())
   Total_tfidf = df_tfidf.sum(axis = 0)                    
   Top10_list = Total_tfidf.nlargest(10)                      
   Top10_words = list(Top10_list.index)                        
   df_tfidf[Top10_words]                                    
   return df_tfidf[Top10_words]


# In[ ]:


for user in top10_users:                             
   New_data = data[data['owneruserid']==user]    
   Tfidf_df = calculate_tfidf(New_data)                 
   print("For Username ID TF/IDF table : "+str(user))
   Tfidf_df.insert(0, 'owneruserid', user)                 
   display(Tfidf_df)


# In[ ]:




