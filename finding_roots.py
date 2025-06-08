#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Root Finder for Arbitrary-Degree Polynomials
Implementation of the Newton-Raphson method using Horner’s scheme.
No external modules used.

"""

def evaluate_polynomial_and_derivative(coefficients, x_val):
    """
    Evaluate polynomial and its derivative at a given point using Horner's method.
    """
    n = len(coefficients)
    poly_val = coefficients[0]
    deriv_val = coefficients[0]

    for i in range(1, n):
        poly_val = poly_val * x_val + coefficients[i]
        if i < n - 1:
            deriv_val = deriv_val * x_val + poly_val

    return poly_val, deriv_val


def locate_root(coefficients, starting_points, tolerance=1e-10, max_steps=100):
    """
    Apply Newton-Raphson method to find a root using multiple initial guesses.
    """
    for start in starting_points:
        current = start
        for _ in range(max_steps):
            f_val, df_val = evaluate_polynomial_and_derivative(coefficients, current)
            if df_val == 0:
                break
            next_val = current - f_val / df_val
            if abs(next_val - current) < tolerance:
                return next_val
            current = next_val
    return None


def reduce_polynomial(coefficients, root_found):
    """
    Use synthetic division to deflate polynomial by (x - root).
    """
    result = [coefficients[0]]
    for i in range(1, len(coefficients) - 1):
        result.append(coefficients[i] + result[-1] * root_found)
    return result


def extract_all_roots(coefficients):
    """
    Extract all real roots from a polynomial using iterative deflation.
    """
    roots_collected = []
    polynomial = coefficients[:]
    degree = len(polynomial) - 1

    guess_bank = [0.0, 1.0, -1.0, 2.0, -2.0, 3.0, -3.0]

    while degree > 0:
        root = locate_root(polynomial, guess_bank)
        if root is None:
            break
        rounded_root = round(root, 8)
        if not any(abs(rounded_root - existing) < 1e-6 for existing in roots_collected):
            roots_collected.append(rounded_root)
            polynomial = reduce_polynomial(polynomial, root)
            degree -= 1
        else:
            break

    return roots_collected


def run_tests():
    print("Testing custom polynomial root solver:")

    print("\nPolynomial: x^3 - 6x^2 + 11x - 6")
    poly1 = [1, -6, 11, -6]
    print("Roots:", extract_all_roots(poly1))

    print("\nPolynomial: x^3 + x^2 - x - 1")
    poly2 = [1, 1, -1, -1]
    print("Roots:", extract_all_roots(poly2))

    print("\nPolynomial: x^4 - 10x^2 + 9")
    poly3 = [1, 0, -10, 0, 9]
    print("Roots:", extract_all_roots(poly3))

run_tests()
