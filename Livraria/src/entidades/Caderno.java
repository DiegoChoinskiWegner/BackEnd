package Livraria.src.entidades;

import Livraria.src.entidades.constante.QtdMaterias;

public class Caderno extends Produto {

    public Caderno(String codigo, Double preco, int quantidade) {
        super(codigo, preco, quantidade);
    }
    
    private QtdMaterias qtdMaterias;

    public QtdMaterias getQtdMaterias(){
        return qtdMaterias;
    }

    public void setQtdMaterias(QtdMaterias qtdMaterias){
        this.qtdMaterias = qtdMaterias;
    }

    //Método importado com override da classe mãe "Produto"
    @Override
    public double calcularFrete(){
        return (getPreco() * getQuantidade()) * (1+qtdMaterias.getFator());  
    }

    //repensar saída, melhorar escrita
    @Override
    public String toString(){
        return  "Caderno{" +
                "Quantidade de Matérias=" + qtdMaterias +
                ", codigo='" + getCodigo() + '\'' +
                ", preço='" + getPreco() + '\'' +
                '}';
    }
    
}
