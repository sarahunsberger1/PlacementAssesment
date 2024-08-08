# Question 2
# Sara Hunsberger

# import libraries
import numpy as np
from sympy import *

#### Find the derivative of L ####

# define the symbols in L
x = Symbol('x')
y = Symbol('y')
b = Symbol('b')

# define L
L = ((y-b*x)**2)
# L when x and y are vectors of more elements L will be ((y1-b*x1)**2 + (y2-b*x2)**2...)
# we take the derivative of one term because the derivatives are just added together for more terms

# find the derivative
L_prime = L.diff(b)
#print(L_prime)

# the derivative is:
# -2*x*(-b*x + y) for each term, so we add this for each element in the vector



######## Define a function for gradient descent ############

def graddesc(x,y,e,b, n):

    # iterate through updating b n times
    for j in range(n):

        # initialize Lprime
        Lprime = 0

        # find the derivative of L with respect to b
        for i, val in enumerate(x):

            # for each element in the vectors x and y add the derivative of L taken at the current b
            Lprime = Lprime + (-2* x[i]*(y[i]-x[i]*b))

        # find the updated value of b
        b = b - (e * Lprime)

    return b


####### Test the function on random normal vectors ########

# set step size and starting b value
e = 0.00001
b = 0

# define random normal vectors
x = np.random.normal(10, 2.5, size=(100))
y = np.random.normal(10, 2.5, size=(100))


# run the function on the test vectors
b = graddesc(x,y,e,b, 1000)

print("The calculated value of b is: " + str(b))

# calculate the known value b for the test vectors to compare
bknown = np.dot(x,y)/(np.linalg.norm(x))**2

print("The known value of b is: " + str(bknown))


# The algorithm fails when e is too large.
# We are trying to find the value b that makes the function L the smallest it can be,
# but with a large enough step size the gradient descent function can skip over the minima that it is
# trying to find and diverge.


