import math

def f(x):
    return math.sin(x)

def central_difference_method(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

#parameters

x = math.pi / 4
h = 0.05

derivative = str(central_difference_method(f,x,h))

print("Estimated derivative of sin(x) at x = pi/4 is :" + derivative)
