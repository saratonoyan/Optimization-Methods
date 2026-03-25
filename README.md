# Optimization Methods

This repository contains the implementation of three classical one-dimensional optimization methods used in numerical analysis and applied mathematics. Each method is implemented in Python with step-by-step code, detailed comments, and visualizations.

All three methods are applied to the same objective function on the same interval, making it straightforward to compare their behavior, efficiency, and accuracy directly.

---

## Objective Function

$$f(x) = \frac{1}{3}x^4 + 2x^2 - 6x + 5 \qquad [a, b] = [0,\, 3], \quad \varepsilon = 0.5, \quad n = 6, \quad \delta = 0.125$$

This function is continuous and unimodal on $[0, 3]$, meaning it has exactly one local minimum in this interval, which makes it suitable for all three methods.

---

## Repository Structure
```
Optimization-Methods/
│
├── Bisection-Method/
│   ├── bisection_method.py
│   ├── bisection_visual.py
│   ├── bisection_plot.png
│   └── README.md
│
├── Golden-Section-Method/
│   ├── golden_section_method.py
│   ├── golden_section_visual.py
│   ├── golden_section_plot.png
│   ├── golden_section_convergence.png
│   └── README.md
│
├── Method-of-Alternatives/
│   ├── method_of_alternatives.py
│   ├── alternatives_visual.py
│   ├── alternatives_plot.png
│   └── README.md
│
└── README.md
```

---

## Methods Overview

### 1. Method of Alternatives (Uniform Scanning)

The most fundamental optimization technique. Divides the search interval into equally spaced points and evaluates the objective function at every single point. The point that yields the smallest function value is reported as the approximate minimum. Requires no assumptions about the shape of the function beyond continuity.

**Algorithm:**
- Generate $n + 1$ points: $x_i = a + i \cdot \varepsilon$
- Evaluate $f(x_i)$ at every point
- Return $x^* = \arg\min_i f(x_i)$

**Convergence:** $O(1/\varepsilon)$ — linear. Halving the step size doubles the number of evaluations.

**Accuracy:** result is guaranteed within $\pm\varepsilon$ of the true minimum.

---

### 2. Bisection Method (Section Division Method)

A significant improvement over uniform scanning. Places two probe points near the midpoint of the current interval, compares their values, and eliminates the half that cannot contain the minimum. Relies on the unimodality of the function — because of unimodality, the probe with the larger function value is always on the far side of the minimum and can be safely discarded.

**Algorithm:**
- Place probes: $x_1 = m - d/2$, $x_2 = m + d/2$ where $m = (a+b)/2$
- If $f(x_1) < f(x_2)$: set $b \leftarrow x_2$
- Else: set $a \leftarrow x_1$
- Repeat until $|b - a| \leq \varepsilon$

**Convergence:** $O(\log_2(1/\varepsilon))$ — logarithmic. Each iteration uses exactly 2 function evaluations and reduces the interval by half.

---

### 3. Golden Section Method

The most refined of the three. Places probe points at positions determined by the golden ratio $\phi = (1 + \sqrt{5})/2 \approx 1.618$. This placement guarantees that one probe from the current iteration can always be reused in the next — requiring only one new function evaluation per step after initialization.

**Algorithm:**
- Place probes at: $x_1 = a + 0.3820(b-a)$, $x_2 = a + 0.6180(b-a)$
- If $f(x_1) < f(x_2)$: shrink right, reuse $x_1$ as new $x_2$, compute new $x_1$ only
- Else: shrink left, reuse $x_2$ as new $x_1$, compute new $x_2$ only
- Repeat until $|b - a| \leq \varepsilon$

**Convergence:** $O(\log_\phi(1/\varepsilon))$ — logarithmic. Interval reduces by factor $1/\phi \approx 0.618$ per step.

---

## Results

All three methods were applied to $f(x) = \frac{1}{3}x^4 + 2x^2 - 6x + 5$ on $[0, 3]$ with $\varepsilon = 0.5$.

The exact minimum computed by scipy is $x^* = 1.080044$, $f(x^*) = 1.306296$.

| Method | $x^*$ | $f(x^*)$ | Error in $x$ | Error in $f$ | Iterations | Function Evals |
|---|---|---|---|---|---|---|
| Exact minimum | 1.080044 | 1.306296 | — | — | — | — |
| Method of Alternatives | 1.000000 | 1.333333 | 0.080044 | 0.027037 | 7 | 7 |
| Bisection | 0.960938 | 1.365400 | 0.119107 | 0.059104 | 3 | 6 |
| Golden Section | 1.197561 | 1.368536 | 0.117517 | 0.062240 | 4 | 5 |

---

## Method Comparison

### Function evaluations needed for accuracy $\varepsilon$ on $[0, 3]$

| $\varepsilon$ | Method of Alternatives | Bisection | Golden Section |
|---|---|---|---|
| 0.5 | 7 | 6 | 5 |
| 0.1 | 31 | 10 | 11 |
| 0.01 | 301 | 16 | 18 |
| 0.001 | 3001 | 24 | 25 |
| 0.0001 | 30001 | 30 | 32 |

### Summary Table

| | Method of Alternatives | Bisection | Golden Section |
|---|---|---|---|
| Evaluations per step | 1 per point | 2 | 1 (after init) |
| Convergence rate | Linear | Logarithmic | Logarithmic |
| Requires unimodality | No | Yes | Yes |
| Requires derivatives | No | No | No |
| Implementation complexity | Very simple | Simple | Moderate |

---

## Which Method is Best and Why

Among the three methods, the **Golden Section Method is the most efficient** for minimizing a unimodal function on a closed interval.

The **Method of Alternatives**, while the simplest to understand and implement, is computationally the most expensive. Its linear convergence means that achieving high accuracy requires an impractically large number of function evaluations — at $\varepsilon = 0.0001$ it needs 30,001 evaluations on $[0, 3]$. It is only appropriate when the function has unknown structure or when a guaranteed global scan is required.

The **Bisection Method** achieves logarithmic convergence with just 2 evaluations per iteration, making it dramatically more efficient than uniform scanning. It is reliable, easy to implement, and converges predictably. However, it always requires two fresh function evaluations per step regardless of what was computed in the previous step — it discards information.

The **Golden Section Method** also achieves logarithmic convergence but exploits the mathematical properties of the golden ratio to reuse one evaluation per step. More importantly, it is **mathematically optimal** for this class of problems — it has been proven that no derivative-free interval search method can achieve a better reduction ratio per function evaluation than $1/\phi$. This means it is not just practically efficient — it is theoretically the best possible approach under these constraints.

**In conclusion:** if the function is known to be unimodal and no derivative information is available, the Golden Section Method is the recommended choice. If the function's unimodality cannot be guaranteed, the Method of Alternatives should be used as a safe fallback.

---

## Conclusion

This study implemented and compared three classical one-dimensional optimization methods applied to the function f(x) = 1/3·x⁴ + 2x² - 6x + 5 on the interval [0, 3] with parameters ε = 0.5, n = 6, and δ = 0.125. The exact minimum computed as a reference was x* = 1.080044 with f(x*) = 1.306296.

Among the three methods, the Method of Alternatives produced the closest result to the exact minimum, returning x* = 1.000000 and f(x*) = 1.333333 with an error of 0.080044 in x and 0.027037 in f(x). However this accuracy is not due to the method being superior — it is simply because one of its seven equally spaced sample points happened to land close to the true minimum at x = 1.0. With a different function or a finer required accuracy the method would need significantly more evaluations and would fall far behind the other two methods.

The Bisection Method converged in the fewest iterations — only 3 — but required 2 function evaluations per iteration, bringing its total to 6. It returned x* = 0.960938 and f(x*) = 1.365400 with an error of 0.119107 in x. The method is reliable and straightforward to implement, making it a practical choice when the function is known to be unimodal and moderate efficiency is acceptable.

The Golden Section Method required 4 iterations but only 5 function evaluations in total — fewer than both other methods — because it reuses one probe point at every step after initialization. It returned x* = 1.197561 and f(x*) = 1.368536 with an error of 0.117517 in x. While its result was not the closest to the exact minimum in this specific case, the Golden Section Method is mathematically proven to be the optimal derivative-free interval search method. No other method of this type can achieve a better reduction ratio per function evaluation than 1/φ ≈ 0.618.

In terms of implementation difficulty, the Method of Alternatives was the simplest — it is nothing more than a loop over equally spaced points. The Bisection Method required more careful thinking about the probe placement and interval shrinking logic. The Golden Section Method was the most difficult to implement correctly due to the reuse logic, where one probe from the current iteration must be carried over to the next step without a new function evaluation.

Overall, for problems where the function is unimodal and no derivative information is available, the Golden Section Method is the recommended approach — especially when function evaluations are expensive. If the function's unimodality cannot be guaranteed, the Method of Alternatives should be used as a safe and simple fallback. The Bisection Method sits between the two — more efficient than uniform scanning but simpler to implement than the Golden Section.

---

## Dependencies

| Package | Purpose |
|---|---|
| `numpy` | Numerical computation |
| `matplotlib` | Plots and visualizations |
| `scipy` | Reference minimum for accuracy validation |
```bash
pip install numpy matplotlib scipy
```

---

## How to Run
```bash
# Method of Alternatives
cd Method-of-Alternatives
python method_of_alternatives.py
python alternatives_visual.py

# Bisection Method
cd Bisection-Method
python bisection_method.py
python bisection_visual.py

# Golden Section Method
cd Golden-Section-Method
python golden_section_method.py
python golden_section_visual.py
```

---

## References

- Simonyan S.H., Machine Learning: Optimization Problems and Methods. учебный manual / S.H. Simonyan; National Polytechnic University of Armenia (NPUA). – Yerevan: Chartaraget, 2024
- Simonyan S.H., Avetisyan A.G., Subgradient Methods, Monograph / State Engineering University of Armenia. Yerevan: Author’s publication, 2005
