from charset_normalizer import from_path
from numpy import source
from tinydb import Query,TinyDB
import pandas as pd
from banco import Client
import os
import shutil

import pdfkit

bd = TinyDB('BancoDados.json')
cli = Query()

def insert (banco: Client):
    bd.insert({"codigo": banco.codigo,
        "nome": banco.nome,
        "endereço": banco.endereço,
        "numero": banco.numero,
        "complemento": banco.complemento,
        "bairro": banco.bairro,
        "cidade": banco.cidade,
        "estado": banco.estado,
        "CEP": banco.CEP
    })

def show_all():
    todos = bd.all()
    return todos

def deleteCode(codigo: int):
    if bd.search (cli.codigo==str(codigo)):
        bd.remove(cli.codigo==str(codigo))
        print('Usuario apagado com sucesso')
    else:
        print('Usuario não encontarado')    

def updade_client(codigo: int, banco:Client):
    if bd.search (cli.codigo==str(codigo)):
        bd.remove(cli.codigo==str(codigo))
        insert(banco)
    else:
        print('Usuario não existe')    

def show_table():
    todos = pd.DataFrame(bd)
    return todos

def search_data(codigo):
    return bd.search(cli.codigo==str(codigo))

def query_data(codigo):
    if bd.search(cli.codigo==codigo):
        return "codigo erro"    
    else:
        return "Pode registrar"

def download_pdf():
    pdfkit.from_url("http://127.0.0.1:3000/teste", "site_teste6.pdf")
    source = r'C:\Users\mayco\OneDrive\Área de Trabalho\Create pdf\site_teste6.pdf'
    destination = r'C:\Users\mayco\OneDrive\Área de Trabalho\Create pdf\static\pdf\site_teste6.pdf'
    shutil.move(source,destination)
    

   




