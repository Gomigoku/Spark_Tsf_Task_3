#!/usr/bin/env python
# coding: utf-8

# GOUTHAMI SUVARNA
# Task -3 Exploratory Data Analysis -Retail (Level - Beginner)
# 
# Perfroming Exploratory Data Analysis on Dataset 'Sample Superstore'

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
print('All librairies imported successfully!!')


# In[4]:


data= pd.read_csv('SampleSuperstore.csv')


# In[5]:


data


# Step : 2 #Analysis of Data 

# In[7]:


data.sample()


# In[8]:


data.head()


# In[9]:


data.tail()


# In[10]:


data.describe()


# In[11]:


data.info()


# In[12]:


data.shape


# Step:3 
# ##Checking for unique values

# In[14]:


for i in data.columns:
    print(i,len(data[i].unique()))
    


# In[17]:


#Checking for null values
data.isnull


# In[18]:


Step:4 
    ##Data visualisation
    


# In[19]:


sns.pairplot(data)


# In[24]:


data.duplicated().sum()


# In[26]:


data.drop_duplicates()


# In[27]:


data.nunique()


# In[28]:


#Deleting the column
col=['Postal Code']
new_data=data.drop(columns=col,axis=1)


# In[29]:


new_data


# In[30]:


#Correlation between variables
new_data.corr()


# In[31]:


#Covariance of columns
new_data.cov()


# In[32]:


#Loading the first five columns of data
new_data.head()


# In[34]:


#Data Visualisation
plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category',data=new_data)
plt.title('Category versus Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Category')
plt.xticks(rotation=45)
plt.show()


# In[35]:


new_data.corr()


# In[36]:


new_data.hist(bins=50,figsize=(20,15))
plt.show();


# In[37]:


new_data['State'].value_counts()


# In[39]:


plt.figure(figsize=(15,15))
sns.countplot(x=new_data['State'])
plt.xticks(rotation=90)
plt.title("STATE")
plt.show()


# In[45]:


fig, axes=plt.subplots(1,1,figsize=(12,7))
sns.heatmap(new_data.corr())
plt.show()


# In[57]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total Profit versus Sales")
sns.barplot(data =new_data.groupby('Sub-Category')['Sales','Profit'].agg(sum),x='Sales',y='Profit',ax=axes[1])
new_data.groupby('Sub-Category')['Sales','Profit'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[58]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total Sales versus Quantity")
sns.barplot(data =new_data.groupby('Sub-Category')['Sales','Quantity'].agg(sum),x='Sales',y='Quantity',ax=axes[1])
new_data.groupby('Sub-Category')['Sales','Quantity'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show()


# In[60]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
new_data.groupby('Sub-Category')['Profit','Quantity'].agg(sum).plot(kind='bar',ax=axes[0]).set_title('Qunatity and Profit relation based on Sub-Category')
new_data.groupby('Sub-Category')['Profit','Discount'].agg(sum).plot(kind='bar',ax=axes[1]).set_title('Discount and Profit relation based on Sub-Category')
plt.xticks(rotation=90)
plt.show()


# In[61]:


fig,ax= plt.subplots(1,1,figsize=(12,7))
sns.countplot(new_data['Quantity'],hue=new_data['Region'])
plt.show()


# In[63]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Distribution Plots",fontsize = 16)
sns.distplot(new_data['Sales'],ax=axes[0,0])
sns.distplot(new_data['Profit'],ax=axes[0,1])
sns.distplot(new_data['Discount'],ax=axes[1,0])
sns.distplot(new_data['Quantity'],ax=axes[1,1])
plt.show()


# In[65]:


fig,ax = plt.subplots(1,1,figsize=(12,7))
sns.countplot(new_data['Quantity'],hue=new_data['Region'])
plt.show()


# In[67]:


fig,axes = plt.subplots(2,2,figsize=(16,8))
fig.suptitle("Sales with different shipping modes and segments",fontsize=16)
sns.lineplot(new_data['Ship Mode'], new_data['Sales'],ax=axes[0,0])
sns.barplot(new_data['Ship Mode'], new_data['Sales'],ax=axes[0,1])
sns.lineplot(new_data['Segment'], new_data['Sales'],ax=axes[1,0])
sns.barplot(new_data['Segment'], new_data['Sales'],ax=axes[1,1])
plt.show()


# # Important findings
# 1.The features of profit and loss are dependent on each other.
# 2.Low quantity product are having more sales.
# 3.The mode of shipping acts as a independent variable.
# 4.The home office produces highest sales compared to the other sales domain.

# In[ ]:


Task 3 Completed!!!

