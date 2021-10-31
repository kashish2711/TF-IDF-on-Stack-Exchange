#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


data = pd.read_csv("/home/kashish_kishinchandani2/FinalDataSet.csv")


# In[ ]:


data.head()


# In[ ]:


data.dropna()


# In[ ]:


data.info()


# In[ ]:


data.drop_duplicates()


# In[ ]:


data = data.drop(["ParentId","DeletionDate"], axis=1)


# In[ ]:


data.info()


# In[ ]:


import re


# In[ ]:


data_clean = data.replace(
{'Body': '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', 
'Title': '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'}, 
{'Body': '', 'Title': ''}, regex = True)


# In[ ]:


data_clean['Body'] = data_clean['Body'].replace(r'\n|\r|\t','',regex=True)


# In[ ]:


data_clean.to_csv(r'gs://dataproc-staging-europe-west2-434500979019-mtxch6f3/google-cloud-dataproc-metainfo/ca675-assgn1/DataSet.csv', header = True, index = False)


# In[ ]:




