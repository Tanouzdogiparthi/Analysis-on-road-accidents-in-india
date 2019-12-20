#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import matplotlib.pyplot as plt


# In[95]:


state_month=pd.read_csv('only_road_accidents_data_month2.csv')
state_time=pd.read_csv('only_road_accidents_data3.csv')


# In[96]:


display(state_month)


# In[97]:


# it is used to return top 5 rows of a dataset
state_time.head()


# In[98]:


#here ".unique()" is used to return the same item in selected column for a data set
state_names=state_month['STATE/UT'].unique()
print(state_names)


# In[99]:


#replace function is used to replace the value of an item with other value given
state_month['STATE/UT']=state_month['STATE/UT'].replace({'Delhi (Ut)':'Delhi Ut', 'D & N Haveli':'D&N Haveli'})
print(state_month['STATE/UT'].unique())


# In[100]:


state_names=state_month['STATE/UT'].unique()
print(state_names)


# In[101]:


#axis=1 represents columns and here it creates new column in dataset 
state_month['SUMMER']=state_month[['JUNE','JULY','AUGUST']].sum(axis=1)
state_month['AUTUMN']=state_month[['SEPTEMBER','OCTOBER','NOVEMBER']].sum(axis=1)
state_month['WINTER']=state_month[['DECEMBER','JANUARY','FEBRUARY']].sum(axis=1)
state_month['SPRING']=state_month[['MARCH','APRIL','MAY']].sum(axis=1)


# In[102]:


state_month=state_month.drop(['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY'
                                             ,'AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'], axis=1)
print(state_month)


# In[103]:


state_grouped=state_month.groupby(['STATE/UT']).sum()
print(state_grouped.head())


# In[104]:


state_grouped['%_SUMMER']=state_grouped['SUMMER']/state_grouped['TOTAL']
state_grouped['%_AUTUMN']=state_grouped['AUTUMN']/state_grouped['TOTAL']
state_grouped['%_WINTER']=state_grouped['WINTER']/state_grouped['TOTAL']
state_grouped['%_SPRING']=state_grouped['SPRING']/state_grouped['TOTAL']

display(state_grouped.head())


# In[112]:


state_time.rename(columns={'0-3 hrs. (Night)':'0-3',
                              '3-6 hrs. (Night)':'3-6',
                                '6-9 hrs (Day)':'6-9', '9-12 hrs (Day)':'9-12','12-15 hrs (Day)':'12-15','15-18 hrs (Day)':
                                   '15-18','18-21 hrs (Night)':'18-21','21-24 hrs (Night)':'21-24'}, inplace=True)
state_time_grouped=state_time.groupby(['STATE/UT']).sum()

state_time_grouped['MORNING']=(state_time_grouped['6-9']+state_time_grouped['9-12'])
state_time_grouped['AFTERNOON']=(state_time_grouped['12-15']+state_time_grouped['15-18'])
state_time_grouped['EVENING']=(state_time_grouped['18-21']+state_time_grouped['21-24'])
state_time_grouped['NIGHT']=(state_time_grouped['0-3']+state_time_grouped['3-6'])

state_time_grouped['%_MORNING']=(state_time_grouped['6-9']+state_time_grouped['9-12'])/state_time_grouped['Total']
state_time_grouped['%_AFTERNOON']=(state_time_grouped['12-15']+state_time_grouped['15-18'])/state_time_grouped['Total']
state_time_grouped['%_EVENING']=(state_time_grouped['18-21']+state_time_grouped['21-24'])/state_time_grouped['Total']
state_time_grouped['%_NIGHT']=(state_time_grouped['0-3']+state_time_grouped['3-6'])/state_time_grouped['Total']

state_time_grouped=state_time_grouped.drop(state_time_grouped.columns[0:9], axis=1)
display(state_time_grouped.head())


# In[113]:


state_time_grouped['Total'].plot.bar(figsize=(15,5),title="accidents in states")


# In[114]:


t=state_grouped.sort_values('TOTAL')
t['TOTAL'].plot.bar(figsize=(15,5),title="accidents in states")


