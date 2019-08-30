import Correlacao
import EditaFuncao
import FuncaoZero
import Funcao
import IC
# import Interpolacao

# from Correlacao import *
# from FuncaoZero import *
# from Funcao import *
# from IC import *
# from Interpolacao import *

import os
import importlib

def recarrega():
    #os.system('del __pycache__/Funcao.cpython-37.pyc')
    #os.remove('__pycache__/Funcao.cpython-37.pyc')
    importlib.reload(Funcao)

#print(IC.icStudent(5, 100, 500, 95))






#if __name__ == '__main__':

print("1. Zero de funcoes")
print("2. Interpolacao")
print("3. IC")
print("4. Coefiecientes de correlação")
print("5. Metodos de Reamostragem")
print("6. Regressão")

i = input("Digite aqui: ")
if i == '1':
    print("1. Bissecao")
    print("2. Posicao falsa")
    print("3. Newton ralphson ")
    print("4. Secante")
    j = input("Digite aqui: ")

    if j == '1':
        funcao = input("Digite a funcao: ")
        EditaFuncao.editaFuncao(funcao)
        recarrega()
        a = float(input("a: "))
        b = float(input("b: "))
        erro = float(input("erro: "))
        print(FuncaoZero.bissecao(b, a, erro))
    if j == '2':
        funcao = input("Digite a funcao: ")
        EditaFuncao.editaFuncao(funcao)
        recarrega()
        a = float(input("a: "))
        b = float(input("b: "))
        erro = float(input("erro: "))
        print(FuncaoZero.posicao_falsa(b, a, erro))
    if j == '3':
        funcao = input("Digite a funcao: ")
        EditaFuncao.editaFuncao(funcao)
        recarrega()
        x = int(input("x: "))
        erro = int(input("erro: "))
        print(FuncaoZero.bissecao(x, erro))
    if j == '4':
        funcao = input("Digite a funcao: ")
        EditaFuncao.editaFuncao(funcao)
        recarrega()
        a = int(input("a: "))
        b = int(input("b: "))
        erro = int(input("erro: "))
        print(FuncaoZero.secante(b, a, erro))

elif i == '2':
    print("1. Lagrange")
    print("2. Newton")
    print("3. Spline linear")
    print("4. Interpolação trigonométrica")
    j = input("Digite aqui: ")

elif i == '3':
    print("1. IC Normal")
    print("2. IC Student")
    print("3. IC Populacional")
    j = input("Digite aqui: ")
    if j == '1':
        dpp = float(input("Desvio padrao populacional: "))
        n = int(input("Quantidade da amostra: "))
        media = float(input("media: "))
        significancia = float(input("Significancia: "))
        print(IC.icNormal(dpp, n, media, significancia))
    if j == '2':
        dp = float(input("Desvio padrao:" ))
        n = int(input("Quantidade da amostra: "))
        media = float(input("media: "))
        significancia = float(input("Significancia: "))
        print(IC.icStudent(dp, n, media, significancia))
    if j == '3':
        sucesso = float(input("Sucesso:" ))
        n = int(input("Quantidade da amostra: "))
        significancia = float(input("Significancia: "))
        print(IC.pPopulacional(sucesso, n, significancia))


elif i == '4':
        print("1. Pearson")
        print("2. Spearman")
        print("3. Kendall")
        j = input("Digite aqui: ")
        if j == '1':
            listx =list(map(float, input("Lista x: ").split()))
            listy = list(map(float, input("Lista y: ").split()))
            print(Correlacao.pearson(listx, listy))
        if j == '2':
            listx =list(map(float, input("Lista x: ").split()))
            listy = list(map(float, input("Lista y: ").split()))
            print(Correlacao.spearman(listx, listy))
        if j == '3':
            listx =list(map(float, input("Lista x: ").split()))
            listy = list(map(float, input("Lista y: ").split()))
            print(Correlacao.kendall(listx, listy))

if i == '5':
    print("1. Bootstrap")
    print("2. jackknife")

if i == '6':
    print("1. Linear")
    print("2. Múltipla")
