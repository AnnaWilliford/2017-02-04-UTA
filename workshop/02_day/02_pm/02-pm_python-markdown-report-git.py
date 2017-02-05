
# coding: utf-8

# # Evaluating mean poverty levels in urban and rural areas of each U.S. state
# ### Daren Card

# ## Introduction
# Poverty remains a major problem worldwide and, surprisingly, even in the United States. Understanding rates of poverty and their correlates is vital to combating this debilitating public issue. However, many former investigators have focused on poverty levels without understanding how they may vary in urban versus rural areas. The goal of this study is to understand whether average poverty levels in each U.S. state vary in urban and rural counties. I hypothesize that rural areas will have higher poverty rates.

# ## Methods
# I invastigated poverty levels using a dataset obtained from the U.S. Centers for Disease Control, which measured population density and poverty rates in counties nationwide. I began by importing necessary libraries, reading in the data, and viewing its structure.

# In[31]:

import pygal
import pandas as pd
from IPython.display import SVG


# In[32]:

dem_health_data = pd.read_csv("../data/Dem_Health_Full.txt", sep="\t")


# In[33]:

dem_health_data.head()


# I then created three functions that could be used to test my hypothesis:
# - A function that splits the dataset into urban and rural counties based on population density. Density can be varied in anyway possible by the investigator.

# In[34]:

def split_county_by_pop(df, threshold):
    urban = df.loc[df['Population_Density'] >= threshold, :]
    rural = df.loc[df['Population_Density'] < threshold, :]
    return [urban, rural]


# - A function to calculate the average of a gathered demographic or health measurement for a given state. For this function, the investigator can define the state of interest and the column name of the measure to be averaged.

# In[44]:

def mean_of_column(df, state_name, column_name):
    state_df = df.loc[df['State'] == state_name, [column_name]]
    return state_df[column_name].mean()


# - A function that plots the average of a given measure for every state as a bar plot. This function contains a loop that gathers the mean of a demographic or health measure using the `mean_of_column` function defined above. The user can define which measure they want to average and the plot title.

# In[54]:

def plot_state_means(df, measure, title):
    bar_chart = pygal.Bar(legend_box_size=10, legend_at_bottom=True, legend_at_bottom_columns=10,
                         x_title='State', y_title='Poverty Rate')
    bar_chart.title = title
    for state in list(df['State'].unique()):
        bar_chart.add(state, mean_of_column(df, state, measure))
    return SVG(bar_chart.render())


# Using these defined functions, I split the nationwide dataset into two parts by population density, with the urban part comprising counties with a population density greater than 500 and the rural part including counties with a populaiton density less than 500. From here, I plotted a bar chart for each part and visualized whether poverty rates were generally higher or lower in urban versus rural counties in each state.

# ## Results

# In[55]:

split_data = split_county_by_pop(dem_health_data, 500)


# In[56]:

plot_state_means(split_data[0], 'Poverty', 'Poverty Rate in Urban Counties')


# In[57]:

plot_state_means(split_data[1], 'Poverty', 'Poverty Rate in Rural Counties')


# ## Conclusions
# Generally it appears that poverty rates are lower in rural counties, as less county averages exceed a poverty rate of 14. Therefore, I confirm my hypothesis that rural areas have higher poverty rates. The reason for this remains unclear, but it could be due to fewer job opportunities and general economic issues in these areas.