# In[115]:


state_grouped.boxplot(['%_SUMMER','%_WINTER','%_AUTUMN','%_SPRING'])
plt.show()


# In[130]:


plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
summer_sorted=state_grouped.sort_values('%_SUMMER')
#print(summer_sorted)
summer_sorted['%_SUMMER'].tail(5).plot.bar(title='Highest Summer Accidents percent in total accidents',color='b')
plt.subplot(2,2,2)
winter_sorted=state_grouped.sort_values('%_WINTER')
winter_sorted['%_WINTER'].tail(5).plot.bar(title='Highest Winter Accidents percent in total accidents',color='g')
plt.subplot(2,2,3)
autumn_sorted=state_grouped.sort_values('%_AUTUMN')
autumn_sorted['%_AUTUMN'].tail(5).plot.bar(title='Highest Autumn Accidents percent in total accidents',color='r')
plt.subplot(2,2,4)
spring_sorted=state_grouped.sort_values('%_SPRING')
spring_sorted['%_SPRING'].tail(5).plot.bar(title='Highest Spring Accidents percent in total accidents',color='black')


# In[131]:


plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
morning_sorted=state_time_grouped.sort_values('%_MORNING')
morning_sorted['%_MORNING'].tail(5).plot.bar(title='Highest Morning Accidents percent in total accidents',color='b')
plt.subplot(2,2,2)
afternoon_sorted=state_time_grouped.sort_values('%_AFTERNOON')
afternoon_sorted['%_AFTERNOON'].tail(5).plot.bar(title='Highest Afternoon  Accidents percent in total accidents',color='g')
plt.subplot(2,2,3)
evening_sorted=state_time_grouped.sort_values('%_EVENING')
evening_sorted['%_EVENING'].tail(5).plot.bar(title='Highest Evening Accidents percent in total accidents',color='r')
plt.subplot(2,2,4)
night_sorted=state_time_grouped.sort_values('%_NIGHT')
night_sorted['%_NIGHT'].tail(5).plot.bar(title='Highest Night Accidents percent in total accidents',color='black')


# In[128]:


highest_accident_states=state_grouped.sort_values('TOTAL',ascending=False)
#print(highest_accident_states)
state_list=list(highest_accident_states.head().index)

print(state_list)


# In[132]:


#print(state_time_grouped)
state_time_grouped.loc[:,'MORNING':'NIGHT'].sum(axis=0).plot.pie(title='Daily accidents in INDIA 2001-2014',subplots=True, figsize=(5,5),autopct='%1.1f%%',shadow=True,explode=(0.1,0.1,0.1,0.1))


# In[125]:


state_grouped.loc[:,'SUMMER':'SPRING'].sum(axis=0).plot.pie(figsize=(5,5),title='Seasonal accidents in INDIA(2001-14)'
                                                            ,autopct='%1.1f%%',shadow=True,explode=(0.1,0.1,0.1,0.1))


# In[123]:


day=state_time_grouped.loc[state_time_grouped.index.isin(state_list)]
day=day.drop(state_time_grouped.loc[:,'Total':'NIGHT'],axis=1)
print(day)
print(state_time_grouped.index.isin(state_list))
day_pie=day.T.plot.pie(subplots=True, figsize=(25,25),autopct='%1.1f%%',shadow=True,explode=(0.1,0.1,0.1,0.1))


# In[129]:


#loc is used to access rows or columns by label in pandas(python)
#  .T or .transpose() is used to transpose the index and columns of a dataset
season=state_grouped.loc[state_grouped.index.isin(state_list)]
season=season.drop(state_grouped.loc[:,'YEAR':'SPRING'],axis=1)
print(season)
season_pie=season.T.plot.pie(subplots=True, figsize=(25,25),autopct='%1.1f%%',shadow=True,explode=(0.1,0.1,0.1,0.1))


# In[126]:


acc_total=state_time.groupby(['YEAR']).sum()
acc_total.loc[:,'Total'].plot(title='Accidents growth in India')


# In[ ]:




