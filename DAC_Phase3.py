#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
product=pd.read_csv("statsfinal.csv")
product


# In[2]:


product.describe()


# In[3]:


product.info()


# In[4]:


x=product.drop("S-P2",axis=1)
y=product['S-P2']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=0)
x_train


# In[5]:


x_train.shape


# In[6]:


x_test.shape


# In[7]:


y_train.shape


# In[8]:


y_test.shape


# In[9]:


y_test


# In[10]:


x_test


# In[11]:


display(product.drop_duplicates())


# In[ ]:




