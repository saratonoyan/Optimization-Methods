# Golden Section Method

The most efficient classical one-dimensional optimization method. Places probe points at the **golden ratio** positions inside the interval — this allows one probe to be **reused** each iteration, so only one new function evaluation is needed per step after initialization.

---

## Files

| File | Description |
|---|---|
| `golden_section_method.py` | Core algorithm + full comparison table |
| `golden_section_visual.py` | Visualization — run this to generate the plots |
| `golden_section_plot.png` | Per-iteration plots |
| `golden_section_convergence.png` | Interval width convergence chart |

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
| `φ` | 1.6180 | Golden ratio |
| `τ` | 0.6180 | Right probe ratio $= 1/\phi$ |
| `1-τ` | 0.3820 | Left probe ratio $= 1 - 1/\phi$ |

---

## How It Works

**Initialization** — place two probes at golden-ratio positions:
$$x_1 = a + 0.3820 \cdot (b - a), \qquad x_2 = a + 0.6180 \cdot (b - a)$$

**Repeat until** $|b - a| \leq \varepsilon$:

**If $f(x_1) < f(x_2)$:** minimum is in $[a, x_2]$
- Shrink right: $b \leftarrow x_2$
- Reuse: $x_2 \leftarrow x_1$ ← no new evaluation needed
- Compute only: $x_1 = a + 0.3820 \cdot (b - a)$

**If $f(x_1) \geq f(x_2)$:** minimum is in $[x_1, b]$
- Shrink left: $a \leftarrow x_1$
- Reuse: $x_1 \leftarrow x_2$ ← no new evaluation needed
- Compute only: $x_2 = a + 0.6180 \cdot (b - a)$

**Return:** $x^* = \dfrac{a + b}{2}$

---

## Why the Golden Ratio?

It is the unique value satisfying the reuse condition:
$$\alpha^2 + \alpha - 1 = 0 \quad \Rightarrow \quad \alpha = \frac{1}{\phi} = 0.6180\ldots$$

Any other probe placement would fail the reuse condition.

---

## Convergence

Each iteration reduces the interval by factor $1/\phi \approx 0.618$:

| Iteration | Interval width |
|---|---|
| 0 | $b - a = 3$ |
| 1 | $\approx 1.854$ |
| 2 | $\approx 1.146$ |
| k | $\approx 3 \cdot (1/\phi)^k$ |

---

## Full Comparison: All Three Methods

Evaluations needed for accuracy $\varepsilon$ on $[0, 3]$:

| $\varepsilon$ | Alternatives | Bisection | Golden Section |
|---|---|---|---|
| 0.5 | 7 | 4 | 5 |
| 0.1 | 31 | 10 | 11 |
| 0.01 | 301 | 16 | 18 |
| 0.001 | 3001 | 24 | 25 |

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
pip install numpy matplotlib

# Run the algorithm
python golden_section_method.py

# Generate the plots
python golden_section_visual.py
```
