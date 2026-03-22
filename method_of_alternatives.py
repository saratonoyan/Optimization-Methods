import numpy as np
from scipy.optimize import minimize


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return (1/4) * x**4 + x**2 - 8*x + 12


# ─── Step 1: Set search parameters ───────────────────────────────────────────

a = 0       # left bound
b = 2       # right bound
e = 0.5     # step size (result is accurate within ± e)


# ─── Step 2: Compute number of sample points ─────────────────────────────────

n = int((b - a) / e)
print(f"Number of sample points: {n + 1}")


# ─── Step 3: Generate equally spaced x-values ────────────────────────────────

l_x = [a + i * e for i in range(n + 1)]
print("Sample x-values:", l_x)


# ─── Step 4: Evaluate the function at each point ─────────────────────────────

l_y = [f(x) for x in l_x]
print("f(x) values:", [round(y, 4) for y in l_y])


# ─── Step 5: Find the approximate minimum ────────────────────────────────────

f_min = min(l_y)
x_min = l_x[l_y.index(f_min)]

print(f"\nApproximate minimum: f({x_min}) = {f_min:.6f}")


# ─── Step 6: Compare with exact minimum ──────────────────────────────────────

result      = minimize(f, x0=1.5, bounds=[(0, 2)])
min_x_exact = result.x[0]
min_y_exact = result.fun

print(f"Exact minimum:       f({min_x_exact:.6f}) = {min_y_exact:.6f}")
print(f"Approximation error: {abs(x_min - min_x_exact):.6f}  (expected <= e = {e})")


# ─── Step 7: Accuracy vs. cost table ─────────────────────────────────────────

print(f"\n{'Step e':<12} {'Points':<10} {'x approx':<14} {'f(x)':<16} {'Error'}")
print("-" * 62)

for eps in [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]:
    n_i = int(2.0 / eps)
    xs  = [i * eps for i in range(n_i + 1)]
    ys  = [f(x) for x in xs]
    idx = ys.index(min(ys))
    err = abs(xs[idx] - min_x_exact)
    print(f"{eps:<12.3f} {n_i+1:<10} {xs[idx]:<14.4f} {ys[idx]:<16.6f} {err:.4f}")
