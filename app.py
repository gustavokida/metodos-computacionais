from flask import Flask, request
import json
import FuncaoZero
import EditaFuncao
import importlib
import Funcao
import IC
import Correlacao


app = Flask(__name__)


@app.route('/funcaozero/funcao', methods=['POST'])
def funcao():
    funcao = request.json['funcao']
    EditaFuncao.editaFuncao(funcao)
    importlib.reload(Funcao)


@app.route('/funcaozero/bissecao', methods=['POST'])
def bissecao():
    a = request.json['a']
    b = request.json['b']
    erro = request.json['erro']
    return json.dumps(FuncaoZero.bissecao(float(a), float(b), float(erro)))

@app.route('/funcaozero/posicaofalsa', methods=['POST'])
def posicaofalsa():
    a = request.json['a']
    b = request.json['b']
    erro = request.json['erro']
    return json.dumps(FuncaoZero.bissecao(float(a), float(b), float(erro)))

@app.route('/funcaozero/newtonralphson', methods=['POST'])
def newtonralphson():
    a = request.json['a']
    erro = request.json['erro']
    return json.dumps(FuncaoZero.bissecao(float(a), float(erro)))

@app.route('/funcaozero/secante', methods=['POST'])
def secante():
    a = request.json['a']
    b = request.json['b']
    erro = request.json['erro']
    return json.dumps(FuncaoZero.bissecao(float(a), float(b), float(erro)))



@app.route('/ic/normal', methods=['POST'])
def icnormal():
    dpp = request.json['dpp']
    n = request.json['n']
    media = request.json['media']
    sig = request.json['sig']
    return json.dumps(IC.icNormal(float(dpp), float(n), float(media), float(sig)))

@app.route('/ic/student', methods=['POST'])
def icstudent():
    dp = request.json['dp']
    n = request.json['n']
    media = request.json['media']
    sig = request.json['sig']
    return json.dumps(IC.icStudent(float(dp), float(n), float(media), float(sig)))

@app.route('/ic/populacional', methods=['POST'])
def icpopulacional():
    sucesso = request.json['sucesso']
    n = request.json['n']
    sig = request.json['sig']
    return json.dumps(IC.pPopulacional(float(sucesso), int(n), float(sig)))



@app.route('/correlacao/pearson', methods=['POST'])
def pearson():
    listax = request.json['listax']
    listay = request.json['listay']
    return json.dumps(Correlacao.pearson(listax, listay))

@app.route('/correlacao/spearman', methods=['POST'])
def spearman():
    listax = request.json['listax']
    listay = request.json['listay']
    return json.dumps(Correlacao.spearman(listax, listay))

@app.route('/correlacao/kendall', methods=['POST'])
def kendall():
    listax = request.json['listax']
    listay = request.json['listay']
    return json.dumps(Correlacao.kendall(listax, listay))


if __name__ == '__main__':
	app.run()