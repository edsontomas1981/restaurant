import sqlite3  # Importe o módulo sqlite3
from controller.conexao import conectar_bd

class Categoria():
    def criar_categoria(nome):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categoria (nome) VALUES (?)", (nome,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao criar categoria:", e)
        finally:
            conn.close()

    def ler_categorias():
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()
            return categorias
        except sqlite3.Error as e:
            print("Erro ao ler categorias:", e)
        finally:
            conn.close()

    def atualizar_categoria(id, nome):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("UPDATE categoria SET nome = ? WHERE id = ?", (nome, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao atualizar categoria:", e)
        finally:
            conn.close()

    def deletar_categoria(id):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categoria WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao deletar categoria:", e)
        finally:
            conn.close()
