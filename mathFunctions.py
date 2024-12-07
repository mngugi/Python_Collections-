import sympy as sym

x = sym.Symbol('x')
func = input("Enter function: ")

sym.Derivative(func, x)
