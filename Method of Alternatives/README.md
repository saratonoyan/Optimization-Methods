# Method of Alternatives (Uniform Scanning)

The simplest one-dimensional optimization method. Divides the interval into equally spaced points, evaluates the function at every point, and returns the one with the lowest value.

---

## Files

| File | Description |
|---|---|
| `method_of_alternatives.ipynb` | Core algorithm + visualization + iteration table |
| `alternatives_plot.png` | Output plot |

---

## Objective Function

$$f(x) = \frac{1}{3}x^4 + 2x^2 - 6x + 5 \qquad x \in [0,\, 3]$$

---

## Parameters

| Parameter | Value | Description |
|---|---|---|
| `a` | 0 | Left bound of interval |
| `b` | 3 | Right bound of interval |
| `e` | 0.5 | Step size |
| `n` | 6 | Number of intervals → 7 sample points |

---

## How It Works

**Step 1** — Compute number of sample points:
$$n = \left\lfloor \frac{b - a}{\varepsilon} \right\rfloor \quad \Rightarrow \quad n + 1 \text{ total points}$$

**Step 2** — Generate equally spaced x-values:
$$x_i = a + i \cdot \varepsilon, \quad i = 0, 1, \ldots, n$$

**Step 3** — Evaluate the function at each point:
$$y_i = f(x_i)$$

**Step 4** — Return the point with the smallest value:
$$x^* \approx x_k \quad \text{where} \quad k = \arg\min_i \, y_i$$

**Accuracy:** result is guaranteed within $\pm\varepsilon$ of the true minimum.

---

## Results

| | x* | f(x*) |
|---|---|---|
| **Approximate (our result)** | 1.000000 | 1.333333 |
| **Exact (scipy)** | 1.080044 | 1.306296 |
| **Error in x** | 0.080044 | — |
| **Error in f(x)** | — | 0.027037 |

- Total iterations: **7**
- The method scanned all 7 equally spaced points and returned $x = 1.0$ as the best point with $f(x) = 1.333333$.
- The true minimum is at $x = 1.080044$ with $f(x) = 1.306296$ — the error is within the expected $\pm\varepsilon = \pm0.5$ range.

---

## Complexity

| Step size $\varepsilon$ | Points evaluated | Accuracy |
|---|---|---|
| 0.5 | 7 | ± 0.5 |
| 0.1 | 31 | ± 0.1 |
| 0.01 | 301 | ± 0.01 |

Halving $\varepsilon$ doubles the computation — $O(1/\varepsilon)$ complexity.

---

## Strengths and Limitations

| ✅ Strengths | ❌ Limitations |
|---|---|
| Simple to implement | Expensive for high accuracy |
| Works on any continuous function | Cannot exploit function structure |
| No assumptions about function shape | Only practical in 1D |

---

## How to Run
```bash
pip install numpy matplotlib scipy plotly
```
