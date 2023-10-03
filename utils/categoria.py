from flask_sqlalchemy import SQLAlchemy
from utils.conexao import conectar_bd
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))

    def criar_categoria(self, nome):
        try:
            nova_categoria = Categoria(nome=nome)
            db.session.add(nova_categoria)
            db.session.commit()
        except SQLAlchemyError as e:
            print("Erro ao criar categoria:", e)

    def ler_categorias(self):
        try:
            categorias = Categoria.query.all()
            return [{"id": categoria.id, "nome": categoria.nome} for categoria in categorias]
        except SQLAlchemyError as e:
            print("Erro ao ler categorias:", e)
            return []

    def atualizar_categoria(self, id, nome):
        try:
            categoria = Categoria.query.get(id)
            if categoria:
                categoria.nome = nome
                db.session.commit()
        except SQLAlchemyError as e:
            print("Erro ao atualizar categoria:", e)

    def deletar_categoria(self, id):
        try:
            categoria = Categoria.query.get(id)
            if categoria:
                db.session.delete(categoria)
                db.session.commit()
        except SQLAlchemyError as e:
            print("Erro ao deletar categoria:", e)
