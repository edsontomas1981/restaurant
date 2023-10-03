import sys
sys.path.append('..')  # Adiciona o diretório pai ao caminho do sistema

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI  # Importe a configuração do banco de dados
from flask_cors import CORS
from utils.categoria import Categoria
from utils.tamanhos import Tamanhos
from flask_migrate import Migrate  # Apenas uma importação

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/restaurant_db.db'  # Usando SQLite neste exemplo
db = SQLAlchemy(app)

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

class Fornecedores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))

class testando(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer)

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
