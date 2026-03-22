import numpy as np
import matplotlib.pyplot as plt


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return 0.25 * x**4 + x**2 - 8*x + 12


# ─── Step 1: Set parameters and run bisection ─────────────────────────────────

a   = 0
b   = 2
eps = 0.2
d   = 0.1

iteration_midpoints = []
intervals           = []

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

xmin = (a + b) / 2


# ─── Step 2: Prepare smooth curve ────────────────────────────────────────────

x_vals = np.linspace(-0.5, 2.5, 500)
y_vals = f(x_vals)


# ─── Step 3: Create figure ────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 6))


# ─── Step 4: Plot the function curve ─────────────────────────────────────────

ax.plot(x_vals, y_vals, color='steelblue', linewidth=2.5, label='f(x)')


# ─── Step 5: Shade the final uncertainty interval ────────────────────────────

final_a, final_b = intervals[-1]
x_shade = np.linspace(final_a, final_b, 100)
ax.fill_between(x_shade, f(x_shade), alpha=0.12, color='orange',
                label=f'Final interval [{final_a:.3f}, {final_b:.3f}]')


# ─── Step 6: Plot the iteration midpoints ─────────────────────────────────────

colors = plt.cm.YlOrRd(np.linspace(0.35, 0.9, len(iteration_midpoints)))

for i, (m, c) in enumerate(zip(iteration_midpoints, colors)):
    ax.scatter(m, f(m), color=c, s=80, zorder=5)
    ax.annotate(f'  m{i+1}', (m, f(m)), fontsize=9, color='#555')


# ─── Step 7: Draw interval boundary lines ────────────────────────────────────

for (ia, ib) in intervals:
    ax.axvline(ia, color='gray', linewidth=0.6, linestyle='--', alpha=0.5)
    ax.axvline(ib, color='gray', linewidth=0.6, linestyle='--', alpha=0.5)


# ─── Step 8: Mark the final minimum ──────────────────────────────────────────

ax.scatter(xmin, f(xmin), color='crimson', s=160, marker='*', zorder=10,
           label=f'x* = {xmin:.4f}')


# ─── Step 9: Apply layout and save ───────────────────────────────────────────

ax.set_title('Bisection Method — Interval Narrowing', fontsize=14, pad=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('bisection_plot.png', dpi=150)
plt.show()
print("Plot saved as bisection_plot.png")
