criaCategoria = document.getElementById('criaCategoria');
readCategorias = document.getElementById('readCategorias');
deleteCategorias = document.getElementById('deleteCategoria');


const deletaCategoria=async(idCategoria)=>{
  try {
    let url = '/api/delete_categoria'
    let dados = {
        'id': idCategoria
    }
    let conexao = new Conexao(url, dados)
    let result = await conexao.sendPostRequest()
    console.log(result)
    e.preventDefault();
} catch (error) {
    console.error('Ocorreu um erro:', error);
}
e.preventDefault();
}

criaCategoria.addEventListener('click', async (e) => {
    let categoriaNome = document.getElementById('categoria').value
    try {
        let url = '/api/add_categoria'
        let dados = {
            'item': categoriaNome
        }
        let conexao = new Conexao(url, dados)
        let result = await conexao.sendPostRequest()
        if (result.status == 200){
          msgOK("Categoria cadastrada com sucesso! 🎉")
          carregaTabelaCategorias()
        }
    } catch (error) {
        console.error('Ocorreu um erro:', error);
    }
    e.preventDefault();

})

const carregaTabelaCategorias = async()=>{
  try {
      let url ='/api/read_categorias'
      let dados = {}
      let conexao = new Conexao(url, dados)
      let result = await conexao.sendPostRequest()
      populaTabelaCategoria(result)
  } catch (error) {
      console.error('Ocorreu um erro:', error);
  }
}

const populaTabelaCategoria = (request)=>{
  let tabelaCategorias = document.getElementById('tableCategorias')
  let htmlTabela = ``
  // tabelaCategorias.innerHTML=htmlTabela
  let data = request
  let template

  data.forEach(item => {
  template += '<tr class="tr" id=' + item[0] + ' ">' +
        '<td>' + item[0] + '</td>' +
        '<td>' + item[1] + '</td>' +
        '<td>' + '<i class="fa fa-pencil" aria-hidden="true"></i>' + '</td>' +
        '<td>' + '<i class="fa fa-eraser" aria-hidden="true"></i>' + '</td>' +
      '</tr>';
  });
    
  template=`
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col" colspan="3">Categoria</th>
          </tr>
        </thead>
        <tbody>
          ${template}
        </tbody>
      </table>
    `
    tabelaCategorias.innerHTML=template
}

carregaTabelaCategorias()


// Adicione o evento de clique aos ícones
document.addEventListener('click', function (e) {
  if (e.target && e.target.classList.contains('fa-pencil')) {
    // O ícone de lápis foi clicado
    const rowId = e.target.closest('tr').getAttribute('id');
    // Faça algo com o ID da linha clicada (rowId)
    console.log('Lápis clicado na linha com ID:', rowId);
  } else if (e.target && e.target.classList.contains('fa-eraser')) {
    // O ícone de borracha foi clicado
    const rowId = e.target.closest('tr').getAttribute('id');
    // Faça algo com o ID da linha clicada (rowId)
    deletaCategoria(rowId);
  }
});



