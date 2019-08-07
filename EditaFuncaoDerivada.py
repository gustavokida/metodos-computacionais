

def editaFuncao(funcao):
    filename = "FuncaoDerivada.py"
    f = open(filename, 'w')

    codigolib = "import os\n" + "import math\n" + "from math import *\n"
    codigo = codigolib + "\ndef f_linha(x):\n"
    codigo2 = "    return " + funcao
    f.writelines(codigo2)
    f.close()
