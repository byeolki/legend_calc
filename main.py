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
    inp = input().replace(" ", "")
    if "+" in inp:
        a, b = map(int, inp.split("+"))
        print(calc.plus(a, b))  
    elif "-" in inp:
        a, b = map(int, inp.split("-"))
        print(calc.minus(a, b))  
    elif "*" in inp:
        a, b = map(int, inp.split("*"))
        print(calc.multiple(a, b))  
    elif "/" in inp:
        a, b = map(int, inp.split("/"))
        print(calc.divide(a, b))  
    else:
        print("plz retry")