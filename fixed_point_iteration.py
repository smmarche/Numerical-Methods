def fpi(g,x0,n):
  # fixed point iteration to solve x = g(x)
  # x0 is the initial point
  # n is the number of iterations
  x = x0
  for j in range(n):
    x = g(x)
    if j == 48:
      print(f"Prior x (49th iteration) value to prove correctness: {x}")
  return x

import math
g = lambda x: 2*math.cosh(x/4)
x0, n = 8.5, 50
fpi(g,x0,n)
