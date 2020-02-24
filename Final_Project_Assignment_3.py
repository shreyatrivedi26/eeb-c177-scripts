#!/usr/bin/env python 
# coding: utf-8

# In[24]:


import netCDF4 as nf
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


data_temp = nf.Dataset("air.mon.mean_1979-2015.nc")


# In[26]:


variables_temp = data_temp.variables


# In[27]:


#Creating the time stamps in the form of real time date format: 
time_temp = variables_temp["time"]


# In[28]:


time_start_temp = nf.date2index(dt.datetime(1979,1,1),time_temp,select="nearest")
time_end_temp = nf.date2index(dt.datetime(2015,12,31),time_temp,select="nearest")

dates= nf.num2date(time_temp[:],time_temp.units)
time= ([date.strftime('%Y-%m-%d') for date in dates[:]])


# ### Selecting the desired dates from the dataset: 
# 
# Selecting only the months of May, June, July, August, September and Octoberand the years from 2002-2011. The filtering of the dates is done so that comparision can be made with the another netcdf file which incorporates the sea-ice values for the above timescale. 

# In[29]:


#selecting the months:
new_mon_temp=[]
for ii in range(len(time)):
    if time[ii][5:7]=='05'or time[ii][5:7]=='06' or time[ii][5:7]=='07' or time[ii][5:7]=='08' or time[ii][5:7]=='09' or time[ii][5:7]=='10':
        new_mon_temp.append(time[ii])


# In[30]:


#selecting the years:
new_time_temp=[]
for ii in range(len(new_mon_temp)):
    if new_mon_temp[ii][0:4]=='2002'or new_mon_temp[ii][0:4]=='2003' or new_mon_temp[ii][0:4]=='2004' or new_mon_temp[ii][0:4]=='2005' or new_mon_temp[ii][0:4]=='2006' or new_mon_temp[ii][0:4]=='2007' or new_mon_temp[ii][0:4]=='2008' or new_mon_temp[ii][0:4]=='2009' or new_mon_temp[ii][0:4]=='2010' or new_mon_temp[ii][0:4]=='2011':
        new_time_temp.append(new_mon_temp[ii])


# ### Plotting temperatures with Sea-ice values:

# In[67]:


temp_new = nf.Dataset("air.mon.mean_M-O_2002-2011.nc")
data_SICE = nf.Dataset("sum_test.nc")


# In[68]:


variables_SICE = data_SICE.variables
variables_new_temp= temp_new.variables


# In[69]:


time_SICE = variables_SICE["time"]
time_new_temp= variables_new_temp["time"]
SIT=variables_SICE["SIT"]
air_temp=variables_new_temp["air"]


# ### Converting timesteps into a well defined date format:
# 
# Using the same function as above.

# In[70]:


time_start_temp = nf.date2index(dt.datetime(2002,10,15),time_new_temp,select="nearest")
time_end_temp = nf.date2index(dt.datetime(2011,10,15),time_new_temp,select="nearest")

dates= nf.num2date(time_new_temp[:],time_new_temp.units)
time= ([date.strftime('%Y-%m-%d') for date in dates[:]])


# In[71]:


air_temp_850hpa=air_temp[:,2,:,:]


# In[118]:


#mean Sea Ice Thickness (SIT) array

SIT_mean=[]
for ii in range(len(SIT)):
    mean_SIT = np.mean(SIT[ii])
    SIT_mean.append(mean_SIT/20000)#since the values of SIT were very high compared to the temperatures, 
    #they are normalized by diving it by 20000
print(SIT_mean)


# In[111]:


#mean temperature array

temp_mean=[]
for ii in range(len(air_temp_850hpa)):
    mean = np.mean(air_temp_850hpa[ii])
    temp_mean.append(mean)
print(temp_mean)


# ## Comparitive plot to study relations between temperature and Sea-ice Thickness: 
# 
# Dates used on the x-axis are the ones which are extracted in a proper date format.
# 

# In[74]:


fig = plt.figure(figsize=(16.0,10.0))
plt.plot(time,SIT_mean, marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=4,label='SIT')
plt.plot(time,temp_mean, marker='', color='red', linewidth=2, linestyle='dashed', label="Temperatures")
plt.xticks(np.arange(0, 55, 4.0))
plt.xlabel('Dates')
plt.ylabel('Mean values')
plt.title('Global Temperatures and SIT trends:Spring and Winter Seasons (2002-11)')
plt.legend(loc='best')
plt.show()


# In[100]:


a=np.std(air_temp_850hpa)
error = a/(np.max(air_temp_850hpa)-np.min(air_temp_850hpa)) 
error


# In[104]:


fig = plt.figure(figsize=(16.0,10.0))
plt.plot(time,temp_mean, marker='', color='black', linewidth=2, linestyle='dashed', label="Temperatures")
plt.xticks(np.arange(0, 55, 4.0))
plt.xlabel('Dates')
plt.ylabel('Mean values')
plt.title('Global Temperatures trends with NRMSE:Spring and Winter Seasons (2002-11)')
plt.fill_between(time, temp_mean-error, temp_mean+error)
plt.show()


# In[105]:


a=np.std(SIT)
error = a/(np.max(SIT)-np.min(SIT)) 
error


# In[108]:


fig = plt.figure(figsize=(16.0,10.0))
plt.plot(time,SIT_mean, marker='', color='black', linewidth=2, linestyle='dashed')
plt.xticks(np.arange(0, 55, 4.0))
plt.xlabel('Dates')
plt.ylabel('Mean values')
plt.title('Global SIT trends with NRMSE:Spring and Winter Seasons (2002-11)')
plt.fill_between(time, SIT_mean-error, SIT_mean+error)
plt.show()


# ## Working with anomalies and barplots:
# 
# Anomalies are a measure of the departure from the mean. This is achieved by subtracting the mean values from every value in the dataset. 
# The boxplot is the best representation of the anomalies. 

# In[133]:


SIT_anom=[]
mean=np.mean(SIT[:])
for ii in range(len(SIT)):
    anomaly = np.mean(SIT[ii])-mean
    SIT_anom.append(anomaly/20000)#since the values of SIT were very high compared to the temperatures, 
    #they are normalized by diving it by 20000
print(list(SIT_anom))


# In[167]:


fig = plt.figure(figsize=(13.0,10.0))
ax = plt.subplot(111)
ax.bar(time, SIT_anom, width=1, color='b')
plt.xticks(np.arange(0, 55, 6.0))
plt.xlabel('Dates')
plt.ylabel('Anomalies')
plt.title('Anarctic SIT anomaly trends:Spring and Winter Seasons (2002-11)')

plt.show()


# In[ ]:




