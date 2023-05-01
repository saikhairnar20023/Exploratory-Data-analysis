#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv("iris.csv")


# In[6]:


df


# In[9]:


df.shape


# In[11]:


df.columns


# In[15]:


df['Species'].value_counts()


# # 2D Scatter Plot

# In[20]:


df.plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm')
plt.show()


# In[25]:


sns.set_style('whitegrid');
sns.FacetGrid(df,hue='Species',height=4)    .map(plt.scatter,'SepalLengthCm','SepalWidthCm')    .add_legend();
plt.show()


# In[27]:


sns.set_style('whitegrid');
sns.FacetGrid(df,hue='Species',height=4)    .map(plt.scatter,'PetalLengthCm','PetalWidthCm')    .add_legend();
plt.show();


# # pairplot

# In[30]:


sns.set_style('whitegrid');
sns.pairplot(df,hue='Species',height=3);
plt.show()

