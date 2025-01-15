import sympy as sp

def false_position(func, a, b, tol=1e-6, max_iter=100):
    
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    for i in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        
        if abs(func(c)) < tol:
            return c
        
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Maximum iterations exceeded without convergence.")

def input_function():
    func_str = input("Enter the function in terms of x (e.g., x**2 - 4): ")
    x = sp.symbols('x')
    func = sp.lambdify(x, sp.sympify(func_str), 'numpy')
    return func

# Main program
if __name__ == "__main__":
    func = input_function()
    
    a = float(input("Enter the start of the interval a: "))
    b = float(input("Enter the end of the interval b: "))
    
    try:
        root = false_position(func, a, b)
        print(f"The root of the equation is approximately: {root}")
    except ValueError as e:
        print(e)
