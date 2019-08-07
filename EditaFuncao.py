

def editaFuncao(funcao):
    filename = "Funcao.py"
    f = open(filename, 'w')

    codigolib = "import os\n" + "import math\n" + "from math import *\n"
    codigo = codigolib + "\ndef f(x):\n"
    codigo2 = "    return " + funcao #colocar o os.remove("MetodosComputacionais-Funcao.py") nas funções.
    f.writelines(codigo)
    f.writelines(codigo2)
    f.close()
