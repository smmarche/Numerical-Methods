#(d)
def newton1(f, fp, x0, tol, m):
    # Find a root of f near x0 with multiplicity m
    # f is the function whose root to be found
    # fp is the derivative of f
    # x0 is the starting point
    # tol is the tolerance for convergence
    # m is the multiplicity of the root

    x = x0
    iteration_count = 0

    while True:
        x_next = x - (m * f(x)) / fp(x)
        iteration_count += 1

        # Check for convergence using the absolute difference between successive x values
        if abs(x_next - x) < tol:
            return x_next, iteration_count

        x = x_next

import math

# function f(x)
f = lambda x: (x - 2)**2 * math.exp(x)

# derivative f'(x)
fp = lambda x: 2 * (x - 2) * math.exp(x) + (x - 2)**2 * math.exp(x)

# Tolerance for convergence
tolerance = 1e-5

# guess
x0 = 2.5

multiplicity = 2

# Find the root and count the iterations
root, iterations = newton1(f, fp, x0, tolerance, multiplicity)

print(f"Approximate root: {root:.5f}")
print(f"Iterations required: {iterations}")
