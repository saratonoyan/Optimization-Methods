import numpy as np                          # import numpy for numerical operations
import matplotlib.pyplot as plt             # import matplotlib for plotting


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Set golden ratio constants and parameters ───────────────────────

PHI     = (1 + np.sqrt(5)) / 2             # golden ratio φ ≈ 1.6180
TAU     = 1 / PHI                           # right probe ratio ≈ 0.6180
TAU_INV = 1 - TAU                           # left probe ratio ≈ 0.3820

a   = 0                                     # left bound of the interval
b   = 3                                     # right bound of the interval
eps = 0.5                                   # convergence tolerance


# ─── Step 2: Place initial probe points ──────────────────────────────────────

x1   = a + TAU_INV * (b - a)               # left probe at 0.3820 of interval
x2   = a + TAU     * (b - a)               # right probe at 0.6180 of interval
f_x1 = f(x1)                               # evaluate function at left probe
f_x2 = f(x2)                               # evaluate function at right probe


# ─── Step 3: Run the golden section algorithm ────────────────────────────────

iterations = []                             # list to store all iteration data
k          = 0                              # iteration counter

while abs(b - a) > eps:                     # loop until interval is small enough
    iterations.append({'iter': k+1,         # save iteration number
                        'a': a, 'b': b,     # save current bounds
                        'x1': x1, 'x2': x2, # save probe positions
                        'f_x1': f_x1, 'f_x2': f_x2})  # save probe values

    if f_x1 < f_x2:                         # if left probe is smaller
        b        = x2                       # shrink from right
        x2, f_x2 = x1, f_x1               # reuse left probe as right
        x1       = a + TAU_INV * (b - a)   # compute new left probe
        f_x1     = f(x1)                   # evaluate new left probe
    else:                                   # if right probe is smaller
        a        = x1                       # shrink from left
        x1, f_x1 = x2, f_x2               # reuse right probe as left
        x2       = a + TAU * (b - a)       # compute new right probe
        f_x2     = f(x2)                   # evaluate new right probe
    k += 1                                  # increment counter

xmin = (a + b) / 2                          # final approximate minimum


# ─── Step 4: Prepare smooth curve ────────────────────────────────────────────

x_full = np.linspace(0, 3, 400)            # generate 400 points for smooth curve
y_full = f(x_full)                          # evaluate function on smooth curve


# ─── Step 5: Plot each iteration in a grid ───────────────────────────────────

n_iters = len(iterations)                  # total number of iterations
cols    = 2                                 # number of columns in the grid
rows    = (n_iters + 1) // cols            # compute number of rows needed

fig, axes = plt.subplots(rows, cols,        # create subplot grid
                          figsize=(14, rows * 5))  # set figure size
axes      = axes.flatten()                  # flatten axes array for easy indexing

for i, it in enumerate(iterations):        # loop over each iteration
    ax = axes[i]                            # get current subplot axis

    ax.plot(x_full, y_full,                 # plot smooth function curve
            color='steelblue',             # set color to steel blue
            linewidth=2,                   # set line thickness
            label='f(x)')                  # set legend label

    ax.scatter(it['x1'], it['f_x1'],        # plot left probe point
               color='crimson',            # set color to red
               s=100, zorder=5,            # set size and draw order
               label=f"x1={it['x1']:.3f}") # set legend label

    ax.scatter(it['x2'], it['f_x2'],        # plot right probe point
               color='dodgerblue',         # set color to blue
               s=100, zorder=5,            # set size and draw order
               label=f"x2={it['x2']:.3f}") # set legend label

    ax.axvline(it['a'],                     # draw left interval boundary
               color='seagreen',           # set color to green
               linewidth=1.5,             # set line thickness
               linestyle='--',            # set dashed style
               alpha=0.7)                 # set transparency

    ax.axvline(it['b'],                     # draw right interval boundary
               color='seagreen',           # set color to green
               linewidth=1.5,             # set line thickness
               linestyle='--',            # set dashed style
               alpha=0.7)                 # set transparency

    x_shade = np.linspace(it['a'], it['b'], 100)  # points inside current interval
    ax.fill_between(x_shade, f(x_shade),    # shade area under curve in interval
                    alpha=0.08,            # set low transparency
                    color='seagreen')      # set shade color to green

    ax.set_title(f"Iteration {it['iter']} | [{it['a']:.3f}, {it['b']:.3f}] | "  # set title
                 f"width={it['b']-it['a']:.4f}", fontsize=10)  # include interval width
    ax.set_xlim(0, 3)                       # fix x-axis range
    ax.set_xlabel('x')                      # set x-axis label
    ax.set_ylabel('f(x)')                   # set y-axis label
    ax.legend(fontsize=8)                   # show legend with small font
    ax.grid(True, alpha=0.3)               # show grid with low opacity


