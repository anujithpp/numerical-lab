import math

def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Find the root of an equation using the bisection method
    
    Parameters:
    - f: Function to find root for
    - a, b: Initial interval boundaries
    - tolerance: Desired precision of root
    - max_iterations: Maximum number of iterations
    
    Returns:
    Root of the equation or None if not found
    """
    
    # Check if root exists in interval
    if f(a) * f(b) >= 0:
        print("Bisection method fails: No sign change detected")
        return None
    
    iterations = 0
    while (b - a) / 2 > tolerance and iterations < max_iterations:
        # Calculate midpoint
        c = (a + b) / 2
        
        # Evaluate function at midpoint
        fc = f(c)
        
        # Update interval
        if fc == 0:
            return c  # Exact root found
        elif f(a) * fc < 0:
            b = c  # Root is in left half
        else:
            a = c  # Root is in right half
        
        iterations += 1
    
    return (a + b) / 2

# Example usage
def example_function(x):
    return x**2 - 4  # Example equation: x^2 - 4 = 0

# Find root between 0 and 3
root = bisection_method(example_function, 0, 3)
print(f"Root found: {root}")
