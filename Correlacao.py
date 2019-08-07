import math
from math import *

def pearson(listX, listY):
    totalX = sum(listX)
    totalY = sum(listY)

    mediaX = totalX/len(listX)
    mediaY = totalY/len(listY)

    somaX = []
    somaY = []
    for i in listX:
        somaX[i] = listX[i] - mediaX
    for i in listY:
        somaY[i] = listY[i] - mediaY

    quadradoX = 0
    quadradoY = 0
    for i in somaX:
        quadradoX += somaX[i]*somaX[i]
    for i in somaY:
        quadradoY += somaY[i]*somaY[i]

    r = 0
    for i in somaX:
        r += (somaX[i]*somaY[i]) / (sqrt(quadradoX)*sqrt(quadradoY))

    return r

def spearman(listX, listY):

    soma = 0
    for i in listX:
        soma += (listX[i] - listY[i])*(listX[i] - listY[i])

    n = len(listX)
    p = 1 - (6*soma/(n*(n*n - 1)))
    return p

def kendall(listX, listY):

    concordantes = 0
    discordantes = 0

    for i in listX:
        for j in listX:
            if listX[i] < listX[j] and listY[i] < listY[j]:
                concordantes += 1
            elif listX[i] > listX[j] and listY[i] > listY[j]:
                concordantes += 1
            else:
                discordantes += 1

    n = len(listX)
    t = (concordantes - discordantes) / (n*(n-1)/2)
    return t

