def newton(f, fp, x0, tol):
    # Find a root of f near x0
    # f is the function whose root to be found
    # fp is the derivative of f
    # x0 is the starting point
    # tol is the tolerance for convergence

    x = x0
    iteration_count = 0

    while True:
        x_next = x - f(x) / fp(x)
        iteration_count += 1

        # Check for convergence using the absolute difference between successive x values
        if abs(x_next - x) < tol:
            return x_next, iteration_count

        x = x_next

# Example usage:
import math

f = lambda x: x**2 - 4  # Example function
fp = lambda x: 2 * x   # Derivative of the example function
x0 = 3.0               # Starting point
tolerance = 1e-6       # Tolerance for convergence

root, iterations = newton(f, fp, x0, tolerance)
print(f"Approximate root: {root:.5f}")
print(f"Iteration count: {iterations}")

# function f(x)
f = lambda x: x - 2 * math.cosh(x / 4)

# function derivative f'(x)
fp = lambda x: 1 - 0.5 * math.sinh(x / 4)


tolerance = 1e-13

# first root guess
x0_1 = 2.0  # You can choose an appropriate initial guess

# Find the first root
root1, iterations1 = newton(f, fp, x0_1, tolerance)
print(f"Approximate root 1: {root1:.13f}")
print(f"Iterations for root 1: {iterations1}")

# second root guess
x0_2 = 8.0  # You can choose an appropriate initial guess

# Find the second root
root2, iterations2 = newton(f, fp, x0_2, tolerance)
print(f"Approximate root 2: {root2:.13f}")
print(f"Iterations for root 2: {iterations2}")
