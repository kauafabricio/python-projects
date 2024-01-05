""" Projeto de conexão ao banco de dados noSQL no MongoDB Atlas pelo Pymongo"""

import pprint
from urllib.parse import quote_plus
from pymongo.server_api import ServerApi
from pymongo import MongoClient

"""Dados da conta do usuário para iniciar conexão com o MongoDB Atlas"""
username = "kauafabricio"
password = ""
username_encoded= quote_plus(username)
password_encoded= quote_plus(password)
hostname = "cluster0.bqrhnp9.mongodb.net"

# Link para conexão do MongoDB Atlas com informações do usuário
uri = f"mongodb+srv://{username_encoded}:{password_encoded}@{hostname}/?retryWrites=true&w=majority"


""" Variável 'client' é a conexão à conta do usuário do MongoDB Atlas
onde será persistido o banco de dados"""
client = MongoClient(uri, server_api = ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


""" Criando banco de dados 'bank-system', e coleção 'bank'.""" 
bd = client["bank-system"]
bank_collection = bd.bank

""" Dados em formato BSON para serem inseridos no banco de dados"""
clientes_dados = [{
    "Nome Completo": "Will Byers",
    "Data de Nascimento": "16/01/1984",
    "CPF": 12345678910,
    "Endereço": "Rua das Coisas Estranhas, 94",
    "Contas" : [{"Número da Conta": 1234567, "Agência": 1001,
                "Saldo": 500.0},
                {"Número da Conta": 76543321, "Agência": 1001,
                 "Saldo": 0.0}]},
    
    {
        "Nome Completo": "Jonathan Byers",
        "Data de Nascimento": "10/10/1980",
        "CPF": 21354687910,
        "Endereço": "Rua das Coisas Estranhas, 94",
        "Contas": [{
            "Número da Conta": 1234568, "Agência": 1001,
            "Saldo": 1500.0}]
    }]


""" Inserindo os dados na coleção pela função insert_many()"""
try:
    bank_collection.insert_many(clientes_dados)
    print("Dados inseridos com sucesso!")
except Exception as e:
    print(e)

#Recuperando dados

print("\nRecuperando dados do Will Byers\n")
will_dados = bank_collection.find_one({"Nome Completo": "Will Byers"})
pprint.pprint(will_dados)
