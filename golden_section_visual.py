import numpy as np
import matplotlib.pyplot as plt


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):
    return (1/4)*x**4 + x**2 - 8*x + 12


# ─── Step 1: Set golden ratio constants and parameters ───────────────────────

PHI     = (1 + np.sqrt(5)) / 2
TAU     = 1 / PHI
TAU_INV = 1 - TAU

a   = 0
b   = 2
eps = 0.05


# ─── Step 2: Run the golden section algorithm ────────────────────────────────

x1   = a + TAU_INV * (b - a)
x2   = a + TAU     * (b - a)
f_x1 = f(x1)
f_x2 = f(x2)

iterations = []
k          = 0

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

xmin = (a + b) / 2


# ─── Step 3: Prepare smooth curve ────────────────────────────────────────────

x_full = np.linspace(0, 2, 400)
y_full = f(x_full)


# ─── Step 4: Plot each iteration in a grid ───────────────────────────────────

n_iters = len(iterations)
cols    = 2
rows    = (n_iters + 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(14, rows * 5))
axes      = axes.flatten()

for i, it in enumerate(iterations):
    ax = axes[i]

    ax.plot(x_full, y_full, color='steelblue', linewidth=2, label='f(x)')

    ax.scatter(it['x1'], it['f_x1'], color='crimson',    s=100, zorder=5,
               label=f"x1={it['x1']:.3f}")
    ax.scatter(it['x2'], it['f_x2'], color='dodgerblue', s=100, zorder=5,
               label=f"x2={it['x2']:.3f}")

    ax.axvline(it['a'], color='seagreen', linewidth=1.5, linestyle='--', alpha=0.7)
    ax.axvline(it['b'], color='seagreen', linewidth=1.5, linestyle='--', alpha=0.7)

    x_shade = np.linspace(it['a'], it['b'], 100)
    ax.fill_between(x_shade, f(x_shade), alpha=0.08, color='seagreen')

    ax.set_title(f"Iteration {it['iter']} | [{it['a']:.3f}, {it['b']:.3f}] | "
                 f"width={it['b']-it['a']:.4f}", fontsize=10)
    ax.set_xlim(0, 2)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)


# ─── Step 5: Hide any unused subplots ────────────────────────────────────────

for j in range(n_iters, len(axes)):
    axes[j].set_visible(False)


# ─── Step 6: Apply layout and save ───────────────────────────────────────────

plt.suptitle('Golden Section Method — All Iterations', fontsize=14, y=1.01)
plt.tight_layout()
plt.savefig('golden_section_plot.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot saved as golden_section_plot.png")


# ─── Step 7: Plot convergence of interval width ───────────────────────────────

widths      = [it['b'] - it['a'] for it in iterations]
iter_nums   = list(range(1, len(widths) + 1))
theoretical = [2.0 * (1/PHI)**(i-1) for i in iter_nums]

fig2, axes2 = plt.subplots(1, 2, figsize=(12, 4))

axes2[0].plot(iter_nums, widths,      'o-', color='steelblue', label='Actual')
axes2[0].plot(iter_nums, theoretical, 's--', color='orange',   label='Theoretical')
axes2[0].set_title('Interval Width — Linear Scale')
axes2[0].set_xlabel('Iteration')
axes2[0].set_ylabel('Width')
axes2[0].legend()
axes2[0].grid(alpha=0.3)

axes2[1].semilogy(iter_nums, widths,      'o-', color='steelblue', label='Actual')
axes2[1].semilogy(iter_nums, theoretical, 's--', color='orange',   label='Theoretical')
axes2[1].set_title('Interval Width — Log Scale')
axes2[1].set_xlabel('Iteration')
axes2[1].set_ylabel('Width (log)')
axes2[1].legend()
axes2[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('golden_section_convergence.png', dpi=150)
plt.show()
print("Convergence plot saved as golden_section_convergence.png")
