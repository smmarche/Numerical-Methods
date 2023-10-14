# multi-dimensional Newton's method
import numpy as np
def newton_nd(F,J,x0,tol,N):
  # F = [f1,...fn]
  # J Jacobian matrix of F
  # x0 is the initial guess (n-vector)
  x = np.ones(x0.shape) # initialize solution vector
  y = np.ones(x0.shape) # this is the error vector y = x(i+1) - x(i)
  Fc, Jc = F(x0), J(x0) # evaluate both F and J at the initial value
  count = 0 # initialize counting
  error = np.linalg.norm(y) # Euclidean norm of the error vector
  while (error > tol) and count < N:
    y = np.linalg.solve(Jc, -Fc) # solve the linear system Jy = -F to get y
    x = x0 + y # now add y to previous iterate
    #prints first iteration solution
    print("x^(1) = ", x)
    error = np.linalg.norm(y) # compute the error vector
    print(error) # print the error (this shd go to zero with more counts)
    Fc, Jc = F(x), J(x) # evaluate F and J at new iterate
    x0 = x # update the solution vector
    count+=1 # increase the count by 1
  return x, count # return solution vector and count

#where x[0]=x and x[1]=y
def F(x): #define an example in 2D
  f1= x[1]-x[0]**3 #y-x^3=0
  f2 = x[0]**2+(x[1]**2)-1 #x^2+y^2-1=0
  return np.array([f1,f2]) # return as a 2 vector

def J(x): # define the Jacobian 2 X 2 matrix function
  f1x1, f1x2 = -3*(x[0]**2), 1
  f2x1, f2x2 = 2*(x[0]), 2*(x[1])
  return np.array([[f1x1,f1x2], [f2x1,f2x2]]) # Jacobian matrix function

x0 = np.array([1,2]) # initial vector (solution)

N = 20 # maximum number of permissible iterations

tol = 1e-13 # tolerance

sol, count = newton_nd(F,J,x0,tol,N)
print("The solution is", sol)
print("The number of iterations is", count)
