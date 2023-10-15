import numpy as np
from matplotlib import pyplot as plt

f = lambda x: np.log(x)  # define function as ln(x)
x = 1.0  # Point at which we want to approximate f'(x)
true_derivative = 1.0  # True derivative value at x=1.0

# Define the central difference scheme for 2nd order and 4th order
D2_func = lambda x, h: (f(x + h) - f(x - h)) / (2 * h)  # 2nd order difference
D4_func = lambda x, h: (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)  # 4th order difference

h = 2.0**(-np.arange(2, 7).astype(float))  # h values as floating points, from 2^-2 to 2^-6

# Calculate the approximations and errors for both schemes
D2 = D2_func(x, h)
D4 = D4_func(x, h)
E2 = abs(true_derivative - D2)
E4 = abs(true_derivative - D4)

# Plot the convergence histories
plt.loglog(1 / h, E2, marker='o', label='Central Difference (2nd Order)')
plt.loglog(1 / h, E4, marker='o', label='Richardson Extrapolation (4th Order)')

# Plot reference lines for 2nd order and 4th order convergence
plt.loglog(1 / h, h**2, '--', label='2nd Order Convergence')
plt.loglog(1 / h, h**4, '--', label='4th Order Convergence')


plt.ylim(1e-12, 1)
plt.grid()
plt.legend()
plt.title('Convergence of Difference Schemes for ln(x) at x=1.0')
plt.xlabel('1/h')
plt.ylabel('Absolute Error')
plt.show()
