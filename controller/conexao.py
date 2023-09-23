import sqlite3

# Função para criar a conexão com o banco de dados
def conectar_bd():
    conn = sqlite3.connect('restaurant_db.db')
    return conn