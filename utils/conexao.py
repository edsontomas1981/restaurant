from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Função para criar a conexão com o banco de dados
def conectar_bd():
    conn = db.engine.connect()
    return conn
