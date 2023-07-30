package Livraria.src.entidades;

public abstract class Produto {
    //variaveis privadas 
    private String codigo;
    private double preco;
    private int quantidade;

    //métodos
    public Produto(String codigo, Double preco, int quantidade){
        this.codigo = codigo;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    public String getCodigo(){
        return codigo;
    }

    public void setCodigo(String codigo){
        this.codigo = codigo;
    }

    public double getPreco(){
        return preco;
    }

    public void setPreco(Double preco){
        this.preco = preco;
    }

    public int getQuantidade(){
        return quantidade;
    }

    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }

    //método para calculo de Frete
    public abstract double calcularFrete();  
}
