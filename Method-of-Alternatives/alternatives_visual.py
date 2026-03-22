import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return (1/4) * x**4 + x**2 - 8*x + 12


# ─── Step 1: Set parameters ───────────────────────────────────────────────────

a = 0
b = 2
e = 0.5


# ─── Step 2: Generate sample points ──────────────────────────────────────────

n   = int((b - a) / e)
l_x = [a + i * e for i in range(n + 1)]
l_y = [f(x) for x in l_x]


# ─── Step 3: Find approximate and exact minimum ───────────────────────────────

f_min       = min(l_y)
x_min       = l_x[l_y.index(f_min)]
result      = minimize(f, x0=1.5, bounds=[(0, 2)])
min_x_exact = result.x[0]
min_y_exact = result.fun


# ─── Step 4: Prepare smooth curve ────────────────────────────────────────────

x_vals = np.linspace(0, 2, 400)
y_vals = f(x_vals)


# ─── Step 5: Plot the function curve ─────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, y_vals, color='royalblue', linewidth=2.5,
        label='f(x) = ¼x⁴ + x² − 8x + 12')


# ─── Step 6: Plot the exact minimum ──────────────────────────────────────────

ax.scatter(min_x_exact, min_y_exact, color='crimson', s=160,
           marker='*', zorder=10,
           label=f'Exact minimum  x={min_x_exact:.4f}')


# ─── Step 7: Plot the sampled points ─────────────────────────────────────────

ax.scatter(l_x, l_y, color='seagreen', s=90, zorder=5,
           label=f'Sampled points (e = {e})')

for xi, yi in zip(l_x, l_y):
    ax.annotate(f'  ({xi}, {round(yi,2)})', (xi, yi), fontsize=8, color='#444')


# ─── Step 8: Apply layout and save ───────────────────────────────────────────

ax.set_title('Method of Alternatives — Uniform Scan on [0, 2]', fontsize=14, pad=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('alternatives_plot.png', dpi=150)
plt.show()
print("Plot saved as alternatives_plot.png")
