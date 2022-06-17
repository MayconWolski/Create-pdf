from banco import Client
from flask import Flask, flash, redirect, render_template
import pandas as pd
from flask.globals import request
from connect import deleteCode, download_pdf, insert, query_data, search_data, show_all, updade_client


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def Inicio():
    result = show_all()
    return render_template('index.html', result=result)     

@app.route('/teste')
def Inicio2():
    result = show_all()
    return render_template('tag_client.html', result=result)     

@app.route('/cadastrar', methods=["POST", 'GET'])
def cadrastrar():
    codigo = request.form['codigo']
    consulta = query_data(codigo)
    if consulta =="Pode registrar":
        nome = request.form['nome']
        endereço = request.form['endereço']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        CEP = request.form['CEP']
        client = Client(codigo, nome, endereço, numero, complemento, bairro, cidade, estado, CEP)
        insert(client)
        result = download_pdf()
        return redirect("/")
    elif consulta=="codigo erro":
        flash ("Codigo ja registrado ")
        return redirect("/")
    else:
        return "Algo deu errado"  
       
@app.route("/deletar/<int:codigo>")
def deletar(codigo):
    try:
        deleteCode(codigo)
        return redirect("/")
    except:
        return "Algo deu errado"    


@app.route('/atualizar/<int:codigo>',methods=["POST","GET"])
def atualizar(codigo):   
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        endereço = request.form['endereço']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        CEP = request.form['CEP']
        index_update = Client(codigo, nome, endereço, numero, complemento, bairro, cidade, estado, CEP)
        try:
            updade_client(codigo, index_update)
            return redirect('/')
        except:
            return 'algo deu errado'
    else:
        index_update = search_data(codigo)
        return render_template('index_update.html', index_update=index_update)             

if __name__ == "__main__":
    app.run(port=3000, debug=True)





