const imagemPokemon = document.querySelector('.pokemon-image');

function proximoPokemon() {
    if (imagemPokemon.src == `./img/charmander.avif`) {
        imagemPokemon.src = `./img/charmeleon.avif`;
    }
    else if (imagemPokemon.src == `./img/charmeleon.avif`) {
        imagemPokemon.src = `./img/charizard.avif`;
    }
    else {
        imagemPokemon.src = `./img/charmander.avif`;
    }

    console.log("funcionando");
}

function pokemonAnterior() {
    if (imagemPokemon.src == `./img/charizard.avif`) {
        imagemPokemon.src = `./img/charmeleon.avif`;
    }
    else if (imagemPokemon.src == `./img/charmeleon.avif`) {
        imagemPokemon.src = `./img/charmander.avif`;
    }
    else {
        imagemPokemon.src = `./img/charizard.avif`;
    }
}

document.getElementById("proximoPokemonButton").addEventListener("click", proximoPokemon());