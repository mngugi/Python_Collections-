import math
from sympy import symbols, latex

x, y = symbols('x y')
expr = x**2 + 3*y - 1

latex_code = latex(expr)
print(latex_code)
