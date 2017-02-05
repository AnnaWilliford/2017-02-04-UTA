
# coding: utf-8

# # Introduction to Python Functions
# 
# ## What are functions?
# - functions are stand-alone bits of code that perform a particular function
# - when well done, they have a pretty limited scope
# 
# ## Why use functions?
# - functions contribute greatly to creating modularized code
# - modularized code describes a software design technique that emphasizes structuring a program into independent, interchangeable parts
# - ideally, each can stand-alone and will execute one limited aspect of the desired functionality
# - this allows users to easily incorporate an existing function in a new way without having to rewrite it
# - an example might be a function that adds 2 numbers together
# 
# ## Introduction example

# In[1]:

def celsius_fahrenheit():
    # F = (C * 9/5) + 32
    fahrenheit = (22 * (9 / 5)) + 32
    return fahrenheit


# In[2]:

celsius_fahrenheit()


# - you can see here that we have a function that converts celsius to fahrenheit, using a celsius measure of 22 (room temp)
# - note how we use `def` to define a function of a give name, in this case `celsius_fehrenheit`
# - the parentheses allow you to pass arguments to the function, which we haven't done in this case
# - once the function has been created, you can run it by typing `function_name()`
# - if arguments are desired, they would be included inside the parentheses
# - one big issue with this function is that it is way too limited, only converting one measure of celcius to fahrenheit
# - let's make it a bit more flexible by adding an argument

# In[3]:

def celsius_fahrenheit(C):
    # F = (C * 9/5) + 32
    fahrenheit = (C * (9 / 5)) + 32
    return fahrenheit


# In[4]:

celsius_fahrenheit()


# - notice the error we receive if we called it like we did before, which is telling us that an argument is required
# - let's give it one

# In[5]:

celsius_fahrenheit(C=22)


# - you can see this recapitulated what we did before by passing 22 celsius and getting fahrenheit back
# - this is more flexible, however, because we aren't constrained to using only 22

# In[6]:

celsius_fahrenheit(30)


# - another important point is that you can define a default value, which is useful in avoiding errors and making fuctions 'dummy-proof', though it isn't always a good idea

# In[7]:

def celsius_fahrenheit(C=22):
    # F = (C * 9/5) + 32
    fahrenheit = (C * (9 / 5)) + 32
    return fahrenheit


# In[8]:

celsius_fahrenheit()


# - you can see that if no argument is passed, it automatically uses the 5 specified
# - but we can still pass an argument and override the default

# In[9]:

celsius_fahrenheit(15)


# ### Challenge
# - create a function that converts fahrenheit to celsius, much like the one we already have
# - also set default argument values so that it will produce some result, no matter what
# - lastly, determine what the difference is between the supplied temperature, which you are converting to celsius, and a 2nd argument that supplies a temperature that is already in celsius

# In[10]:

def fahrenheit_celsius(F=67, check=22):
    # C = (F - 32) x (5 / 9)
    celsius = (F - 32) * (5 / 9)
    diff_cel = check - celsius
    return diff_cel


# In[11]:

fahrenheit_celsius()


# In[12]:

fahrenheit_celsius(F=5)


# In[13]:

fahrenheit_celsius(5)


# In[14]:

fahrenheit_celsius(check=6)


# In[15]:

fahrenheit_celsius(F=33, check=67)


# In[16]:

fahrenheit_celsius(32, 48)


# ## Advanced example
# - so far what we have done is pretty simple, but you now know the basics of creating modular code with functions
# - let's go back to our full dataset of demography and human health data for US counties and write a meaningful function based on that
# - thinking back to yesterday, what do you have to do first to start working with that data?

# In[17]:

import pandas as pd


# - now you can do the actual data import

# In[18]:

dem_health_data = pd.read_csv("../data/Dem_Health_Full.txt", sep="\t")


# In[19]:

dem_health_data.head()


# - you should recognize what you are looking at
# - only difference is that this includes data for all states, and not just 1
# - before, when everything was separated by state, you created a python script and then used the shell to run it on all states
# - however, what if you want to compare the data in a differet way?
# - you could make a new script that does what you desire and run it in the shell
# - but let's do this totally in python using a function
# - let's say we want to split data into 2 datasets: one that includes cities with very large populations and one that doesn't, and returns the one with cities
# - create a function to do this

# In[24]:

def get_urban(df):
    urban = df.loc[df['Population_Density'] >= 1000, :]
    return urban


# In[26]:

urban_counties = get_urban(dem_health_data)


# In[27]:

urban_counties.head()


# - but what if we want both urban and rural
# - turns out it is pretty easy to do that once you see an example
# - in this case, we are going to return a list that includes 2 elements: the urban subset and the rural subset

# In[48]:

def split_county_by_pop(df):
    urban = df.loc[df['Population_Density'] >= 1000, :]
    rural = df.loc[df['Population_Density'] < 1000, :]
    return [urban, rural]


# In[49]:

urban_rural_counties = split_county_by_pop(dem_health_data)


# In[50]:

urban_rural_counties.head()


# - oops, we can't see the head of a list like we can a data frame
# - let's try printing

# In[51]:

urban_rural_counties


# - that's better, but it still doesn't look like what we had before
# - why?
# - it is because we have a list element, not a dataframe

# In[52]:

type(urban_rural_counties)


# - well what happens when we just want one of the dataframes?
# - is is very easy to subset lists (called slicing) using indexing, where an index represents an ordered section of the element
# - let's do this, remembering that the urban counties are the first element of our list

# In[53]:

urban_rural_counties[1].head()


# - what happened? we have our rural county data not our urban county data
# - python is 0-index or has an origin of 0
# - that means that the first element is 0, 2nd is 1, etc. up to n-1 elements

# In[54]:

urban_rural_counties[0].head()


# ### Challenge
# - great, but notice that we used an inflexble, arbitrary threshold for urban counties
# - at some other time, you may wish to split your dataset using a different threshold
# - let's code a function that allows us to do that as a last challenge

# In[56]:

def split_county_by_pop(df, threshold):
    urban = df.loc[df['Population_Density'] >= threshold, :]
    rural = df.loc[df['Population_Density'] < threshold, :]
    return [urban, rural]


# In[57]:

urban_rural_counties = split_county_by_pop(dem_health_data, 500)


# In[58]:

urban_rural_counties[0].head()


# In[59]:

len(urban_rural_counties[0])


# In[60]:

urban_check = urban_rural_counties[0]


# In[61]:

urban_check.loc[: ,['Population_Density']].min()


# - awesome, we have what we need now!
# - after the break, Gaurav will continue with this dataset but will teach you how to create functions use python plotting capabilities to explore and understand the data
# - keep this Jupyter notebook open and Gaurav will pick up where I left off
