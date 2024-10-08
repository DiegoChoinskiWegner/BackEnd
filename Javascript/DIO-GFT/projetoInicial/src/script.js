const imagemPokemon = document.querySelector('.pokemon-image');
let contador = 1;

function proximoPokemon() {
    contador++;
    imagemPokemon.src = `pokemon${contador}.png`;
}

function pokemonAnterior() {
    if (contador > 1) {
        contador--;
        imagemPokemon.src = `pokemon${contador}.png`;
    }
}