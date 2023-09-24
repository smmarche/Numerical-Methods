# Bisection Method for finding a fixed point
def bisection(function, a, b, tolerance):
  count = 0 # number of iterations
  while (b-a)/2 > tolerance: # iterate while error > tolerance
    p = (a+b)/2 # approx solution

    #check if the fixed point is in the left side of the interval
    if function(a)*function(p)<0:
      #if it is in the left side change the right most endpoint (b) to p
      b = p
    else:
      #otherwise the fixed point is in the right half of the interval
      #so change the left most endpoint (a) to p
      a = p
    count+=1 # add to count
  return p, count # return both root and count
import math

#define endpoints and tolerance level
a, b, tolerance = 1, 2, 1e-8

# Define the first function
def function_a(x):
    function_answera = x**2 - 4*x + 4 - math.log(x)
    return function_answera

# Calculate
p, count = bisection(function_a, a, b, tolerance)
print("(a)")
print(p)
print(count)
print()

# Define endpoints and tolerance level
a, b, tolerance = 3, 4, 1e-8

# Define the second function
def function_b(y):
    function_answerb = y**y - 50
    return function_answerb

# Calculate
p, count = bisection(function_b, a, b, tolerance)
print("(b)")
print(p)
print(count)
print()

# Define endpoints and tolerance level
a, b, tolerance = -1, 1, 1e-8

# Define the third function
def function_c(z):
    function_answerc = 2*z + 3*math.cos(z) - math.exp(z)
    return function_answerc

# Calculate
p, count = bisection(function_c, a, b, tolerance)
print("(c)")
print(p)
print(count)
