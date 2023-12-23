const botaoFinalizar = document.querySelector('.finalizar-servico');
const servicoId = botaoFinalizar.dataset.servicoId;

// Verifique se o botão foi encontrado
if (botaoFinalizar) {
    botaoFinalizar.addEventListener('click', function () {
        // Verifique se o ID do serviço é válido
        if (servicoId === undefined || servicoId === null) {
            // Exiba uma mensagem de erro
            alert('O ID do serviço é inválido.');
            return;
        }

        // Envie uma requisição AJAX para atualizar o status do serviço no servidor
        fetch('/finalizar_servico/' + servicoId, {
            method: 'POST'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao finalizar o serviço');
            }
            return response.json();
        })
        .then(data => {
            const linhaServico = document.querySelector(`tr[data-servico-id="${servicoId}"]`);
            linhaServico.querySelector('td:nth-child(5)').textContent = 'Finalizado';
            linhaServico.querySelector('td:nth-child(5) span').style.color = 'rgb(198, 255, 198)';
        })
        .catch(error => console.error(error));
    });
} else {
    console.error('Botão não encontrado.');
}
