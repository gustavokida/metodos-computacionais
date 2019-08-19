import decimal
import math
from math import *

def f(x):
    return x*x
def f_linha(x):
    h = decimal.Decimal(1e-10)
    return (f(x + h) - f(x)) / h