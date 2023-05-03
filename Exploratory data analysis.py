#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv("iris.csv")


# In[5]:


df


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df['Species'].value_counts()


# In[9]:


iris_setosa=df.loc[df['Species'] == 'Iris-setosa'];
iris_versicolor=df.loc[df['Species'] == 'Iris-versicolor'];
iris_virginica=df.loc[df['Species'] == 'Iris-virginica'];


# In[10]:


print(np.median(iris_setosa['SepalLengthCm']))


# # 2D Scatter Plot

# In[11]:


df.plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm')
plt.show()


# In[12]:


sns.set_style('whitegrid');
sns.FacetGrid(df,hue='Species',height=4)    .map(plt.scatter,'SepalLengthCm','SepalWidthCm')    .add_legend();
plt.show()


# In[13]:


sns.set_style('whitegrid');
sns.FacetGrid(df,hue='Species',height=4)    .map(plt.scatter,'PetalLengthCm','PetalWidthCm')    .add_legend();
plt.show();


# # pairplot

# In[14]:


sns.set_style('whitegrid');
sns.pairplot(df,hue='Species',height=3);
plt.show()


# In[15]:


sns.set_style('whitegrid')
sns.FacetGrid(df,hue='Species',height=8)    .map(sns.distplot,'PetalLengthCm')     .add_legend();
plt.show();


# In[16]:


sns.FacetGrid(df,hue='Species',height=8)    .map(sns.distplot,'PetalWidthCm')     .add_legend();
plt.show();


# In[17]:


sns.FacetGrid(df,hue='Species',height=8)    .map(sns.distplot,'SepalLengthCm')     .add_legend();
plt.show();


# In[18]:


sns.FacetGrid(df,hue='Species',height=8)    .map(sns.distplot,'SepalLengthCm')     .add_legend();
plt.show();


# In[19]:


sns.FacetGrid(df,hue='Species',height=8)    .map(sns.distplot,'SepalWidthCm')     .add_legend();
plt.show();


# In[20]:


import numpy as np
print(np.median(iris_setosa['PetalLengthCm']))


# In[21]:


sns.boxplot(x='Species',y='PetalLengthCm',data=df)
plt.show()


# In[22]:


sns.boxplot(x='Species',y='SepalWidthCm',data=df)
plt.show()


# In[23]:


sns.boxplot(x='Species',y='PetalWidthCm',data=df)
plt.show()


# In[24]:


sns.boxplot(x='Species',y='SepalLengthCm',data=df)
plt.show()


# In[26]:


print(np.mean(iris_setosa['SepalLengthCm']))
print(np.mean(iris_setosa['SepalWidthCm']))
print(np.mean(iris_setosa['PetalLengthCm']))
print(np.mean(iris_setosa['PetalWidthCm']))


# In[27]:


print(np.median(iris_setosa['SepalLengthCm']))
print(np.median(iris_setosa['SepalWidthCm']))
print(np.median(iris_setosa['PetalLengthCm']))
print(np.median(iris_setosa['PetalWidthCm']))


# In[28]:


print(np.std(iris_setosa['SepalLengthCm']))
print(np.std(iris_setosa['SepalWidthCm']))
print(np.std(iris_setosa['PetalLengthCm']))
print(np.std(iris_setosa['PetalWidthCm']))


# # LinePlot

# In[29]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]


# In[34]:


plt.plot(days,temperature,c="g")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.title("delhi temperature")
plt.show()


# In[38]:


plt.plot(days,temperature,c="g")
plt.axis([0,30,0,50])
plt.xlabel("days")
plt.ylabel("Temperature")
plt.title("delhi temperature")
plt.show()


# In[74]:


from matplotlib.pyplot import style
style.use("ggplot")
plt.plot(days,temperature,'go:',lw="4")
plt.xlabel("days",fontsize='16')
plt.ylabel("Temperature",fontsize='16')
plt.title("delhi temperature",fontsize='20')
plt.legend(["Tem"],loc=4)
plt.show()


# In[73]:


sns.set_style('whitegrid')
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_tem = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_tem = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]
 
plt.plot(days, delhi_tem, "co--", linewidth = 3,
        markersize = 10, label = "Delhi tem")
 
plt.plot(days, mumbai_tem, "yo:", linewidth = 3,
        markersize = 10, label = "Mumbai tem}")
 
