# Bisection Method (Section Division Method)

An interval-halving method for finding the minimum of a **unimodal** function. At each step it places two probe points near the midpoint, compares their values, and discards the half of the interval that cannot contain the minimum.

---

## Files

| File | Description |
|---|---|
| `bisection_method.ipynb` | Core algorithm + visualization + iteration table |
| `bisection_plot.png` | Output plot |

---

## Objective Function

$$f(x) = \frac{1}{3}x^4 + 2x^2 - 6x + 5 \qquad x \in [0,\, 3]$$

---

## Parameters

| Parameter | Value | Description |
|---|---|---|
| `a` | 0 | Left bound of interval |
| `b` | 3 | Right bound of interval |
| `eps` | 0.5 | Convergence tolerance |
| `d` | 0.125 | Probe offset — must satisfy $0 < d < \varepsilon$ |

---

## How It Works

**Repeat until** $|b - a| \leq \varepsilon$:

**Step 1** — Compute the midpoint:
$$m = \frac{a + b}{2}$$

**Step 2** — Place two probes symmetric about $m$:
$$x_1 = m - \frac{d}{2}, \qquad x_2 = m + \frac{d}{2}$$

**Step 3** — Compare and eliminate:
- If $f(x_1) < f(x_2)$: minimum is in $[a, x_2]$ → set $b \leftarrow x_2$
- If $f(x_1) \geq f(x_2)$: minimum is in $[x_1, b]$ → set $a \leftarrow x_1$

**Return:** $x^* = \dfrac{a + b}{2}$

---

## Results

| | x* | f(x*) |
|---|---|---|
| **Approximate (our result)** | 0.960938 | 1.365400 |
| **Exact (scipy)** | 1.080044 | 1.306296 |
| **Error in x** | 0.119107 | — |
| **Error in f(x)** | — | 0.059104 |

- Total iterations: **3**
- Function evaluations: **6** (2 per iteration)
- The method narrowed the interval in 3 steps and returned $x = 0.960938$ with $f(x) = 1.365400$.
- The true minimum is at $x = 1.080044$ with $f(x) = 1.306296$.

---

## Convergence

Each iteration reduces the interval by approximately $\frac{1}{2}$:

| Iteration | Interval width |
|---|---|
| 0 | $3.0000$ |
| 1 | $1.5625$ |
| 2 | $0.8438$ |
| 3 | $0.4844$ |

Complexity: $O(\log_2(1/\varepsilon))$ — far fewer evaluations than the Method of Alternatives.

---

## Strengths and Limitations

| ✅ Strengths | ❌ Limitations |
|---|---|
| Logarithmic convergence | Requires **unimodality** |
| Only 2 evaluations per step | Does not use derivative info |
| Guaranteed convergence | Not directly extendable to multivariate |

---

## How to Run
```bash
pip install numpy matplotlib scipy plotly
```
