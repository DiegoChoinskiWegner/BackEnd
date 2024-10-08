package Livraria.src.entidades;

import Livraria.src.entidades.constante.Genero;

public class Livro extends Produto{
    
    public Livro(String codigo, Double preco, int quantidade) {
        super(codigo, preco, quantidade);
        
    }

    //variaveis privadas
    private String nome;

    private Genero genero;

    //métodos
    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public Genero getGenero(){
        return genero;
    }

    public void setGenero(Genero genero){
        this.genero = genero;
    }

    //Método exportado com override
    @Override
    public double calcularFrete(){
        return (getPreco() * getQuantidade()) * (1+genero.getFator());  
    }

    //repensar saída, melhorar escrita
    @Override
    public String toString(){
        return  "Livro{" +
                "nome='" + nome + '\'' +
                ", genero=" + genero + '\'' +
                ", codigo='" + getCodigo() + '\'' +
                ", preço='" + getPreco() + '\'' +
                '}';
    }
}
