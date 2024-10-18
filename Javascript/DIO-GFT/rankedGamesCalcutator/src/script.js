// Pegando os elementos do DOM
const buttonCalcular = document.getElementById("calcular");
const numeroVitoriasInput = document.getElementById("vitorias");
const numeroDerrotasInput = document.getElementById("derrotas");
const resultadoLabel = document.getElementById("resultado-label");

// Função para calcular o ranking
function calcularRank(vitorias, derrotas) {
    const saldo = vitorias - derrotas; // Calcula o saldo entre vitórias e derrotas
    let rank;

    // Comparando o saldo para definir o ranking
    if (saldo <= 10) {
        rank = "Ferro";
    } else if (saldo >= 11 && saldo <= 20) {
        rank = "Bronze";
    } else if (saldo >= 21 && saldo <= 50) {
        rank = "Prata";
    } else if (saldo >= 51 && saldo <= 80) {
        rank = "Ouro";
    } else if (saldo >= 81 && saldo <= 90) {
        rank = "Diamante";
    } else if (saldo >= 91 && saldo <= 100) {
        rank = "Lendário";
    } else if (saldo > 100) {
        rank = "Imortal";
    } else {
        rank = "Inválido"; // Caso haja algum erro nos valores
    }

    return rank;
}

// Evento de clique no botão de calcular
buttonCalcular.addEventListener("click", function() {
    // Pegando os valores dos inputs e convertendo para número
    const numeroVitorias = parseInt(numeroVitoriasInput.value);
    const numeroDerrotas = parseInt(numeroDerrotasInput.value);

    // Verificando se os valores são números válidos
    if (isNaN(numeroVitorias) || isNaN(numeroDerrotas)) {
        resultadoLabel.innerText = "Por favor, insira números válidos.";
        return;
    }

    // Chamando a função de calcular o rank e exibindo no label
    const rank = calcularRank(numeroVitorias, numeroDerrotas);
    resultadoLabel.innerText = `Seu ranking é: ${rank}`;
});
