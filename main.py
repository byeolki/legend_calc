from minus import *
from plus import *
from multiple import *
from divide import *

class LegendCalc():
    def __init__(self):
        self.minus = minus
        self.plus = plus
        self.multiple = multiply
        self.divide = div

if __name__ == "__main__":
    calc = LegendCalc()
    a, op, b = input().split()
    a = int(a); b = int(b)
    if op == "+":
        print(calc.plus(a, b))  
    elif op == "-":
        print(calc.minus(a, b))  
    elif op == "*" or op == "x":
        print(calc.multiple(a, b))  
    elif op == "/":
        print(calc.divide(a, b))  
    else:
        print("plz retry")