import math
import Funcao
from math import *
import os

def bissecao(a, b, erro):

    fa = Funcao.f(a)
    fb = Funcao.f(b)
    x = float((a + b) / 2)
    fx = Funcao.f(x)

    while fa * fb < 0 and abs(fx) > erro:
        print(a, b, x, fx, fa, fb)
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = Funcao.f(a)
        fb = Funcao.f(b)
        x = float((a + b) / 2)
        fx = Funcao.f(x)
    return x

def posicao_falsa(a, b, erro):
    def valorX(a, b):
        return (a * Funcao.f(b) - b * Funcao.f(a)) / (Funcao.f(b) - Funcao.f(a))

    fa = Funcao.f(a)
    fb = Funcao.f(b)
    x = valorX(a, b)
    fx = Funcao.f(x)

    while fa * fb < 0 and abs(fx) > e:
        print(a, b, x, fx, fa, fb)
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = Funcao.f(a)
        fb = Funcao.f(b)
        x = valorX(a, b)
        fx = Funcao.f(x)
    return x

def newton_ralphson(x, erro):
    def calculaX(x0):
        return x0 - Funcao.f(x0) / Funcao.f_linha(x0)


    while ((abs(f(x))) > erro):
        print(x, Funcao.f(x), Funcao.f_linha(x))
        x = calculaX(x)
    return x

def secante(x1, x2, erro):
    def calculaX(x1, x2):
        return (x1 * Funcao.f(x2) - x2 * Funcao.f(x1)) / (Funcao.f(x2) - Funcao.f(x1))


    x = calculaX(x1, x2)
    while abs(Funcao.f(x)) > erro:
        print(x, Funcao.f(x))
        x1 = x2
        x2 = x
        x = calculaX(x1, x2)
    return x

