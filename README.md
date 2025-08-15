# Numerical Analysis Methods

A collection of numerical analysis algorithms implemented in Python, based on topics taught in Numerical Analysis Course taught at IISER Pune by Prof Prafullkumar Tale.  
This repository serves both as a study resource and a reference for common computational methods used to approximate solutions for mathematical problems.

---

## Overview

Numerical analysis focuses on designing algorithms for approximating solutions to problems that cannot be solved analytically or are too complex for exact computation.  
This repository contains clean, well-documented implementations of these methods along with example usages.

The goal of this project is:
- To reinforce theoretical understanding with practical coding examples.
- To create a reusable collection of algorithms for future assignments, projects, and research.

---

## Implemented Methods

- **Roots of Non-Linear Eqns**
  - [x] Bisection Method
  - [x] Newton-Raphson Method
  - [x] Secant Method
- **Interpolation**
  - [ ] Lagrange Interpolation
  - [ ] Newton’s Divided Difference
- **Numerical Integration**
  - [ ] Trapezoidal Rule
  - [ ] Simpson’s Rule
- **Differential Equations**
  - [ ] Euler’s Method
  - [ ] Runge–Kutta Methods

*(More methods will be added as the course progresses.)*

---

## Example Usage

### Bisection Method
```python
from bisection_method import bisection_method

# Example function
def f(x):
    return x**2 - 4

# Create the solver instance
root_finder = bisection_method(f, a=1, b=3, hor_tol=1e-5, ver_tol=1e-5, max_iter=100)

# Find the root
root = root_finder()
print("Estimated Root:", root)
