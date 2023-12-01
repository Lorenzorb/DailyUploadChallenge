import math

# solves a quadratic in the form ax^2+bx+c
def solveQuadratic(a, b, c):
    x1 = (-b + (math.sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = (-b - (math.sqrt((b**2)-(4*a*c))))/(2*a)    
    return x1, x2
x1, x2 = solveQuadratic(

print(
