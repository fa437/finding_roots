# finding_roots

Title: Root Finder for Polynomial Equations Using Newton-Raphson and Horner’s Scheme

Objective
The goal of this project is to develop a generic Python program that can find all the real roots of
a polynomial equation of any degree. The program must use Newton-Raphson method combined
with Horner’s scheme, as specified in Section 1.9.

Methodology

Newton-Raphson Method:
The Newton-Raphson method is an iterative numerical technique used to find a root of a real-valued
function. The formula used is:
xn+1 = xn − P′(xn) / P(xn)
This method requires both the value of the polynomial and its derivative at each iteration step.

Horner’s Scheme:
Horner's scheme is used to evaluate both the polynomial and its derivative efficiently. It reduces the
number of multiplications required and is ideal for implementation in environments with no math
libraries.

Polynomial Deflation:
After each root is found, the polynomial is deflated (divided by x−root) using synthetic division.
This reduces the degree of the polynomial by 1, allowing repeated application of the method to find
all roots.

Features
• Works with polynomials of any order
• Finds real roots
• Requires no imports
• Uses tolerance-based convergence

Usage Example

The following polynomial is used to validate the program:
x3−6x2+11x−6

This polynomial has the roots: 1, 2, 3

Input:
poly = [1, -6, 11, -6]

Output:

Finding roots of: [1, -6, 11, -6]

Roots found:
1.0
2.0
3.0

Limitations
• Only real roots are computed (complex roots are not supported).
• Newton-Raphson may fail to converge if a poor starting guess is used or the derivative is
zero.
• No error handling for complex-valued inputs or duplicate roots.
Conclusion
This project successfully implements a complete solution to find all real roots of a polynomial using
Newton-Raphson and Horner's method. It meets the requirement of using no external libraries and
provides a mathematically sound, efficient approach to solving polynomial equations in Python.