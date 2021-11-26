#!/usr/bin/env python
# coding: utf-8

# In[1]:


df = pd.DataFrame({'From_To':['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
                  'FlightNumber': [10045, np.nan, 10065,np.nan, 10085],
                  'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],
                  'Airline': ['KLM(!)', '<Air France>(12)','(British Airways.)','12.Air France', "Swiss Air"]})


# In[2]:


df


# # 1.some values are missing in flight number column we need to replace those with an increase of 10 for every row

# In[3]:


df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)


# In[4]:


df


# In[5]:


tempdf = pd.DataFrame()
tempdf['From'] = df['From_To'].str.split('_').str[0].str.capitalize()
tempdf['To'] = df['From_To'].str.split('_').str[1].str.capitalize()
df.pop('From_To')
df = pd.concat([df,tempdf[['From','To']]],axis= 1)
df


# In[6]:


df


# In[7]:


delays = pd.DataFrame(df.RecentDelays.values.tolist())
delays.columns = ['delay_1', 'delay_2', 'delay_3']
df.pop('RecentDelays')
df = pd.concat([df, delays[['delay_1', 'delay_2', 'delay_3']]], axis=1)
df


# In[ ]:




