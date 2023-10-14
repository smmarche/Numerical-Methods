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