plt.title("Delhi  & Mumbai Temperature", fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc = 4)
plt.show()


# # Histogram
# 

# In[85]:


import random
import matplotlib.pyplot as plt


# In[108]:


ml_students_age = np.random.randint(18,45, (100))
py_students_age = np.random.randint(15,50, (100))


# In[109]:


bins=[15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,color='m',label="ML student")
plt.title("age graph")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.legend()
plt.show()


# In[110]:


bins=[15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,orientation="horizontal")
plt.title("age graph")
plt.xlabel("Students age category")
plt.ylabel("No. Students age")
plt.show()


# In[114]:


plt.figure(figsize = (16,9)) 
plt.hist([ml_students_age, py_students_age], bins, rwidth=0.8, histtype = "bar",
         orientation='vertical', color = ["c", "y"], label = ["ML Student", "Py Student"])
 
#plt.hist(py_students_age, bins, rwidth=0.8, histtype = "bar",
#         orientation='vertical', color = "y", label = "Py Student")
 
plt.title("ML & Py Students age histograms",fontsize='25')
plt.xlabel("Students age cotegory",fontsize='16')
plt.ylabel("No. Students age",fontsize='16')
plt.legend()
plt.show()


# # Barchart

# In[115]:


classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10] # out of 100 student in each class
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15]


# In[121]:


plt.bar(classes,class1_students,color='b')
plt.xlabel('Classes')
plt.ylabel('class1_students')
plt.show()


# In[130]:


plt.barh(classes,class1_students,color='b')
plt.xlabel('Classes')
plt.ylabel('class1_students')
plt.show()


# In[129]:


plt.bar(classes,class1_students,color='y',width=0.7,edgecolor='g',lw=3)
plt.xlabel('Classes')
plt.ylabel('class1_students')
plt.show()


# # Piechart

# In[131]:


classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece']
class1_students = [45, 15, 35, 25, 30]


# In[132]:


plt.pie(class1_students, labels = classes)
plt.show()


# In[136]:


explode = [0.03,0,0.1,0,0] # To slice the perticuler section
#colors = ["c", 'b','r','y','g'] # Color of each section
textprops = {"fontsize":15} # Font size of text in pie chart
 
plt.pie(class1_students, # Values
        labels = classes, # Labels for each sections
        explode = explode, # To slice the perticuler section
        #colors =colors, # Color of each section
        autopct = "%0.2f%%", # Show data in persentage for with 2 decimal point
        shadow = True, # Showing shadow of pie chart
        radius = 1.4, # Radius to increase or decrease the size of pie chart 
       startangle = 270, # Start angle of first section
        textprops =textprops) 
plt.legend()
plt.show() # To show pie chart only


# # Seaborn Tutorial

# # Lineplot

# In[138]:


tips_df = sns.load_dataset("tips")
tips_df


# In[140]:


sns.lineplot(x='total_bill',y='tip',data=tips_df)
plt.show()


# In[141]:


sns.lineplot(x = "tip", y = "total_bill", data = tips_df)


# In[142]:


sns.lineplot(x = "tip", y = "size", data = tips_df)


# In[143]:


sns.lineplot(x = "size", y = "total_bill", data = tips_df)


# In[144]:


plt.figure(figsize = (16,9)) # figure size with ratio 16:9
sns.set(style='darkgrid',) # background darkgrid style of graph 
 
# Draw line plot of size and total_bill with parameters
sns.lineplot(x = "size", y = "total_bill", data = tips_df, hue = "sex",
            style = "sex", palette = "hot", dashes = False, 
            markers = ["o", "<"],  legend="brief",)
 
plt.title("Line Plot", fontsize = 20)
plt.xlabel("Size", fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# In[145]:


plt.figure(figsize = (16,9))
sns.set(style='darkgrid',)
 
# Draw line plot of size and total_bill with parameters and hue "day"
sns.lineplot(x = "size", y = "total_bill", data = tips_df, hue = "day",
            style = "day", palette = "hot", dashes = False, 
            markers = ["o", "<", ">", "^"],  legend="brief",)
 
plt.title("Line Plot", fontsize = 20)
plt.xlabel("Size", fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# In[ ]:


print(0 or 1)


# In[ ]:




