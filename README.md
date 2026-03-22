# Optimization Methods

Implementation of three classical one-dimensional optimization methods, each in its own folder with algorithm, visualization, and documentation.

---

## Methods

| Folder | Method | Complexity |
|---|---|---|
| `Method-of-Alternatives/` | Uniform Scanning | $O(1/\varepsilon)$ |
| `Bisection-Method/` | Section Division | $O(\log_2(1/\varepsilon))$ |
| `Golden-Section-Method/` | Golden Section | $O(\log_\phi(1/\varepsilon))$ |

All three methods minimize the same function:

$$f(x) = \frac{1}{4}x^4 + x^2 - 8x + 12 \quad \text{on} \quad [0,\, 2]$$

---

## Repository Structure

```
Optimization-Methods/
│
├── README.md
│
├── Method-of-Alternatives/
│   ├── method_of_alternatives.py
│   ├── alternatives_visual.py
│   ├── alternatives_plot.png
│   └── README.md
│
├── Bisection-Method/
│   ├── bisection_method.py
│   ├── bisection_visual.py
│   ├── bisection_plot.png
│   └── README.md
│
└── Golden-Section-Method/
    ├── golden_section_method.py
    ├── golden_section_visual.py
    ├── golden_section_plot.png
    ├── golden_section_convergence.png
    └── README.md
```

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
