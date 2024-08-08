# Placement Assesment
## Sara Hunsberger

This repository contains the code for my solutions to the Biostatistics PhD Data Science Placement Assessment. 

## Question 1

The code for Question 1 is contained in the file called Question1.py. This code scrapes the webpage https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll and puts data
from the Natural disasters of the 20th and 21st centuries into a pandas data frame. The death toll data is converted to numeric data and then a plot is created using seaborn. 
The plot is called DeathTollPlot.png in the repository. The plot shows the death toll of each natural disaster in the 20th and 21st centuries by the year that they occured. 
Each point on the plot represents one natural disaster where the x-axis value of that point is the year that it occured and the y value is how many people died as a result of that disaster. 
The color of the point represents what type of disaster it was, we can find the type of disaster by looking at the key on the right of the plot. 


## Question 2

The code for Question 2 is contained in the file called Question2.py. This code minimizes the loss over b using gradient descent. We find that the algorithm fails when e is too large.
We are trying to find the value b that makes the function L the smallest it can be,
but with a large enough step size the gradient descent function can skip over the minima that it is
trying to find and diverge.
