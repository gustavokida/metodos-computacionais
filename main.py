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

def reload_funcao():
   # os.system('del __pycache__\\Funcao.cpython-37.pyc')
    os.remove('__pycache__/Funcao.cpython-37.pyc')
    importlib.reload(Funcao)

#print(IC.icStudent(5, 100, 500, 95))







#if __name__ == '__main__':
funcao = input("Digite a funcao:")
EditaFuncao.editaFuncao(funcao)
reload_funcao()
a = 1
b = 0
erro = 0.01
print(FuncaoZero.secante(b, a, erro))

funcao = input("Digite a funcao:")
EditaFuncao.editaFuncao(funcao)
reload_funcao()
a = 1
b = 0
erro = 0.05
print(FuncaoZero.secante(b, a, erro))
