import os
import sys

# Obtenha o diretório do arquivo atual (onde servidor_main.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Adicione o diretório raiz do projeto ao sys.path
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from backend.config import SQLALCHEMY_DATABASE_URI  # Importe a configuração do banco de dados
from flask_cors import CORS
from .utils.categoria  import Categoria
from .utils.tamanhos import Tamanhos
from flask_migrate import Migrate  # Apenas uma importação

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Configurar a URI do banco de dados
db = SQLAlchemy(app)  # Criar a instância do SQLAlchemy e registrá-la no aplicativo

CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"items": "teste", "tabelaCriada": "TABELA OK"})

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

@app.route('/api/add_tamanho', methods=['GET'])
def add_tamanho():
    # data = request.get_json()
    tamanho = Tamanhos()
    tamanho.criar_tamanho("GG")
    return jsonify({"items": "teste", "tabelaCriada": "TABELA OK"}),200


@app.route('/api/delete_categoria', methods=['POST'])
def delete_categoria():
    data = request.get_json()
    categoria = Categoria()
    categoria.deletar_categoria(data['id'])
    return jsonify({"status": "ok"}), 200

@app.route('/criar_tabelas', methods=['GET'])
def criar_tabelas():
    with app.app_context():
        db.create_all()
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # criar_tabelas()  # Chama a função para criar tabelas quando o aplicativo é executado
    # Settings for migrations
    migrate = Migrate(app, db)
    app.run(debug=True)
