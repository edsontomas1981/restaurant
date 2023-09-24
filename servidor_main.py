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

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    print(data)
    if 'item' in data:
        item = data['item']
        items.append(item)
        return jsonify({'message': 'Item adicionado com sucesso!'})
    else:
        return jsonify({'error': 'O item não pode estar vazio.'}), 400

@app.route('/api/add_categoria', methods=['POST'])
def add_categoria():
    data = request.get_json()
    categoria = Categoria()
    categoria.criar_categoria(data['item'])
    return jsonify({'error': 'O item não pode estar vazio.'}), 400

@app.route('/api/read_categorias', methods=['POST'])
def add_read_categoria():
    data = request.get_json()
    categoria = Categoria()
    return jsonify(categoria.ler_categorias()), 200

@app.route('/api/delete_categoria', methods=['POST'])
def delete_categoria():
    data = request.get_json()
    categoria = Categoria()
    categoria.deletar_categoria(3)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
