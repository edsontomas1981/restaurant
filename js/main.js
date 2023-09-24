document.addEventListener('DOMContentLoaded', () => {
    const itemList = document.getElementById('item-list');
    const itemForm = document.getElementById('item-form');
    const itemInput = document.getElementById('item-input');

    // Função para carregar a lista de itens da API e exibir na página
    function loadItems() {
        fetch('http://127.0.0.1:5000/api/items')
            .then(response => response.json())
            .then(data => {
                itemList.innerHTML = ''; // Limpar a lista existente
                data.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = item;
                    itemList.appendChild(li);
                });
            })
            .catch(error => console.error('Erro:', error));
    }

    // Carregar itens quando a página carregar
    loadItems();

    // Enviar o formulário para adicionar um item à API
    itemForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const newItem = itemInput.value.trim();
        if (newItem !== '') {
            fetch('http://127.0.0.1:5000/api/items', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'item': newItem }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                    loadItems(); // Recarregar a lista de itens após a adição
                    itemInput.value = ''; // Limpar o campo de entrada
                })
                .catch(error => console.error('Erro:', error));
        }
    });
});
