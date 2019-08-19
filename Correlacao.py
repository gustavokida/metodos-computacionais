import math
from math import *

def pearson(listX, listY):
    totalX = sum(listX)
    totalY = sum(listY)

    mediaX = float(totalX/len(listX))
    mediaY = float(totalY/len(listY))

    print(mediaX, mediaY)

    def subMediaX(n):
        return n - mediaX
    def subMediaY(n):
        return n - mediaY

    somaX = list(map(subMediaX, listX))
    somaY = list(map(subMediaY, listY))
    print(somaX, somaY)
    def quadrado(n):
        return n*n
    quadradoX = float(sum(map(quadrado, somaX)))

    quadradoY = float(sum(map(quadrado, somaY)))

    r = 0
    for i in range (len(somaX)):
        r = r + float(somaX[i]*somaY[i])

    r = r / (float(sqrt(quadradoX))*float(sqrt(quadradoY)))

    return r

def spearman(listX, listY):

    soma = 0
    sortX = sorted(listX)
    sortY = sorted(listY)

    postoX = []
    postoY = []

    for i in range(len(listX)):
        for j in range(len(sortX)):
            if listX[i] == sortX[j]:
                postoX.append(j)
    for i in range(len(listY)):
        for j in range(len(sortY)):
            if listY[i] == sortY[j]:
                postoY.append(j)

    for i in range(len(listX)):
        soma += (postoX[i] - postoY[i])*(postoX[i] - postoY[i])

    n = len(listX)
    p = 1 - (6*soma/(n*(n*n - 1)))
    return p

def kendall(listX, listY):

    concordantes = 0
    discordantes = 0

    for i in range(len(listX)-1):
        for j in range(i, len(listX)-1):
            if listX[i] < listX[j+1] and listY[i] < listY[j+1]:
                concordantes += 1
            elif listX[i] > listX[j+1] and listY[i] > listY[j+1]:
                concordantes += 1
            else:
                discordantes += 1
    print(concordantes, discordantes)
    n = len(listX)
    t = (concordantes - discordantes) / (n*(n-1)/2)
    return t

