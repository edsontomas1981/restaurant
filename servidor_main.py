from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI  # Importe a configuração do banco de dados
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from models.alergenicos import Alergenico
from models.categorias import Categoria
from models.fornecedor import Fornecedor
from models.produtos import Produto

CORS(app)

with app.app_context():
    print("Criando tabelas...")
    db.create_all()
    print("Tabelas criadas com sucesso.")

# Lista de itens como exemplo
items = []

@app.route('/', methods=['GET'])
def index():
    return jsonify({"items":"teste"})

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'item' in data:
        item = data['item']
        items.append(item)
        return jsonify({'message': 'Item adicionado com sucesso!'})
    else:
        return jsonify({'error': 'O item não pode estar vazio.'}), 400

if __name__ == '__main__':
    print('iniciando ')
    app.run(debug=True)
