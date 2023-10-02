import sqlite3  # Importe o módulo sqlite3
from controller.conexao import conectar_bd

class Tamanhos():
    def criar_tamanho(self,tamanho):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tamanhos (tamanho) VALUES (?)", (tamanho,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao criar tamanho:", e)
        finally:
            conn.close()

    def ler_tamanhos(self):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tamanhos")
            tamanhos = cursor.fetchall()
            return tamanhos
        except sqlite3.Error as e:
            print("Erro ao ler tamanhos:", e)
            return 300
        finally:
            conn.close()

    def atualizar_tamanho(self,id, tamanho):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("UPDATE tamanhos SET tamanho = ? WHERE id = ?", (tamanho, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao atualizar tamanho:", e)
        finally:
            conn.close()

    def deletar_tamanho(self,id):
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tamanhos WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Erro ao deletar tamanho:", e)
        finally:
            conn.close()
