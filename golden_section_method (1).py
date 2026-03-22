import numpy as np                          # import numpy for numerical operations
import math                                 # import math for logarithm calculations


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Define golden ratio constants ────────────────────────────────────

PHI     = (1 + np.sqrt(5)) / 2             # golden ratio φ ≈ 1.6180
TAU     = 1 / PHI                           # right probe ratio 1/φ ≈ 0.6180
TAU_INV = 1 - TAU                           # left probe ratio 1 - 1/φ ≈ 0.3820

print(f"Golden ratio phi      = {PHI:.6f}") # print golden ratio value
print(f"Right probe ratio tau = {TAU:.6f}") # print right probe ratio
print(f"Left probe ratio      = {TAU_INV:.6f}\n")  # print left probe ratio


# ─── Step 2: Set search parameters ───────────────────────────────────────────

a   = 0                                     # left bound of the interval
b   = 3                                     # right bound of the interval
eps = 0.5                                   # convergence tolerance


# ─── Step 3: Place the initial probe points ───────────────────────────────────

x1   = a + TAU_INV * (b - a)               # left probe at 0.3820 of interval
x2   = a + TAU     * (b - a)               # right probe at 0.6180 of interval
f_x1 = f(x1)                               # evaluate function at left probe
f_x2 = f(x2)                               # evaluate function at right probe

print(f"Initial probes:")                   # print header for initial probes
print(f"  x1 = {x1:.4f},  f(x1) = {f_x1:.4f}")  # print left probe values
print(f"  x2 = {x2:.4f},  f(x2) = {f_x2:.4f}\n") # print right probe values


# ─── Step 4: Initialize iteration storage ────────────────────────────────────

iterations = []                             # list to store iteration details
k          = 0                              # iteration counter


# ─── Step 5: Run the golden section loop ─────────────────────────────────────

while abs(b - a) > eps:                     # loop until interval is small enough
    iterations.append({'iter': k+1,         # save iteration number
                        'a': a, 'b': b,     # save current interval bounds
                        'x1': x1, 'x2': x2, # save probe positions
                        'f_x1': f_x1, 'f_x2': f_x2})  # save probe values

    if f_x1 < f_x2:                         # if left probe has smaller value
        b        = x2                       # shrink interval from right
        x2, f_x2 = x1, f_x1               # reuse left probe as new right probe
        x1       = a + TAU_INV * (b - a)   # compute new left probe only
        f_x1     = f(x1)                   # evaluate new left probe
    else:                                   # if right probe has smaller value
        a        = x1                       # shrink interval from left
        x1, f_x1 = x2, f_x2               # reuse right probe as new left probe
        x2       = a + TAU * (b - a)       # compute new right probe only
        f_x2     = f(x2)                   # evaluate new right probe

    k += 1                                  # increment iteration counter
    print(f"Iter {k:2d}: [{a:.4f}, {b:.4f}]  width={b-a:.4f}  "  # print interval
          f"x1={x1:.4f} f={f_x1:.4f}  x2={x2:.4f} f={f_x2:.4f}") # print probes


# ─── Step 6: Compute final minimum ───────────────────────────────────────────

xmin = (a + b) / 2                          # approximate minimum is center of final interval
print(f"\nApproximate minimum: x* = {xmin:.6f}")       # print approximate x*
print(f"f(x*)                    = {f(xmin):.6f}")     # print f at approximate minimum
print(f"Iterations               = {k}")               # print total iterations
print(f"Total function evaluations = {k + 1}")         # print total evaluations


# ─── Step 7: Full comparison table — all three methods ───────────────────────

ln_phi = math.log(PHI)                      # natural log of golden ratio
L      = b - a                              # interval length

print(f"\n{'Accuracy e':<14} {'Alternatives':<16} {'Bisection':<16} {'Golden Section'}") # header
print("-" * 62)                             # separator line

for e in [0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001]:  # loop over accuracy levels
    alt = int(L / e) + 1                    # evaluations for uniform scan
    bis = 2 * math.ceil(math.log2(L / e))  # evaluations for bisection
    gs  = math.ceil(math.log(L / e) / ln_phi) + 1  # evaluations for golden section
    print(f"{e:<14.4f} {alt:<16} {bis:<16} {gs}")  # print row
