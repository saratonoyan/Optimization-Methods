import numpy as np                          # import numpy for numerical operations
from scipy.optimize import minimize         # import minimize for exact reference solution


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Set search parameters ───────────────────────────────────────────

a = 0                                       # left bound of the interval
b = 3                                       # right bound of the interval
e = 0.5                                     # step size — result is accurate within ± e


# ─── Step 2: Compute number of sample points ─────────────────────────────────

n = int((b - a) / e)                        # number of intervals → n+1 points
print(f"Number of sample points: {n + 1}")  # print total number of points


# ─── Step 3: Generate equally spaced x-values ────────────────────────────────

l_x = [a + i * e for i in range(n + 1)]    # generate x_i = a + i*e for i = 0..n
print("Sample x-values:", l_x)              # print all sample x-values


# ─── Step 4: Evaluate the function at each point ─────────────────────────────

l_y = [f(x) for x in l_x]                  # compute f(x) for every sample point
print("f(x) values:", [round(y, 4) for y in l_y])  # print rounded f(x) values


# ─── Step 5: Find the approximate minimum ────────────────────────────────────

f_min = min(l_y)                            # find the smallest f(x) value
x_min = l_x[l_y.index(f_min)]              # find the x that gives the smallest f(x)
print(f"\nApproximate minimum: f({x_min}) = {f_min:.6f}")  # print result


# ─── Step 6: Compare with exact minimum ──────────────────────────────────────

result      = minimize(f, x0=1.5, bounds=[(0, 3)])  # find exact minimum using scipy
min_x_exact = result.x[0]                           # extract exact x*
min_y_exact = result.fun                            # extract exact f(x*)

print(f"Exact minimum:       f({min_x_exact:.6f}) = {min_y_exact:.6f}")         # print exact result
print(f"Approximation error: {abs(x_min - min_x_exact):.6f}  (expected <= {e})") # print error


# ─── Step 7: Accuracy vs. cost table ─────────────────────────────────────────

print(f"\n{'Step e':<12} {'Points':<10} {'x approx':<14} {'f(x)':<16} {'Error'}") # print header
print("-" * 62)                             # print separator line

for eps in [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]:  # loop over different step sizes
    n_i = int((b - a) / eps)               # compute number of intervals for this step
    xs  = [a + i * eps for i in range(n_i + 1)]  # generate sample points
    ys  = [f(x) for x in xs]              # evaluate function at each point
    idx = ys.index(min(ys))               # find index of minimum value
    err = abs(xs[idx] - min_x_exact)      # compute error vs exact solution
    print(f"{eps:<12.3f} {n_i+1:<10} {xs[idx]:<14.4f} {ys[idx]:<16.6f} {err:.4f}") # print row
