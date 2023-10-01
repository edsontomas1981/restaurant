from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI  # Importe a configuração do banco de dados
from flask_cors import CORS
from ..controller.categoria import Categoria

app = Flask(__name__)
CORS(app)

@app.route('/api/add_categoria', methods=['POST'])
def add_categoria():
    data = request.get_json()
    print(data['item']) 
    categoria = Categoria()
    categoria.criar_categoria(data['item'])
    return jsonify({'status': 200}), 200

@app.route('/api/read_categorias', methods=['POST'])
def add_read_categoria():
    data = request.get_json()
    categoria = Categoria()
    print(categoria.ler_categorias())
    return jsonify(categoria.ler_categorias()), 200

@app.route('/api/delete_categoria', methods=['POST'])
def delete_categoria():
    data = request.get_json()
    categoria = Categoria()
    categoria.deletar_categoria(data['id'])
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
