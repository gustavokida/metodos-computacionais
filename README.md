# metodos-computacionais

Utilize o python 3.7, porém acredito q a versão 3.6 também deva funcionar normalmente.

---------------------------------------------------------------------

Utilize o Postman, configure o headers inserindo "Content-Type"(Sem as aspas) na KEY, e "application/json"(sem as aspas) no VALUE. Coloque no modo POST.

O endereço provavelmente será "http://localhost:5000/".

---------------------------------------------------------------------

Para abrir a api, é necesário instalar o modulo flask do python.
	$ sudo apt-get install python-pip
	$ pip install flask

Na abra o terminal na pasta onde se encontra o arquivo "app.py" e digite:
	$ export FLASK_APP=app.py
	$ flask run


---------------------------------------------------------------------

FUNCAO ZERO

A FUNÇÃO É ESCRITA NO ENDEREÇO "/funcaozero/funcao"



***OBS: Caso tenha enviado uma função inválida e o programa pare de abrir ou funcionar corretamente, execute o arquivo python "ArrumaFuncao.py".




	Exemplo de entrada:
	{
	 "funcao" : "x*x*x-9*x+3"
	}

Siga essas regras quando escrever a função.


	log(x) -> logaritmo base 10
	ln(x)  -> logaritmo base e
	sin(x) -> seno
	cos(x) -> cosseno
	tan(x) -> tangente

operações basicas:

	* -> multiplicação
	x*x*x -> Potência deve ser feita na forma de multiplicação
	sqrt(x) -> raiz quadrada
	+ -> soma
	- -> subtração
	() -> operador de procedência
	/ -> divisão



2.OBS: Não é necessário escrever a derivada, pois foi utilizada a definição de derivada para calcular ela.(Se encontra no arquivo "Funcao.py" juntamente com a função. 



Bisseção:
endereço: "/funcaozero/bissecao"

Exemplo de entrada:

	{
	 "a" : "1",
	 "b" : "2",
	 "erro" : "0.01"
	}

posição falsa:
endereço: "/funcaozero/posicaofalsa"

	Exemplo de entrada:

	{
	 "a" : "1",
	 "b" : "2",
	 "erro" : "0.01"
	}

newton ralphson:
endereço: "/funcaozero/newtonralphson"

Exemplo de entrada:

	{
	 "a" : "1",
	 "erro" : "0.01"
	}

secante:
endereço: "/funcaozero/secante"

	Exemplo de entrada:
	{
	 "a" : "1",
	 "b" : "2",
	 "erro" : "0.01"
	}


---------------------------------------------------------------------

INTERVALO DE CONFIANÇA

	dpp = desvio padrão populacional

	dp = desvio padrão

	n = quantidade da população

	sucesso = quantidade de sucesso

	sig = significância

Normal:
endereço: "/ic/normal"

Exemplo de entrada:

	{
	 "dpp" : "5",
	 "n" : "100",
	 "media" : "500",
	 "sig" : "95"
	}

Student:
endereço: "/ic/student"

Exemplo de entrada:

	{
	 "dp" : "5",
	 "n" : "100",
	 "media" : "500",
	 "sig" : "95"
	}

populacional:
endereço: "/ic/populacional"

Exemplo de entrada:

	{
	 "sucesso" : "5",
	 "n" : "100",
	 "sig" : "95"
	}

---------------------------------------------------------------------

CORRELAÇÃO

o espaço ' ' é utilizado para separar os números, como mostrado nos exemplos.

Pearson:
endereço: "/correlacao/pearson"

Exemplo de entrada:

	{
	 "listax" : "1 2 3 4 5 6 7 35 100 43",
	 "listay" : "4 1 3 5 6 100 2 3 90 20"
	}

Spearman:
endereço: "/correlacao/spearman"

Exemplo de entrada:

	{
	 "listax" : "1 2 3 4 5 6 7 35 100 43",
	 "listay" : "4 1 3 5 6 100 2 3 90 20"
	}

Kendall:
endereço: "/correlacao/kendall"

Exemplo de entrada:

	{
	 "listax" : "1 2 3 4 5 6 7 35 100 43",
	 "listay" : "4 1 3 5 6 100 2 3 90 20"
	}





