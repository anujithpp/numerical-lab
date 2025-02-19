import numpy as np
from sympy import symbols, lambdify

def forward_difference(f, x, h):

    return (f(x + h) - f(x)) / h

equation = input("Enter the equation (use 'x' as the variable, e.g., 'x**2 + 3*x'): ")
x = float(input("Enter the point x at which to compute the derivative: "))
h = float(input("Enter the step size h: "))

x_sym = symbols('x')
f_sym = lambdify(x_sym, equation, "numpy")

derivative = forward_difference(f_sym, x, h)
print(f"The approximate derivative of the function at x = {x} is {derivative}")