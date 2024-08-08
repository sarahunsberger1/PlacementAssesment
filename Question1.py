# Question 1
# Sara Hunsberger

# import the necessary libraries
import requests
import pandas as pd
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

############# Scrape the website ##############

# load the URL
URL = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"
page = requests.get(URL)

# load the tables from the website into pandas dataframes
all_tables = pd.read_html(URL)

# find the tables we care about

# 20th century table
table20th = all_tables[2]
# 21st century table
table21st = all_tables[3]

# merge the tables
fulltable = pd.concat([table20th, table21st])


########## Convert death toll to numbers ################

# create a function to help convert the death toll to numbers from strings
def convertdeathtoll(n):

    # replace any commas inserted in the numbers
    if ',' in n:
        n = n.replace(",", "")

    # take away plus signs
    if "+" in n:
        n = n.replace("+", "")

    # some numbers have a reference behind them (take away the reference)
    if '[' in n:
        n = n.split("[")
        n = n[0]

    # split the ranges by the dash (there are 2 types)
    if '-' in n:
        l = n.split("-")

        # only get the numbers from the strings
        for i, numb in enumerate(l):
            l[i] = int(re.findall(r'\d+', numb)[0])

        # find the midpoint of the range
        n = np.mean(l)


    # split the ranges by the dash (there are 2 types)
    elif '–' in n:
        l = n.split("–")

        # only get the numbers from the strings
        for i, numb in enumerate(l):
            l[i] = int(re.findall(r'\d+', numb)[0])

        # find the midpoint of the range
        n = np.mean(l)

    # make sure each value is of the type integer
    n = int(n)

    return n

# convert the death toll to numbers
fulltable['Death toll'] = fulltable['Death toll'].apply(lambda x: convertdeathtoll(x))

############### Make plot ###########

# make a scatter plot, with color for the type of event
sns.scatterplot(data = fulltable, x='Year', y='Death toll', hue = 'Type')

# add title
plt.suptitle('Death Toll of Natural Disasters in the 20th and 21st centuries')

# show the plot
plt.show()

