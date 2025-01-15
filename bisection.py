import math

def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    
    if f(a) * f(b) >= 0:
        print("Bisection method fails: No sign change detected")
        return None
    
    iterations = 0
    while (b - a) / 2 > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        
        fc = f(c)
        
        if fc == 0:
            return c  
        elif f(a) * fc < 0:
            b = c  
        else:
            a = c  
        
        iterations += 1
    
    return (a + b) / 2

def example_function(x):
    return x**2 - 4  

root = bisection_method(example_function, 0, 3)
print(f"Root found: {root}")
