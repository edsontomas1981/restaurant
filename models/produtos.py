from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
print("opa entrou produto")

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'), nullable=False)
    descricao = db.Column(db.Text)  # Descrição do produto
    preco = db.Column(db.Float, nullable=False)
    codigo_barras = db.Column(db.String(50))
    ingredientes = db.Column(db.Text)  # Lista de ingredientes
    tamanho_quantidade = db.Column(db.String(50))  # Tamanho ou quantidade do produto
    disponibilidade = db.Column(db.Boolean, default=True)  # Indicação de disponibilidade
    imagem_url = db.Column(db.String(255))  # URL da imagem do produto
    tempo_preparo = db.Column(db.Integer)  # Tempo estimado de preparo
    receita = db.Column(db.Text)  # Instruções de preparo
    informacoes_nutricionais = db.Column(db.Text)  # Informações nutricionais
    origem_fornecedor = db.Column(db.String(100))  # Origem dos ingredientes/fornecedor
    classificacao = db.Column(db.Float)  # Classificação/avaliação do produto
    data_inclusao = db.Column(db.Date)  # Data de inclusão no menu
    estoque = db.Column(db.Integer)  # Quantidade em estoque
    restricoes_dieteticas = db.Column(db.String(100))  # Restrições dietéticas
    sazonalidade = db.Column(db.String(50))  # Sazonalidade do produto
    numero_pedido_identificador = db.Column(db.String(50))  # Número de pedido/identificador
