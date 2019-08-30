

def editaFuncao(funcao):
    filename = "Funcao.py"
    f = open(filename, 'w')

    funcao = funcao.replace("(x)", "((x))")
    funcao = funcao.replace("log", "log10")
    funcao = funcao.replace("ln", "log")
    funcao = funcao.replace("sin(", "sin(radians")
    funcao = funcao.replace("cos(", "cos(radians")
    funcao = funcao.replace("tan(", "tan(radians")

    codigolib = "import decimal\n" + "import math\n" + "from math import *\n"
    codigo = codigolib + "\ndef f(x):\n"
    codigo2 = "    return " + funcao
    codigo3 = "\ndef f_linha(x):\n"
    codigo4 = "    h = decimal.Decimal(1e-10)\n"
    codigo5 = "    return (f(x + h) - f(x)) / h"
    f.writelines(codigo)
    f.writelines(codigo2)
    f.writelines(codigo3)
    f.writelines(codigo4)
    f.writelines(codigo5)
    f.close()
