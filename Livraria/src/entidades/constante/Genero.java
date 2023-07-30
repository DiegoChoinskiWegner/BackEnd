package Livraria.src.entidades.constante;

public enum Genero {
    
    //Generos de livros vendidos
    DRAMA (15),
    SUSPENSE (10),
    ROMANCE (5),
    COMEDIA (3);

    private double fator;

    //Metodo Construtor, @param fator - valor que influencia no frete;
    Genero(double fator){
        this.fator = fator / 100;
    }

    public double getFator() {
        return fator;
    }

}
