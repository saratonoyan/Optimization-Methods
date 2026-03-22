# Method of Alternatives (Uniform Scanning)

The simplest one-dimensional optimization method. Divides the interval into equally spaced points, evaluates the function at every point, and returns the one with the lowest value.

---

## Files

| File | Description |
|---|---|
| `method_of_alternatives.py` | Core algorithm + accuracy vs. cost table |
| `alternatives_visual.py` | Visualization — run this to generate the plot |
| `alternatives_plot.png` | Output plot |

---

## How It Works

**Function:** $f(x) = \frac{1}{4}x^4 + x^2 - 8x + 12$ on $[0, 2]$

**Step 1** — Compute number of sample points:
$$n = \left\lfloor \frac{b - a}{\varepsilon} \right\rfloor$$

**Step 2** — Generate equally spaced x-values:
$$x_i = a + i \cdot \varepsilon, \quad i = 0, 1, \ldots, n$$

**Step 3** — Evaluate the function at each point:
$$y_i = f(x_i)$$

**Step 4** — Return the point with the smallest value:
$$x^* \approx x_k \quad \text{where} \quad k = \arg\min_i \, y_i$$

---

## Complexity

| Step size $\varepsilon$ | Points evaluated | Accuracy |
|---|---|---|
| 0.5 | 5 | ± 0.5 |
| 0.1 | 21 | ± 0.1 |
| 0.01 | 201 | ± 0.01 |

Halving $\varepsilon$ doubles the computation — $O(1/\varepsilon)$ complexity.

---

## How to Run

```bash
pip install numpy matplotlib scipy

# Run the algorithm
python method_of_alternatives.py

# Generate the plot
python alternatives_visual.py
```
