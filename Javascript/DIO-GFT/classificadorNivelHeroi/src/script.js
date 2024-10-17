import Hero, { Warrior, Mage, Archer } from "./hero.js";
//import { Warrior, Mage, Archer } from "./heroTypes.js";

const showHero = document.getElementById('showHero');
const formHero = document.getElementById('formHero');
const gameContainer = document.getElementById('gameContainer');



function criarHeroi() {
    formHero.style.display = 'flex';
}


function salvarHeroi() {
    const nome = document.getElementById('nome').value;
    const tipo = document.getElementById('tipo').value;
    let level = 1; // Valor padrão para o nível
    let exp = 0;

    // Criando o herói com base no tipo
    let novoHeroi;
    if (tipo == 'mage') {
        novoHeroi = new Hero(nome, level, exp, new Mage());
    } else if (tipo == 'warrior') {
        novoHeroi = new Hero(nome, level, exp, new Warrior());
    } else if (tipo == 'archer') {
        novoHeroi = new Hero(nome, level, exp, new Archer());
    } else {
        console.error('Tipo de herói inválido');
        return;
    }

    // Exibindo as informações do herói no console (pode ser substituído por qualquer outra ação)
    novoHeroi.showHero();

    // Exibe o container de iniciar o Jogo
    gameContainer.style.display = 'flex';
    return novoHeroi;
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  

function dadosExperiencia(novoHeroi){

    let levelHeroi = novoHeroi.level;
    console.log(levelHeroi)
    let expGanha = 0;


    const tipoInimigo = getRandomNumber(1, 5);
    console.log(tipoInimigo)
    const levelInimigo = getRandomNumber(1, (levelHeroi + 3));
    console.log(levelInimigo)
    const sorte = getRandomNumber(1, 10);
    console.log(sorte)

    if (levelInimigo < levelHeroi && levelHeroi > 5){    
        if(tipoInimigo == 1){
            expGanha = novoHeroi.strength * levelInimigo;
            console.log("Experiência ganha foi: " + expGanha)
        }else if(tipoInimigo == 2){;
            expGanha = novoHeroi.intelligence * levelInimigo;
            console.log("Experiência ganha foi: " + expGanha)
        }else if(tipoInimigo == 3){
            expGanha = novoHeroi.agility * levelInimigo;
            console.log("Experiência ganha foi: " + expGanha)
        }else if(tipoInimigo == 4){
            expGanha = novoHeroi.defense * levelInimigo;
            console.log("Experiência ganha foi: " + expGanha)
        }else if(tipoInimigo == 5){
            expGanha = levelInimigo * sorte;
            console.log("Experiência ganha foi: " + expGanha)
        }
    }else if(levelHeroi < 5){
        expGanha = (levelInimigo * 1.6) * sorte;
        console.log("Experiência ganha foi: " + expGanha)
    } else{
        expGanha = novoHeroi.exp * 0.95;
        console.log("Você foi derrotado! Perca " + expGanha + " de experiência!") 
    }

    novoHeroi.exp = expGanha;
}



document.getElementById('criarHeroiButton').addEventListener('click', criarHeroi);
document.getElementById('salvarHeroiButton').addEventListener('click', salvarHeroi);
document.getElementById('iniciarJogoButton').addEventListener('click', dadosExperiencia);