let modal_cad_produto  = document.getElementById("template_modal")
modal_cad_produto.innerHTML = `        
<div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <div class="row">
                <div class="form-floating mb-3 col-sm-6 pl-1 ">
                    <input type="text" class="form-control" id="nome_produto" placeholder="Nome do produto">
                    <label for="nome_produto">Nome Produto</label>
                </div>
                <div class="form-floating input-group mb-3 col-sm-6 pl-1">
                    <select class="form-select" id="cmb_categorias" aria-label="cmb_categorias" placeholder="Categoria">
                        <option selected>Selecione uma categoria</option>
                        <option value="1">Bebidas</option>
                        <option value="2">Pizzas</option>
                        <option value="3">Sobremesas</option>
                    </select>
                    <label for="cmb_categorias">Selecione uma categoria</label>
                    <button class="btn btn-primary mr-2" type="button">Adicionar categoria</button>
              </div>               
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
        </div>
    </div>
  </div>
</div>
                            `