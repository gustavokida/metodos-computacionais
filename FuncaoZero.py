import math
import Funcao
from math import *
import os

def bissecao(a, b, erro):

    fa = float(Funcao.f(a))
    fb = float(Funcao.f(b))
    x = float((a + b) / 2)
    fx = float(Funcao.f(x))

    while fa * fb < 0 and fabs(fx) > erro:
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = Funcao.f(a)
        fb = Funcao.f(b)
        x = float((a + b) / 2)
        fx = Funcao.f(x)

    resultado = (('resultado', x))
    return resultado

def posicao_falsa(a, b, erro):
    def valorX(a, b):
        return (a * Funcao.f(b) - b * Funcao.f(a)) / (Funcao.f(b) - Funcao.f(a))

    fa = Funcao.f(a)
    fb = Funcao.f(b)
    x = valorX(a, b)
    fx = Funcao.f(x)

    while fa * fb < 0 and fabs(fx) > erro:
        if fx * fb < 0:
            a = x
        else:
            b = x
        fa = Funcao.f(a)
        fb = Funcao.f(b)
        x = valorX(a, b)
        fx = Funcao.f(x)

    resultado = (('resultado', x))
    return resultado

def newton_ralphson(x, erro):
    def calculaX(x0):
        return x0 - Funcao.f(x0) / Funcao.f_linha(x0)


    while ((abs(f(x))) > erro):
        x = calculaX(x)
    return x

def secante(x1, x2, erro):
    def calculaX(x1, x2):
        return (x1 * Funcao.f(x2) - x2 * Funcao.f(x1)) / (Funcao.f(x2) - Funcao.f(x1))


    x = calculaX(x1, x2)
    while fabs(Funcao.f(x)) > erro:
        x1 = x2
        x2 = x
        x = calculaX(x1, x2)

    resultado = (('resultado', x))
    return resultado



