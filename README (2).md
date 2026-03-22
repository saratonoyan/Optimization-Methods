# Bisection Method (Section Division Method)

An interval-halving method for finding the minimum of a **unimodal** function. At each step it places two probe points near the midpoint, compares their values, and discards the half of the interval that cannot contain the minimum.

---

## Files

| File | Description |
|---|---|
| `bisection_method.py` | Core algorithm + comparison table |
| `bisection_visual.py` | Visualization — run this to generate the plot |
| `bisection_plot.png` | Output plot |

---

## How It Works

**Function:** $f(x) = \frac{1}{4}x^4 + x^2 - 8x + 12$ on $[0, 2]$

**Repeat until** $|b - a| \leq \varepsilon$:

**Step 1** — Compute the midpoint:
$$m = \frac{a + b}{2}$$

**Step 2** — Place two probes symmetric about $m$:
$$x_1 = m - \frac{d}{2}, \qquad x_2 = m + \frac{d}{2}$$

**Step 3** — Compare and eliminate:
- If $f(x_1) < f(x_2)$: set $b \leftarrow x_2$
- If $f(x_1) \geq f(x_2)$: set $a \leftarrow x_1$

**Return:** $x^* = \dfrac{a+b}{2}$

---

## Convergence

Each iteration reduces the interval by ~$\frac{1}{2}$:

| Iteration | Interval width |
|---|---|
| 0 | $b - a$ |
| 1 | $\approx \frac{b-a}{2}$ |
| k | $\approx \frac{b-a}{2^k}$ |

Complexity: $O(\log_2(1/\varepsilon))$ — far fewer evaluations than the Method of Alternatives.

---

## How to Run

```bash
pip install numpy matplotlib

# Run the algorithm
python bisection_method.py

# Generate the plot
python bisection_visual.py
```
