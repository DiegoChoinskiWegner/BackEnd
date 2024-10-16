import Hero, { Warrior, Mage, Archer } from "./hero.js";
//import { Warrior, Mage, Archer } from "./heroTypes.js";

const showHero = document.getElementById('showHero');
const formHero = document.getElementById('formHero');



function criarHeroi() {
    formHero.style.display = 'flex';
}


function salvarHeroi() {
    const nome = document.getElementById('nome').value;
    const tipo = document.getElementById('tipo').value;
    const level = 1; // Valor padrão para o nível

    // Criando o herói com base no tipo
    let novoHeroi;
    if (tipo == 'mage') {
        novoHeroi = new Hero(nome, level, new Mage());
    } else if (tipo == 'warrior') {
        novoHeroi = new Hero(nome, level, new Warrior());
    } else if (tipo == 'archer') {
        novoHeroi = new Hero(nome, level, new Archer());
    } else {
        console.error('Tipo de herói inválido');
        return;
    }

    // Exibindo as informações do herói no console (pode ser substituído por qualquer outra ação)
    novoHeroi.showHero();
}




document.getElementById('criarHeroiButton').addEventListener('click', criarHeroi);
document.getElementById('salvarHeroiButton').addEventListener('click', salvarHeroi);