#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Root Finder for Arbitrary-Degree Polynomials
Implements Newton-Raphson method using Horner’s scheme.
No external modules used.

"""

# Evaluate both P(x) and P'(x) using Horner's method
def horner(poly, x):
    """
    Evaluates a polynomial and its derivative at x using Horner's method.
    :param poly: List of polynomial coefficients [a0, a1, ..., an]
    :param x: Value at which to evaluate
    :return: Tuple (P(x), P'(x))
    """
    n = len(poly)
    b = poly[0]  # P(x)
    c = poly[0]  # P'(x)

    for i in range(1, n):
        b = b * x + poly[i]
        if i < n - 1:
            c = c * x + b

    return b, c

# Use Newton-Raphson method to find a single root
def newton_raphson(poly, x0, tol=1e-10, max_iter=100):
    """
    Applies Newton-Raphson method to find one root.
    :param poly: List of polynomial coefficients
    :param x0: Initial guess
    :param tol: Convergence tolerance
    :param max_iter: Maximum number of iterations
    :return: Root (float) or None if it fails to converge
    """
    for _ in range(max_iter):
        fx, dfx = horner(poly, x0)
        if dfx == 0:
            return None  # Derivative is zero, can't proceed
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1  # Root found
        x0 = x1
    return None  # Failed to converge

# Deflate the polynomial after finding a root
def deflate(poly, root):
    """
    Deflates the polynomial by dividing it by (x - root).
    :param poly: Original polynomial
    :param root: Root found
    :return: Deflated polynomial
    """
    n = len(poly)
    new_poly = [poly[0]]  # Start with leading coefficient

    for i in range(1, n - 1):
        new_poly.append(poly[i] + new_poly[-1] * root)

    return new_poly

# Find all roots by iteratively applying Newton-Raphson and deflating
def find_all_roots(poly):
    """
    Finds all roots of a polynomial by applying Newton-Raphson and deflation.
    :param poly: Polynomial coefficients
    :return: List of roots
    """
    poly = poly[:]  # Copy to avoid changing original
    roots = []
    degree = len(poly) - 1

    while degree > 0:
        guess = 0.0
        root = newton_raphson(poly, guess)
        if root is None:
            print("Failed to converge on a root.")
            break
        roots.append(root)
        poly = deflate(poly, root)
        degree -= 1

    return roots

# Example usage / test case
def test():
    # Polynomial: x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
    poly = [1, -6, 11, -6]
    print("Finding roots of:", poly)
    roots = find_all_roots(poly)
    print("Roots found:")
    for r in roots:
        print(round(r, 6))

# Entry point
if __name__ == "__main__":
    test()
