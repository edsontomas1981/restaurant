import unittest
from controller.categoria import Categoria
from controller.conexao import conectar_bd

class TestCategoriaMethods(unittest.TestCase):
    def test_criar_categoria(self):
        # Teste de criação de categoria
        Categoria.criar_categoria("Categoria de Teste")
        categorias = Categoria.ler_categorias()
        self.assertEqual("Categoria de Teste",categorias[-1][1],"A categoria não foi criada corretamente.")

    def test_atualizar_categoria(self):
        # Teste de atualização de categoria
        Categoria.criar_categoria("Categoria para Atualizar")
        categoria_id = Categoria.ler_categorias()[-1][0]
        Categoria.atualizar_categoria(categoria_id, "Categoria Atualizada")
        categorias = Categoria.ler_categorias()
        self.assertEqual("Categoria Atualizada",categorias[-1][1],"A categoria não foi atualizada corretamente.")
        

    def test_deletar_categoria(self):
        # Teste de exclusão de categoria
        Categoria.criar_categoria("Categoria para Deletar")
        categoria_id = Categoria.ler_categorias()[-1][0]
        Categoria.deletar_categoria(categoria_id)
        categorias = Categoria.ler_categorias()
        self.assertTrue(("Categoria para Deletar",) not in categorias)

    def tearDown(self):
        # Após cada teste, você pode limpar os dados de teste
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categoria WHERE nome = 'Categoria de Teste'")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()
