# Golden Section Method

The most efficient classical one-dimensional optimization method. Places probe points at the **golden ratio** positions inside the interval — this allows one probe to be **reused** each iteration, so only one new function evaluation is needed per step after initialization.

---

## Files

| File | Description |
|---|---|
| `golden_section_method.ipynb` | Core algorithm + visualization + iteration table |
| `golden_section_plot.png` | Output plot |

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
| `φ` | 1.618034 | Golden ratio |
| `τ` | 0.618034 | Right probe ratio $= 1/\phi$ |
| `1-τ` | 0.381966 | Left probe ratio $= 1 - 1/\phi$ |

---

## How It Works

**Initialization** — place two probes at golden-ratio positions:
$$x_1 = a + 0.381966 \cdot (b - a), \qquad x_2 = a + 0.618034 \cdot (b - a)$$

**Repeat until** $|b - a| \leq \varepsilon$:

**If $f(x_1) < f(x_2)$:** minimum is in $[a, x_2]$
- Shrink right: $b \leftarrow x_2$
- Reuse: $x_2 \leftarrow x_1$ ← no new evaluation needed
- Compute only: $x_1 = a + 0.381966 \cdot (b - a)$

**If $f(x_1) \geq f(x_2)$:** minimum is in $[x_1, b]$
- Shrink left: $a \leftarrow x_1$
- Reuse: $x_1 \leftarrow x_2$ ← no new evaluation needed
- Compute only: $x_2 = a + 0.618034 \cdot (b - a)$

**Return:** $x^* = \dfrac{a + b}{2}$

---

## Results

| | x* | f(x*) |
|---|---|---|
| **Approximate (our result)** | 1.197561 | 1.368536 |
| **Exact (scipy)** | 1.080044 | 1.306296 |
| **Error in x** | 0.117517 | — |
| **Error in f(x)** | — | 0.062240 |

- Total iterations: **4**
- Function evaluations: **5** (2 for init + 1 per subsequent step)
- The method narrowed the interval in 4 steps and returned $x = 1.197561$ with $f(x) = 1.368536$.
- The true minimum is at $x = 1.080044$ with $f(x) = 1.306296$.

---

## Why the Golden Ratio?

It is the unique value satisfying the reuse condition:
$$\alpha^2 + \alpha - 1 = 0 \quad \Rightarrow \quad \alpha = \frac{1}{\phi} = 0.618034\ldots$$

Any other probe placement would fail the reuse condition.

---

## Convergence

Each iteration reduces the interval by factor $1/\phi \approx 0.618$:

| Iteration | Interval width |
|---|---|
| 0 | $3.0000$ |
| 1 | $1.8541$ |
| 2 | $1.1459$ |
| 3 | $0.7082$ |
| 4 | $0.4378$ |

---

## Strengths and Limitations

| ✅ Strengths | ❌ Limitations |
|---|---|
| Only 1 evaluation per step after init | Requires **unimodality** |
| Mathematically optimal probe placement | Slightly slower reduction than bisection |
| No derivatives needed | Not directly extendable to multivariate |

---

## How to Run
```bash
pip install numpy matplotlib scipy plotly
```
