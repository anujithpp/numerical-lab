import sympy as sp

def false_position(func, a, b, tol=1e-6, max_iter=100):
    """
    False Position method to find the root of the function.
    
    Parameters:
    func : callable
        The function for which the root is being sought.
    a : float
        The start of the interval.
    b : float
        The end of the interval.
    tol : float
        The tolerance for stopping the iteration (default is 1e-6).
    max_iter : int
        The maximum number of iterations (default is 100).
    
    Returns:
    root : float
        The estimated root of the function.
    """
    # Check if the initial guesses are valid
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    # Perform the False Position method
    for i in range(max_iter):
        # Calculate the point where the line intersects the x-axis
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        
        # Check if the solution is within the desired tolerance
        if abs(func(c)) < tol:
            return c
        
        # Update the interval
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Maximum iterations exceeded without convergence.")

# Define a function (this can be modified as required)
def input_function():
    # Input the function as a string and parse it
    func_str = input("Enter the function in terms of x (e.g., x**2 - 4): ")
    x = sp.symbols('x')
    func = sp.lambdify(x, sp.sympify(func_str), 'numpy')
    return func

# Main program
if __name__ == "__main__":
    # Input the function
    func = input_function()
    
    # Input the interval [a, b]
    a = float(input("Enter the start of the interval a: "))
    b = float(input("Enter the end of the interval b: "))
    
    # Calculate the root using False Position method
    try:
        root = false_position(func, a, b)
        print(f"The root of the equation is approximately: {root}")
    except ValueError as e:
        print(e)
