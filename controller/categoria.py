import sqlite3  # Importe o módulo sqlite3
from controller.conexao import conectar_bd

class Categoria():
    def criar_categoria(self,nome):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categoria (nome) VALUES (?)", (nome,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao criar categoria:", e)
        finally:
            conn.close()

    def ler_categorias(self):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categoria")
            categorias = cursor.fetchall()
            return categorias
        except sqlite3.Error as e:
            print("Erro ao ler categorias:", e)
            return 300
        finally:
            conn.close()

    def atualizar_categoria(self,id, nome):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("UPDATE categoria SET nome = ? WHERE id = ?", (nome, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao atualizar categoria:", e)
        finally:
            conn.close()

    def deletar_categoria(self,id):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categoria WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao deletar categoria:", e)
        finally:
            conn.close()
