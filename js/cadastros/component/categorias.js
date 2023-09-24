criaCategoria = document.getElementById('criaCategoria');
categorias = document.getElementById('readCategorias');
deleteCategorias = document.getElementById('deleteCategoria');

categorias.addEventListener('click', async (e) => {
    try {
        let url = '/api/read_categorias'
        let dados = {
            'item': "newItem"
        }
        conexao = new Conexao(url, dados)
        let result = await conexao.sendPostRequest()
        console.log(result)
        e.preventDefault();
    } catch (error) {
        console.error('Ocorreu um erro:', error);
    }
    e.preventDefault();
})

deleteCategorias.addEventListener('click', async (e) => {
    try {
        let url = '/api/delete_categoria'
        let dados = {
            'item': "newItem"
        }
        conexao = new Conexao(url, dados)
        let result = await conexao.sendPostRequest()
        console.log(result)
        e.preventDefault();
    } catch (error) {
        console.error('Ocorreu um erro:', error);
    }
    e.preventDefault();
})


criaCategoria.addEventListener('click', async (e) => {
    alert("ok ok")
    try {
        let url = '/api/add_categoria'
        let dados = {
            'item': "newItem"
        }
        conexao = new Conexao(url, dados)
        let result = await conexao.sendPostRequest()
        e.preventDefault();
    } catch (error) {
        console.error('Ocorreu um erro:', error);
    }
})


document.getElementById('tableCategorias').innerHTML=`
<table class="table">
  <thead>
    <tr>
      <th scope="col">Categoria</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
`