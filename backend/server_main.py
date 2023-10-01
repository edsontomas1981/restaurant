from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI  # Importe a configuração do banco de dados
from flask_cors import CORS
from controller.categoria import Categoria

app = Flask(__name__)
CORS(app)

# Lista de itens como exemplo
items = []

@app.route('/', methods=['GET'])
def index():
    return jsonify({"items":"teste"})

if __name__ == '__main__':
    app.run(debug=True)