# ─── Step 6: Hide unused subplots ────────────────────────────────────────────

for j in range(n_iters, len(axes)):        # loop over unused subplot slots
    axes[j].set_visible(False)             # hide unused subplots


# ─── Step 7: Apply layout and save iteration plot ────────────────────────────

plt.suptitle('Golden Section Method — All Iterations',  # set overall title
             fontsize=14, y=1.01)          # set font size and position
plt.tight_layout()                         # adjust layout to prevent clipping
plt.savefig('golden_section_plot.png',     # save iteration plot as PNG
            dpi=150, bbox_inches='tight')  # set resolution and tight bounds
plt.show()                                 # display the plot
print("Plot saved as golden_section_plot.png")  # confirm save


# ─── Step 8: Plot convergence of interval width ───────────────────────────────

widths      = [it['b'] - it['a'] for it in iterations]  # extract interval widths
iter_nums   = list(range(1, len(widths) + 1))            # create iteration numbers
theoretical = [3.0 * (1/PHI)**(i-1) for i in iter_nums] # compute theoretical widths

fig2, axes2 = plt.subplots(1, 2, figsize=(12, 4))  # create two side-by-side plots


# ─── Step 9: Linear scale convergence plot ───────────────────────────────────

axes2[0].plot(iter_nums, widths,            # plot actual interval widths
              'o-', color='steelblue',     # set style to circles connected by line
              label='Actual')              # set legend label
axes2[0].plot(iter_nums, theoretical,       # plot theoretical interval widths
              's--', color='orange',       # set style to squares with dashed line
              label='Theoretical')         # set legend label
axes2[0].set_title('Interval Width — Linear Scale')  # set subplot title
axes2[0].set_xlabel('Iteration')            # set x-axis label
axes2[0].set_ylabel('Width')               # set y-axis label
axes2[0].legend()                          # show legend
axes2[0].grid(alpha=0.3)                   # show grid


# ─── Step 10: Log scale convergence plot ─────────────────────────────────────

axes2[1].semilogy(iter_nums, widths,        # plot actual widths on log scale
                  'o-', color='steelblue', # set style
                  label='Actual')          # set legend label
axes2[1].semilogy(iter_nums, theoretical,   # plot theoretical widths on log scale
                  's--', color='orange',   # set style
                  label='Theoretical')     # set legend label
axes2[1].set_title('Interval Width — Log Scale')  # set subplot title
axes2[1].set_xlabel('Iteration')            # set x-axis label
axes2[1].set_ylabel('Width (log)')         # set y-axis label
axes2[1].legend()                          # show legend
axes2[1].grid(alpha=0.3)                   # show grid


# ─── Step 11: Save and display convergence plot ───────────────────────────────

plt.tight_layout()                         # adjust layout
plt.savefig('golden_section_convergence.png', dpi=150)  # save convergence plot
plt.show()                                 # display the plot
print("Convergence plot saved as golden_section_convergence.png")  # confirm save
