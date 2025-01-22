import math

def newtonRaphson(func, derivative, initial_guess, tole=1e-6, max_iter=100):
    x = initial_guess
    for i in range(max_iter):
        f_x = func(x)
        f_prime_x = derivative(x)
        
        if f_prime_x == 0:
            raise ValueError("Derivative of the input function is zero, so Newton-Raphson method cannot be performed")
        
        x_new = x - f_x / f_prime_x
        
        if abs(x_new - x) < tole:
            return x_new, i+1  
        
        x = x_new
    
    raise ValueError(f"X did not converge to a root within {max_iter} iterations")


def func(x):
    return x**3+2*x-2

def derivative(x):
    return 3*x**2+2

root, iterations = newtonRaphson(func, derivative, initial_guess=1.0)
print(f"Root found: {root}, Iterations: {iterations}")
