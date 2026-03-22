import numpy as np                          # import numpy for numerical operations
import matplotlib.pyplot as plt             # import matplotlib for plotting
from scipy.optimize import minimize         # import minimize for exact reference solution


# ─── Objective function ───────────────────────────────────────────────────────

def f(x):                                   # define the objective function
    return (1/3) * x**4 + 2*x**2 - 6*x + 5 # f(x) = 1/3*x^4 + 2x^2 - 6x + 5


# ─── Step 1: Set parameters ───────────────────────────────────────────────────

a = 0                                       # left bound of the interval
b = 3                                       # right bound of the interval
e = 0.5                                     # step size


# ─── Step 2: Generate sample points ──────────────────────────────────────────

n   = int((b - a) / e)                      # compute number of intervals
l_x = [a + i * e for i in range(n + 1)]    # generate equally spaced x-values
l_y = [f(x) for x in l_x]                  # evaluate function at each sample point


# ─── Step 3: Find approximate and exact minimum ───────────────────────────────

f_min       = min(l_y)                      # find the minimum f(x) value
x_min       = l_x[l_y.index(f_min)]        # find the x corresponding to minimum
result      = minimize(f, x0=1.5, bounds=[(0, 3)])  # compute exact minimum with scipy
min_x_exact = result.x[0]                  # extract exact x*
min_y_exact = result.fun                   # extract exact f(x*)


# ─── Step 4: Prepare smooth curve ────────────────────────────────────────────

x_vals = np.linspace(0, 3, 400)            # generate 400 points for smooth curve
y_vals = f(x_vals)                          # evaluate function on smooth curve


# ─── Step 5: Create the figure ───────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 6))    # create figure with size 10x6


# ─── Step 6: Plot the function curve ─────────────────────────────────────────

ax.plot(x_vals, y_vals,                    # plot the smooth function curve
        color='royalblue',                 # set line color to royal blue
        linewidth=2.5,                     # set line thickness
        label='f(x) = 1/3·x⁴ + 2x² − 6x + 5')  # set legend label


# ─── Step 7: Plot the exact minimum ──────────────────────────────────────────

ax.scatter(min_x_exact, min_y_exact,       # plot exact minimum point
           color='crimson',                # set marker color to red
           s=160,                          # set marker size
           marker='*',                     # set marker shape to star
           zorder=10,                      # draw on top of other elements
           label=f'Exact minimum  x={min_x_exact:.4f}')  # set legend label


# ─── Step 8: Plot the sampled points ─────────────────────────────────────────

ax.scatter(l_x, l_y,                       # plot all sampled points
           color='seagreen',               # set marker color to green
           s=90,                           # set marker size
           zorder=5,                       # draw above curve but below minimum
           label=f'Sampled points (e = {e})')  # set legend label


# ─── Step 9: Annotate each sampled point ─────────────────────────────────────

for xi, yi in zip(l_x, l_y):              # loop over each sample point
    ax.annotate(f'  ({xi}, {round(yi,2)})',  # annotation text with coordinates
                (xi, yi),                  # position at the point
                fontsize=8,                # set font size
                color='#444')             # set text color to dark gray


# ─── Step 10: Apply layout settings ──────────────────────────────────────────

ax.set_title('Method of Alternatives — Uniform Scan on [0, 3]',  # set plot title
             fontsize=14, pad=14)          # set font size and padding
ax.set_xlabel('x', fontsize=12)            # set x-axis label
ax.set_ylabel('f(x)', fontsize=12)         # set y-axis label
ax.legend(fontsize=10)                     # show legend with font size 10
ax.grid(True, alpha=0.3)                   # show grid with 30% opacity
plt.tight_layout()                         # adjust layout to prevent clipping


# ─── Step 11: Save and display the plot ──────────────────────────────────────

plt.savefig('alternatives_plot.png', dpi=150)  # save plot as PNG with 150 DPI
plt.show()                                 # display the plot on screen
print("Plot saved as alternatives_plot.png")   # confirm file was saved
