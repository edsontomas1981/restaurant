from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

print("opa entrou Alergenico")

class Alergenico(db.Model):
    __tablename__ = 'alergenicos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    # Outros campos relacionados aos alergênicos

# Defina a tabela de junção (produtos_alergenicos) fora da classe Alergenico
produtos_alergenicos = db.Table(
    'produtos_alergenicos',
    db.Column('produto_id', db.Integer, db.ForeignKey('produtos.id'), primary_key=True),
    db.Column('alergenico_id', db.Integer, db.ForeignKey('alergenicos.id'), primary_key=True)
)
