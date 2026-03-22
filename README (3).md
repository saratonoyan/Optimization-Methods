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

## How It Works

**Function:** $f(x) = \frac{1}{4}x^4 + x^2 - 8x + 12$ on $[0, 2]$

**Golden ratio constants:**
$$\phi = \frac{1+\sqrt{5}}{2} \approx 1.618, \qquad \frac{1}{\phi} \approx 0.6180, \qquad 1 - \frac{1}{\phi} \approx 0.3820$$

**Initialization** — place two probes at golden-ratio positions:
$$x_1 = a + 0.3820 \cdot (b-a), \qquad x_2 = a + 0.6180 \cdot (b-a)$$

**Repeat until** $|b - a| \leq \varepsilon$:

**If $f(x_1) < f(x_2)$:**
- Shrink right: $b \leftarrow x_2$
- Reuse: $x_2 \leftarrow x_1$ ← no new evaluation
- Compute new: $x_1 = a + 0.3820 \cdot (b-a)$

**If $f(x_1) \geq f(x_2)$:**
- Shrink left: $a \leftarrow x_1$
- Reuse: $x_1 \leftarrow x_2$ ← no new evaluation
- Compute new: $x_2 = a + 0.6180 \cdot (b-a)$

**Return:** $x^* = \dfrac{a+b}{2}$

---

## Convergence

Each iteration reduces the interval by factor $1/\phi \approx 0.618$:

| Iteration | Interval width |
|---|---|
| 0 | $b - a$ |
| 1 | $\approx 0.618 \cdot (b-a)$ |
| k | $\approx (1/\phi)^k \cdot (b-a)$ |

---

## Comparison: All Three Methods

Evaluations needed for accuracy $\varepsilon$ on $[0, 2]$:

| $\varepsilon$ | Alternatives | Bisection | Golden Section |
|---|---|---|---|
| 0.1 | 21 | 8 | 9 |
| 0.01 | 201 | 14 | 16 |
| 0.001 | 2001 | 22 | 23 |

---

## How to Run

```bash
pip install numpy matplotlib

# Run the algorithm
python golden_section_method.py

# Generate the plots
python golden_section_visual.py
```
