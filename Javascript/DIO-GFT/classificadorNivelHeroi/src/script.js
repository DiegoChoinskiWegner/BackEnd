const formHero = document.getElementById('formHero');



function criarHeroi() {
    //formHero.style.display = 'block';
    console.log("teste")
}

function salvarHeroi() {
    const nome = document.getElementById('nome').value;
    const tipo = document.getElementById('tipo').value;
    const level = 1; // Valor padrão para o nível

    // Criando o herói com base no tipo
    let novoHeroi;
    if (tipo === 'mage') {
        novoHeroi = new Hero(nome, level, 'Mage');
    } else if (tipo === 'warrior') {
        novoHeroi = new Hero(nome, level, 'Warrior');
    } else {
        console.error('Tipo de herói inválido');
        return;
    }

    // Exibindo as informações do herói no console (pode ser substituído por qualquer outra ação)
    novoHeroi.showHero();
}


document.getElementById('criarHeroiButton').addEventListener('click', HTMLButtonElement);
document.getElementById('salvarHeroiButton').addEventListener('click', salvarHeroi);