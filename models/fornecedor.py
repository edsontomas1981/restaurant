from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

print("opa entrou fornecedor")
class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    produtos = db.relationship('Produto', backref='fornecedor', lazy=True)
    # Outros campos do fornecedor
