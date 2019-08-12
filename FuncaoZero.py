import math
import Funcao
from Funcao import *
from math import *
import os

def bissecao(a, b, erro):

    fa = f(a)
    fb = f(b)
    x = float((a + b) / 2)
    fx = f(x)

    while fa * fb < 0 and abs(fx) > erro:
        print(a, b, x, fx, fa, fb)
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = f(a)
        fb = f(b)
        x = float((a + b) / 2)
        fx = f(x)
    return x

def posicao_falsa(a, b, erro):
    def valorX(a, b):
        return (a * f(b) - b * f(a)) / (f(b) - f(a))

    fa = f(a)
    fb = f(b)
    x = valorX(a, b)
    fx = f(x)

    while fa * fb < 0 and abs(fx) > e:
        print(a, b, x, fx, fa, fb)
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = f(a)
        fb = f(b)
        x = valorX(a, b)
        fx = f(x)
    return x

def newton_raphson(x, erro):
    def calculaX(x0):
        return x0 - f(x0) / f_linha(x0)


    while ((abs(f(x))) > erro):
        print(x, f(x), f_linha(x))
        x = calculaX(x)
    return x

def secante(x1, x2, erro):
    def calculaX(x1, x2):
        return (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))


    x = calculaX(x1, x2)
    while abs(f(x)) > erro:
        print(x, f(x))
        x1 = x2
        x2 = x
        x = calculaX(x1, x2)
    return x

