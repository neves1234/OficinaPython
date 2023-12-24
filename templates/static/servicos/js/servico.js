fetch('/finalizar_servico/' + servicoId, {
        method: 'POST'
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Ocorreu um erro ao finalizar o serviço.');
    })
    .then(data => {
        // Altere o status do serviço no DOM
        const linhaServico = document.querySelector(`tr[data-servico-id="${servicoId}"]`);
        linhaServico.querySelector('td:nth-child(5)').textContent = data.finalizado ? 'Finalizado' : 'Em andamento';
        linhaServico.querySelector('td:nth-child(5) span').style.color = data.finalizado ? 'rgb(198, 255, 198)' : 'rgb(255, 198, 198)';
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao finalizar o serviço: ' + error.message);
    });
    