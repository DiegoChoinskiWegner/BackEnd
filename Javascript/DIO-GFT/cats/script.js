const imagem = document.getElementById('imagem');
const imagens = ['img/imagem1.jpg', 'img/imagem2.jpg', 'img/imagem3.jpg']; // Substitua pelos seus caminhos
let indiceImagem = 0;

function proximoImagem() {
    indiceImagem = (indiceImagem + 1) % imagens.length;
    imagem.src = imagens[indiceImagem];
    document.getElementById("textoInicial").innerHTML= "HELLO WORLD!"
}

function imagemAnterior() {
    indiceImagem = (indiceImagem - 1 + imagens.length) % imagens.length; // Garante que o índice não seja negativo
    imagem.src = imagens[indiceImagem];
    document.getElementById("textoInicial").innerHTML= "Olá Mundo!"
}

function styleChange(){
    const image = document.getElementById("imagem")
    if (image.style.display != "flex") {
        image.style.display = "flex";
    }
};

function hiddenImage(){
    const image = document.getElementById("imagem")
    if (image.style.display != "none") {
        image.style.display = "none";
    }
};

