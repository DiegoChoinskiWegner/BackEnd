package Livraria.src.entidades;

public class Cupom {
    
    //variaveis privadas
    private String codigo;
    private int desconto;

    
    //construtor??
    public Cupom(String codigo, int desconto){
        this.codigo = codigo;
        this.desconto = desconto;
    }

    
    //Métodos
    public String getCodigo(){
        return codigo;
    }

    public void setCodigo(String codigo){
        this.codigo = codigo;
    }

    public int getDesconto(){
        return desconto;
    }

    public void setDesconto(int desconto){
        this.desconto = desconto;
    }
}
