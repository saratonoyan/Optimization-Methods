import numpy as np
import math


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return (1/4)*x**4 + x**2 - 8*x + 12


# ─── Step 1: Define golden ratio constants ────────────────────────────────────

PHI     = (1 + np.sqrt(5)) / 2   # ≈ 1.6180
TAU     = 1 / PHI                 # ≈ 0.6180  right probe position
TAU_INV = 1 - TAU                 # ≈ 0.3820  left probe position

print(f"Golden ratio phi      = {PHI:.6f}")
print(f"Right probe ratio tau = {TAU:.6f}")
print(f"Left probe ratio      = {TAU_INV:.6f}\n")


# ─── Step 2: Set search parameters ───────────────────────────────────────────

a   = 0
b   = 2
eps = 0.05


# ─── Step 3: Place the initial probe points ───────────────────────────────────

x1   = a + TAU_INV * (b - a)
x2   = a + TAU     * (b - a)
f_x1 = f(x1)
f_x2 = f(x2)

print(f"Initial probes:")
print(f"  x1 = {x1:.4f},  f(x1) = {f_x1:.4f}")
print(f"  x2 = {x2:.4f},  f(x2) = {f_x2:.4f}\n")


# ─── Step 4: Initialize iteration storage ────────────────────────────────────

iterations = []
k          = 0


# ─── Step 5: Run the golden section loop ─────────────────────────────────────

while abs(b - a) > eps:
    iterations.append({'iter': k+1, 'a': a, 'b': b,
                        'x1': x1, 'x2': x2, 'f_x1': f_x1, 'f_x2': f_x2})

    if f_x1 < f_x2:
        b        = x2
        x2, f_x2 = x1, f_x1
        x1       = a + TAU_INV * (b - a)
        f_x1     = f(x1)
    else:
        a        = x1
        x1, f_x1 = x2, f_x2
        x2       = a + TAU * (b - a)
        f_x2     = f(x2)

    k += 1
    print(f"Iter {k:2d}: [{a:.4f}, {b:.4f}]  width={b-a:.4f}  "
          f"x1={x1:.4f} f={f_x1:.4f}  x2={x2:.4f} f={f_x2:.4f}")


# ─── Step 6: Compute final minimum ───────────────────────────────────────────

xmin = (a + b) / 2

print(f"\nApproximate minimum: x* = {xmin:.6f}")
print(f"f(x*)      = {f(xmin):.6f}")
print(f"Iterations = {k}")
print(f"Total function evaluations = {k + 1}")


# ─── Step 7: Full comparison table — all three methods ───────────────────────

ln_phi = math.log(PHI)
L      = 2.0

print(f"\n{'Accuracy e':<14} {'Alternatives':<16} {'Bisection':<16} {'Golden Section'}")
print("-" * 62)

for e in [0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001]:
    alt = int(L / e) + 1
    bis = 2 * math.ceil(math.log2(L / e))
    gs  = math.ceil(math.log(L / e) / ln_phi) + 1
    print(f"{e:<14.4f} {alt:<16} {bis:<16} {gs}")
