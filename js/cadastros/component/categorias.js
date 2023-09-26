criaCategoria = document.getElementById('criaCategoria');
readCategorias = document.getElementById('readCategorias');
deleteCategorias = document.getElementById('deleteCategoria');

const BASEURL = "http://127.0.0.1:5000"

class Conexao {
    constructor(url,data){
        this.url=BASEURL+url
        this.data=data
    }

    getCSRFToken() {
      const match = document.cookie.match(/(^|;)csrftoken=([^;]*)/);
      if (match && match[2]) {
          return match[2];
      } else {
          // Lida com o caso em que o cookie csrftoken não foi encontrado
          console.error("O cookie 'csrftoken' não foi encontrado.");
          return null; // Ou outra ação apropriada, dependendo do seu caso
      }
    }
     
    async sendPostRequest() {
      // this.csrfToken=this.getCSRFToken()
      try {
        const response = await fetch(this.url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            // "X-CSRFToken": this.csrfToken,
          },
          body: JSON.stringify(this.data),
        });
  
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        const result = await response.json();
        return result;
      } catch (error) {
        console.error(error);
        // alert("Erro interno!");
      }
    }
}

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

// criaCategoria.addEventListener('click', async (e) => {
//     let categoriaNome = document.getElementById('categoria').value
//     try {
//         let url = '/api/add_categoria'
//         let dados = {
//             'item': categoriaNome
//         }
//         let conexao = new Conexao(url, dados)
//         let result = await conexao.sendPostRequest()
//         if (result.status == 200){
//           msgOK("Categoria cadastrada com sucesso! 🎉")
//           carregaTabelaCategorias()
//         }
//     } catch (error) {
//         console.error('Ocorreu um erro:', error);
//     }
//     e.preventDefault();

// })

const carregaTabelaCategorias = async()=>{
  try {
      let url ='/api/read_categorias'
      let dados = {}
      let conexao = new Conexao(url, dados)
      let result = await conexao.sendPostRequest()
      return result
  } catch (error) {
      console.error('Ocorreu um erro:', error);
  }
}

// const populaTabelaCategoria = (request)=>{
//   let tabelaCategorias = document.getElementById('tableCategorias')
//   let htmlTabela = ``
//   // tabelaCategorias.innerHTML=htmlTabela
//   let data = request
//   let template
//   data.forEach(item => {
//   template += '<tr class="tr" id=' + item[0] + ' ">' +
//         '<td>' + item[0] + '</td>' +
//         '<td>' + item[1] + '</td>' +
//         '<td>' + '<i class="fa fa-eraser" aria-hidden="true"></i>' + '</td>' +
//       '</tr>';
//   });
//   template=`
//         <thead>
//           <tr>
//             <th scope="col">Id</th>
//             <th scope="col" colspan="3">Categoria</th>
//           </tr>
//         </thead>
//         <tbody>
//           ${template}
//         </tbody>
//     `
//     tabelaCategorias.innerHTML=template
// }
// carregaTabelaCategorias()
// Adicione o evento de clique aos ícones

document.addEventListener('click', function (e) {
  if (e.target && e.target.classList.contains('fa-pencil')) {
    // O ícone de lápis foi clicado
    const rowId = e.target.closest('tr').getAttribute('id');
    // Faça algo com o ID da linha clicada (rowId)
    console.log('Lápis clicado na linha com ID:', rowId);
  } else if (e.target && e.target.classList.contains('fa-eraser')) {
    const rowId = e.target.closest('tr').getAttribute('id');
    deletaCategoria(rowId);
  }
});

const carrega_cmb_categorias = async()=>{
  let cmb_categorias = document.getElementById("cmb_categorias")
  let template
  let data = await carregaTabelaCategorias()
  data.forEach(item => {
  template +=`<option value=${item[0]}>${item[1]}</option>
  `;
  cmb_categorias.innerHTML=template
  });
}

carrega_cmb_categorias()



