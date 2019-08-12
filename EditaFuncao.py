

def editaFuncao(funcao):
    filename = "Funcao.py"
    f = open(filename, 'w')

    codigolib = "import decimal\n" + "import math\n" + "from math import *\n"
    codigo = codigolib + "\ndef f(x):\n"
    codigo2 = "    return " + funcao #colocar o os.remove("MetodosComputacionais-Funcao.py") nas funções.
    codigo3 = "\ndef f_linha(x):\n"
    codigo4 = "    h = decimal.Decimal(1e-10)\n"
    codigo5 = "    return (f(x + h) - f(x)) / h"
    f.writelines(codigo)
    f.writelines(codigo2)
    f.writelines(codigo3)
    f.writelines(codigo4)
    f.writelines(codigo5)
    f.close()
