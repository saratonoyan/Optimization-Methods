import numpy as np                          # import numpy for numerical operations
import matplotlib.pyplot as plt             # import matplotlib for plotting


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Set parameters ───────────────────────────────────────────────────

a   = 0                                     # left bound of the interval
b   = 3                                     # right bound of the interval
eps = 0.5                                   # convergence tolerance
d   = 0.125                                 # probe offset


# ─── Step 2: Initialize storage ──────────────────────────────────────────────

iteration_midpoints = []                    # list to store midpoints
intervals           = []                    # list to store interval bounds


# ─── Step 3: Run the bisection algorithm ─────────────────────────────────────

while abs(b - a) > eps:                     # loop until interval is small enough
    intervals.append((a, b))               # record current interval
    midpoint = (a + b) / 2                 # compute midpoint
    iteration_midpoints.append(midpoint)   # record midpoint

    x1 = (a + b - d) / 2                   # compute left probe point
    x2 = (a + b + d) / 2                   # compute right probe point

    if f(x1) < f(x2):                      # compare function values at probes
        b = x2                             # shrink interval from right
    else:                                  # otherwise
        a = x1                             # shrink interval from left

xmin = (a + b) / 2                         # final approximate minimum


# ─── Step 4: Prepare smooth curve ────────────────────────────────────────────

x_vals = np.linspace(-0.5, 3.5, 500)       # generate points for smooth curve
y_vals = f(x_vals)                          # evaluate function on smooth curve


# ─── Step 5: Create the figure ───────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 6))    # create figure with size 10x6


# ─── Step 6: Plot the function curve ─────────────────────────────────────────

ax.plot(x_vals, y_vals,                    # plot the smooth function curve
        color='steelblue',                 # set color to steel blue
        linewidth=2.5,                     # set line thickness
        label='f(x)')                      # set legend label


# ─── Step 7: Shade the final uncertainty interval ────────────────────────────

final_a, final_b = intervals[-1]           # get the last recorded interval bounds
x_shade = np.linspace(final_a, final_b, 100)  # generate points inside final interval
ax.fill_between(x_shade, f(x_shade),       # shade the area under the curve
                alpha=0.12,                # set transparency
                color='orange',            # set shade color to orange
                label=f'Final interval [{final_a:.3f}, {final_b:.3f}]')  # legend label


# ─── Step 8: Plot the iteration midpoints ────────────────────────────────────

colors = plt.cm.YlOrRd(                    # create color gradient from yellow to red
    np.linspace(0.35, 0.9, len(iteration_midpoints)))  # one color per iteration

for i, (m, c) in enumerate(zip(iteration_midpoints, colors)):  # loop over midpoints
    ax.scatter(m, f(m), color=c, s=80, zorder=5)               # plot midpoint marker
    ax.annotate(f'  m{i+1}', (m, f(m)), fontsize=9, color='#555')  # label the point


# ─── Step 9: Draw interval boundary lines ────────────────────────────────────

for (ia, ib) in intervals:                 # loop over all recorded intervals
    ax.axvline(ia,                         # draw vertical line at left bound
               color='gray',              # set color to gray
               linewidth=0.6,             # set thin line width
               linestyle='--',            # set dashed style
               alpha=0.5)                 # set transparency
    ax.axvline(ib,                         # draw vertical line at right bound
               color='gray',              # set color to gray
               linewidth=0.6,             # set thin line width
               linestyle='--',            # set dashed style
               alpha=0.5)                 # set transparency


# ─── Step 10: Mark the final minimum ─────────────────────────────────────────

ax.scatter(xmin, f(xmin),                  # plot the final minimum point
           color='crimson',               # set color to red
           s=160,                         # set marker size
           marker='*',                    # set star marker shape
           zorder=10,                     # draw on top of everything
           label=f'x* = {xmin:.4f}')     # set legend label


# ─── Step 11: Apply layout settings ──────────────────────────────────────────

ax.set_title('Bisection Method — Interval Narrowing',  # set plot title
             fontsize=14, pad=14)          # set font size and padding
ax.set_xlabel('x', fontsize=12)            # set x-axis label
ax.set_ylabel('f(x)', fontsize=12)         # set y-axis label
ax.legend(fontsize=10)                     # show legend
ax.grid(True, alpha=0.3)                   # show grid with 30% opacity
plt.tight_layout()                         # adjust layout


# ─── Step 12: Save and display the plot ──────────────────────────────────────

plt.savefig('bisection_plot.png', dpi=150) # save plot as PNG with 150 DPI
plt.show()                                 # display the plot on screen
print("Plot saved as bisection_plot.png")  # confirm file was saved
