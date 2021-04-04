#!/usr/bin/env python
# coding: utf-8

# # <CENTER> PROGRAM-11: DATA VISUALIZATION </CENTER>

#   **REQUIREMENT:**
#               
#               With the help of suitable data and plots of your choice discuss how the data visualization can lead to misleading information.

# ## IMPORTING LIBRARIES

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## ABOUT DATASET

#            This dataset consists of data if an advertisement will be success or not.

# ## IMPORTING DATASET AND DISPLAYING IT

# In[3]:


media = pd.read_csv ('Media.csv')
actual = pd.read_csv ('Actual.csv')


# In[4]:


media.info()


# In[5]:


actual.info()


# In[6]:


media=media.drop(['money_back_guarantee'],axis = 1)
media.head(7)


# In[7]:


actual=actual.drop(['money_back_guarantee','netgain'],axis = 1)
actual.head(7)


# ## VISUALIZATION

# ### 1. RATINGS VS TARGET SEX

# In[8]:


ax = sns.barplot(x="Targeted Sex", y="ratings", palette="CMRmap",data=media).set_title('MEDIA:Ratings vs Targeted sex',weight='bold', fontsize=16)


# In[9]:


ax = sns.barplot(x="Targeted Sex", y="ratings", palette="CMRmap",data=actual).set_title('ACTUAL:Ratings vs Targeted sex',weight='bold', fontsize=16)


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset its clear that media has maniplucated the dataset. In Actual, the target sex is Male but when we compare with Media its clear that target sex is female. 

# ### 2. RATINGS vs AIRTIME

# In[10]:


ax = sns.barplot(x="Airtime", y="ratings", hue="Targeted Sex",palette="rainbow_r", data=media).set_title('Media:Airtime vs Targeted sex',weight='bold', fontsize=16)


# In[11]:


ax = sns.barplot(x="Airtime", y="ratings", hue="Targeted Sex", palette="rainbow_r",data=actual).set_title('Actual:Airtime vs Targeted sex',weight='bold', fontsize=16)


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset its clear that media has maniplucated the dataset. In Actual, the target sex and airtime anlysis is direct opposite from Media.

# ### 3. AIRTIME VS AVERAGE RUNTIME(minute_perweek)

# In[12]:


sns.catplot(x='Airtime', y='average_min_perweek', data=media, kind='boxen', aspect=2)
plt.title('Media:Airtime Vs Average runtime(minute_perweek)', weight='bold', fontsize=16)
plt.show()


# In[13]:


sns.catplot(x='Airtime', y='average_min_perweek', data=actual, kind='boxen', aspect=2)
plt.title('Actual:Airtime Vs Average runtime(minute_perweek)', weight='bold', fontsize=16)
plt.show()


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset there is no manipulcation done.

# ### 4. GENRE VS RATINGS

# In[14]:


ax = sns.barplot(x="genre", y="ratings", data=media,
                 palette="rainbow_r").set_title('MEDIA', weight='bold', fontsize=16)


# In[15]:


ax = sns.barplot(x="genre", y="ratings", data=actual,
                 palette="rainbow_r").set_title('ACTUAL', weight='bold', fontsize=16)


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset its clear that media has maniplucated the dataset. The visualization shows slight diffence in genre between Actual and Media.

# ### 5. TARGETED SEX VS EXPENSE

# In[16]:


# Media
g=sns.catplot(x="Targeted Sex", y="ratings",
                hue="expensive", col="Airtime",
                data=media, kind="bar",
                height=4, aspect=.7);


# In[17]:


# Actual
g=sns.catplot(x="Targeted Sex", y="ratings",
                hue="expensive", col="Airtime",
                data=actual, kind="bar",
                height=4, aspect=.7);


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset its clear that media has maniplucated the dataset. There is a drastic change in Expense vs targeted sex when compared between Actual and media.

# ### 6. TARGETED SEX VS RELATIONSHIP STATUS

# In[18]:


g = sns.catplot(x="Targeted Sex", y="ratings",
                hue="realtionship_status", col="Airtime",
                data=media, kind="bar",
                height=4, aspect=.7);
print("MEDIA")
g


# In[19]:


g = sns.catplot(x="Targeted Sex", y="ratings",
                hue="realtionship_status", col="Airtime",
                data=actual, kind="bar",
                height=4, aspect=.7);
print("ACTUAL")
g


# ### INFERENCE:
# 
# Compairing Media and Actual Dataset its clear that media has maniplucated the dataset. There is a drastic change in Relationship status vs targeted sex when compared between Actual and media.
