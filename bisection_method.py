import math


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return 0.25 * x**4 + x**2 - 8*x + 12


# ─── Step 1: Set search parameters ───────────────────────────────────────────

a   = 0      # left bound
b   = 2      # right bound
eps = 0.2    # convergence tolerance
d   = 0.1    # probe offset — must satisfy 0 < d < eps


# ─── Step 2: Initialize iteration storage ────────────────────────────────────

iteration_midpoints = []
intervals           = []
iteration           = 0


# ─── Step 3: Run the bisection loop ──────────────────────────────────────────

while abs(b - a) > eps:
    intervals.append((a, b))
    midpoint = (a + b) / 2
    iteration_midpoints.append(midpoint)

    x1 = (a + b - d) / 2
    x2 = (a + b + d) / 2

    if f(x1) < f(x2):
        b = x2
    else:
        a = x1

    iteration += 1
    print(f"Iter {iteration:2d}: [{a:.4f}, {b:.4f}]  width={b-a:.4f}  "
          f"x1={x1:.4f} f={f(x1):.4f}  x2={x2:.4f} f={f(x2):.4f}")


# ─── Step 4: Compute final approximate minimum ───────────────────────────────

xmin = (a + b) / 2

print(f"\nApproximate minimum: x* = {xmin:.6f}")
print(f"f(x*)      = {f(xmin):.6f}")
print(f"Iterations = {iteration}")
print(f"Function evaluations = {2 * iteration}")


# ─── Step 5: Comparison table — Bisection vs. Method of Alternatives ─────────

print(f"\n{'Accuracy e':<14} {'Alternatives':<16} {'Bisection':<16} {'Speedup'}")
print("-" * 58)

for e in [0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001]:
    alt_evals = int(2.0 / e) + 1
    bis_evals = 2 * math.ceil(math.log2(2.0 / e))
    speedup   = alt_evals / bis_evals
    print(f"{e:<14.4f} {alt_evals:<16} {bis_evals:<16} {speedup:.1f}x")
