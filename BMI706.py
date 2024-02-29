#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Hypothetical data for the dashboard
data = {
    'Year': [2010, 2010, 2010, 2011, 2011, 2011, 2012, 2012, 2012] * 3,
    'County': ['Albany', 'Bronx', 'Broome'] * 9,
    'Cause of Death': ['Diseases of the Heart', 'Accidents', 'Diabetes Mellitus'] * 9,
    'Deaths': [771, 132, 30] * 9
}

df = pd.DataFrame(data)

# Group data by Year and Cause of Death for line chart
line_chart_data = df.groupby(['Year', 'Cause of Death'])['Deaths'].sum().unstack()

# Group data by Cause of Death for pie chart
pie_chart_data = df[df['Year'] == 2010]['Deaths'].groupby(df['Cause of Death']).sum()

# Group data by County for bar chart
bar_chart_data = df[df['Year'] == 2010]['Deaths'].groupby(df['County']).sum()

# Create line chart
plt.figure(figsize=(10, 6))
sns.lineplot(data=line_chart_data)
plt.title('Trend of Deaths by Cause Over Years')
plt.ylabel('Number of Deaths')
plt.xlabel('Year')
plt.legend(title='Cause of Death')
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit the figure nicely
plt.savefig('line_chart.png')  # Save the figure as a .png file
plt.show()

# Create pie chart
plt.figure(figsize=(8, 8))
pie_chart_data.plot(kind='pie', autopct='%1.1f%%')
plt.title('Cause of Death Distribution for 2010')
plt.ylabel('')  # Hide the y-axis label
plt.tight_layout()  # Adjust layout to fit the figure nicely
plt.savefig('pie_chart.png')  # Save the figure as a .png file
plt.show()

# Create bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=bar_chart_data.index, y=bar_chart_data.values)
plt.title('Total Number of Deaths by County for 2010')
plt.ylabel('Number of Deaths')
plt.xlabel('County')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to fit the figure nicely
plt.savefig('bar_chart.png')  # Save the figure as a .png file
plt.show()


# In[19]:


import numpy as np

# Generating hypothetical data for the visualizations
np.random.seed(0)  

# Heatmap data for age-groups
age_groups = ['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']
years = list(range(2010, 2021))
heatmap_data = np.random.rand(len(years), len(age_groups))

# Adjusting the heatmap data to represent deaths per total deaths of the year (per 100k for simplicity in this hypothetical scenario)
total_deaths_per_year = heatmap_data.sum(axis=1) * 100000  # Hypothetical total deaths per year
heatmap_data_normalized = heatmap_data / total_deaths_per_year[:, np.newaxis]

# Generating hypothetical gender and ethnicity data for the bar chart
genders = ['Male', 'Female']
ethnicities = ['Black', 'Hispanic', 'White', 'Other']
gender_ethnicity_deaths = np.random.randint(100, 500, size=(len(genders), len(ethnicities)))

# Creating the adjusted figures
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Adjusted heatmap for age-groups
sns.heatmap(heatmap_data_normalized, ax=axs[0, 0], cmap="Blues", annot=True, fmt=".2f", xticklabels=age_groups, yticklabels=years)
axs[0, 0].set_title('Heatmap of Mortality Rates by Age Group (per 100k)')

# Adjusted bar chart for gender differences with ethnicity
gender_ethnicity_df = pd.DataFrame(gender_ethnicity_deaths, index=genders, columns=ethnicities)
gender_ethnicity_df.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ax=axs[0, 1])
axs[0, 1].set_title('Mortality Rates by Gender and Ethnicity')
axs[0, 1].set_xlabel('Gender')
axs[0, 1].set_ylabel('Number of Deaths')

# Trend line for different accident causes (no change needed)
sns.lineplot(x='Year', y='Deaths', hue='Cause', data=line_chart_data, ax=axs[1, 0], marker='o')
axs[1, 0].set_title('Trend of Deaths by Different Accident Causes')

# Pie chart for proportion of causes of death (no change needed)
axs[1, 1].pie(pie_chart_data['Deaths'], labels=pie_chart_data['Cause'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('tab10'))
axs[1, 1].set_title('Proportion of Causes of Death')

plt.tight_layout()
plt.show()


# In[8]:


# Generating hypothetical data for the heatmap with races on the y-axis and age groups on the x-axis
np.random.seed(0)  # Seed for reproducibility

# Data setup
age_groups = ['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']
races = ['Black', 'Hispanic', 'White', 'Other']
heatmap_data_by_race_age = np.random.rand(len(races), len(age_groups))

# Normalize data to represent deaths per total deaths of each race (per 100k for simplicity)
total_deaths_per_race = heatmap_data_by_race_age.sum(axis=1) * 100000
heatmap_data_normalized_by_race_age = (heatmap_data_by_race_age.T / total_deaths_per_race).T

# Create the adjusted heatmap for race and age group
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data_normalized_by_race_age, cmap="Blues", annot=True, fmt=".2f", yticklabels=races, xticklabels=age_groups)
plt.title('Heatmap of Mortality Rates by Race and Age Group (per 100k)')
plt.ylabel('Race')
plt.xlabel('Age Group')
plt.show()


# In[ ]:




