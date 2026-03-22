# Optimization Methods

Implementation of three classical one-dimensional optimization methods, each in its own folder with algorithm, visualization, and documentation.

---

## Objective Function

All three methods minimize the same function:

$$f(x) = \frac{1}{3}x^4 + 2x^2 - 6x + 5 \qquad \text{on} \qquad [a, b] = [0,\, 3]$$

With parameters: $\varepsilon = 0.5$, $n = 6$, $\delta = 0.125$

---

## Methods

| Folder | Method | Evaluations per step | Complexity |
|---|---|---|---|
| `Method-of-Alternatives/` | Uniform Scanning | 1 per point | $O(1/\varepsilon)$ |
| `Bisection-Method/` | Section Division | 2 | $O(\log_2(1/\varepsilon))$ |
| `Golden-Section-Method/` | Golden Section | 1 (after init) | $O(\log_\phi(1/\varepsilon))$ |

---

## Repository Structure

```
Optimization-Methods/
│
├── README.md
│
├── Method-of-Alternatives/
│   ├── README.md
│   ├── method_of_alternatives.py
│   ├── alternatives_visual.py
│   └── alternatives_plot.png
│
├── Bisection-Method/
│   ├── README.md
│   ├── bisection_method.py
│   ├── bisection_visual.py
│   └── bisection_plot.png
│
└── Golden-Section-Method/
    ├── README.md
    ├── golden_section_method.py
    ├── golden_section_visual.py
    ├── golden_section_plot.png
    └── golden_section_convergence.png
```

---

## Comparison: Evaluations Needed

For accuracy $\varepsilon$ on $[0, 3]$:

| $\varepsilon$ | Alternatives | Bisection | Golden Section |
|---|---|---|---|
| 0.5 | 7 | 4 | 5 |
| 0.1 | 31 | 10 | 11 |
| 0.01 | 301 | 16 | 18 |
| 0.001 | 3001 | 24 | 25 |

---

## How to Run

```bash
pip install numpy matplotlib scipy

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

## Dependencies

| Package | Purpose |
|---|---|
| `numpy` | Numerical computation |
| `matplotlib` | Plots and visualizations |
| `scipy` | Reference minimum (Method of Alternatives only) |
