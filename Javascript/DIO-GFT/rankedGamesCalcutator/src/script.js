import Calculator from "./renkedCalculator.js";

const buttonCalcular = document.getElementById("buttonCalcular");
const numeroVitórias = document.getElementById("numeroVitórias");
const numeroDerrotas = document.getElementById("numeroDerrotas");
 
const calculator = new Calculator(numeroVitórias, numeroDerrotas, resultado, rank);



function calcularRank(numeroVitórias, numeroDerrotas) {
    resultado = numeroVitórias - numeroDerrotas;
    return resultado;
}




buttonCalcular.addEventListener("click", calcularRank(numeroVitórias, numeroDerrotas), calculator.rankUp(resultado));