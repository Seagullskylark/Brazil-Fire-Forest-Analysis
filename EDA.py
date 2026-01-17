

# importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importing Dataset
data=pd.read_csv('E:/Data Science/Project/amazon.csv',encoding='iso-8859-1')

# displaying first 5 rows of dataset

data.head()

data.dtypes

# Checking last 5 rows of dataset

data.tail()

#Find the Shape of Our Dataset

data.shape

print('number of Rows: ',data.shape[0])
print('Number Of Columns :',data.shape[1])

#Get the information about our Dataset


data.info()

# Check Duplicated Data and drop them

print('Any Duplicated Value ?: ',data.duplicated().any())

data=data.drop_duplicates()

print('Any Duplicated Value ?: ',data.duplicated().any())

data.isnull().any()

# Display isnull values using Heatmap
sns.heatmap(data.isnull())

data.isnull().sum()

# Get Overall Statstics about the Dataset

data.describe(include='all')

# Cleaning Month Data

data['month']

list1=[]

for mon in data['month']:
    if mon not in list1:
        list1.append(mon)

list1

data['New_Month']=data['month'].map(
    {
        'Janeiro':'jan',
        'Fevereiro':'feb',
        'Março':'march',
        'Abril':'april',
        'Maio':'may',
        'Junho':'june',
        'Julho':'jully',
        'Agosto':'august',
        'Setembro':'sep',
        'Outubro':'oct',
        'Novembro':'nov',
        'Dezembro':'dec'
 
    }
)


data.head()

# Total No. Of Forest Fire registered

data.columns

data['number'].count()

# Which months Maximum number of fires were reported?

data.columns

data.groupby('New_Month')['number'].sum().sort_values(ascending=False).reset_index().set_index('New_Month').head(1)
# Visualization
plt.figure(figsize=(16,5))
sns.barplot(x='New_Month',y='number',data=data,hue='New_Month')
plt.title('Fires By Months')
plt.show()

# In Which year Maximum Number of Forest Fire were Reported ?

data.columns

data.groupby('year')['number'].sum().sort_values(ascending=False).reset_index().set_index('year').head(1)
# Visualization
plt.figure(figsize=(15,7))
sns.barplot(x='year',y='number',data=data,hue='year')
plt.title('Forest Fire By Year')
plt.show()

# In Which State Maximum number Of Forest Fire Were Reported ?

data.columns

data.groupby('state')['number'].sum().sort_values(ascending=False).reset_index().set_index('state').head(1)

plt.figure(figsize=(16,5))
sns.barplot(x='state',y='number',data=data,hue='state')
plt.xticks(rotation=75)
plt.title('Forest Fire By State')
plt.show()

# Find Total Number of Fires were Reported in Amazonas

data.columns

print('Total no Of Fires reported In Amazonas State  is: ',data[data['state']=='Amazonas']['number'].sum())

# Display Number of Fires Were Reported in Amazonas (Year-wise)

data.columns

data1=data[data['state']=='Amazonas']

data2=data1.groupby('year')['number'].sum().sort_values(ascending=False).reset_index().set_index('year')

data2

plt.figure(figsize=(16,5))
sns.barplot(x=data2.index,y='number',data=data2,hue='number')
plt.xticks(rotation=75)
plt.title('Forest Fire Reported in Amazonas (Year-Wise)')
plt.show()

# Find the total Number of Fires were Reported in 2015 and visualize data based on each Month

data.columns

fire=data[data['year']==2015].groupby('New_Month')['number'].sum().reset_index()

fire

plt.figure(figsize=(10,5))
sns.barplot(x='number',y='New_Month',data=fire,hue='New_Month')
plt.title('Total Number of Fires in Each Months in 2015')
plt.show()


# Find the Avg No of Fires Were Reported From Higest To Lowest (State-Wise)

state_wise=data.groupby('state')['number'].mean().sort_values(ascending=False).reset_index()
state_wise

plt.figure(figsize=(20,6))
sns.barplot(x='state',y='number',data=state_wise,hue='state')
plt.xticks(rotation=75)
plt.title('State Wise Fire')
plt.show()

# Find the State Name Where Fires Were Reported in 'dec' Month

data.columns

data[data['New_Month']=='dec']['state'].unique()



