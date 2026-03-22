import math                                 # import math for logarithm calculations


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Set search parameters ───────────────────────────────────────────

a   = 0                                     # left bound of the interval
b   = 3                                     # right bound of the interval
eps = 0.5                                   # convergence tolerance
d   = 0.125                                 # probe offset — must satisfy 0 < d < eps


# ─── Step 2: Initialize iteration storage ────────────────────────────────────

iteration_midpoints = []                    # list to store midpoints at each iteration
intervals           = []                    # list to store interval bounds at each iteration
iteration           = 0                     # iteration counter


# ─── Step 3: Run the bisection loop ──────────────────────────────────────────

while abs(b - a) > eps:                     # continue until interval is small enough
    intervals.append((a, b))               # save current interval bounds
    midpoint = (a + b) / 2                 # compute midpoint of current interval
    iteration_midpoints.append(midpoint)   # save midpoint for plotting

    x1 = (a + b - d) / 2                   # left probe point: midpoint - d/2
    x2 = (a + b + d) / 2                   # right probe point: midpoint + d/2

    if f(x1) < f(x2):                      # if left probe has smaller value
        b = x2                             # minimum is in [a, x2], shrink right
    else:                                  # if right probe has smaller value
        a = x1                             # minimum is in [x1, b], shrink left

    iteration += 1                         # increment iteration counter
    print(f"Iter {iteration:2d}: [{a:.4f}, {b:.4f}]  width={b-a:.4f}  "  # print interval
          f"x1={x1:.4f} f={f(x1):.4f}  x2={x2:.4f} f={f(x2):.4f}")      # print probes


# ─── Step 4: Compute final approximate minimum ───────────────────────────────

xmin = (a + b) / 2                         # approximate minimum is center of final interval
print(f"\nApproximate minimum: x* = {xmin:.6f}")  # print approximate x*
print(f"f(x*)                = {f(xmin):.6f}")    # print f at approximate minimum
print(f"Iterations           = {iteration}")      # print total iterations used
print(f"Function evaluations = {2 * iteration}")  # print total function evaluations


# ─── Step 5: Comparison table — Bisection vs. Method of Alternatives ─────────

print(f"\n{'Accuracy e':<14} {'Alternatives':<16} {'Bisection':<16} {'Speedup'}") # print header
print("-" * 58)                             # print separator line

for e in [0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001]:  # loop over accuracy levels
    alt_evals = int((b - a) / e) + 1       # evaluations needed for uniform scan
    bis_evals = 2 * math.ceil(math.log2((b - a) / e))  # evaluations for bisection
    speedup   = alt_evals / bis_evals      # compute speedup ratio
    print(f"{e:<14.4f} {alt_evals:<16} {bis_evals:<16} {speedup:.1f}x")  # print row
