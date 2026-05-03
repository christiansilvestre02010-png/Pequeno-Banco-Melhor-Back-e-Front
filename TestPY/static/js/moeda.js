const inputMoeda = document.getElementById('moeda');

inputMoeda.addEventListener('input', (e) => {
    let valor = e.target.value;

    // 1. Remove tudo que não é número (letras, pontos, vírgulas)
    valor = valor.replace(/\D/g, "");

    // 2. Transforma em número e divide por 100 para criar os centavos
    valor = (valor / 100).toFixed(2);

    // 3. Substitui ponto por vírgula para o formato brasileiro
    valor = valor.replace(".", ",");

    // 4. Adiciona separador de milhar (ex: 1.000,00)
    valor = valor.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");

    // 5. Devolve para o input com o prefixo R$
    e.target.value = "R$ " + valor;
});