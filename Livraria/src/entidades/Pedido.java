package Livraria.src.entidades;

import Livraria.src.entidades.Produto;
import Livraria.src.entidades.Cliente;
import Livraria.src.entidades.Cupom;
import java.util.ArrayList;
import java.util.List;


public class Pedido {
    
    //variaveis privadas
    private String codigo;
    private Cliente cliente;
    private List<Produto> produtos;
    private double total;

    //Método Construtor
    /**
     * @param produtos
     */
    public Pedido(List<Produto> produtos) {
        this.produtos = new ArrayList<>();
    }
    
    public String getCodigo() {
        return codigo;
    }
    
    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    
    public List<Produto> getProdutos() {
        return produtos;
    }

    public void setProdutos(List<Produto> produtos) {
        this.produtos = produtos;
    }

    public double getTotal() {
        return total;
    }

    public void setTotal(double total) {
        this.total = total;
    }
    
    //Método de exclusão de Pedido


    //Método auxiliar de produtos comprados
    private String getProdutosComprados(){
        StringBuilder produtos = new StringBuilder();
        produtos.append("[");
        for(Produto produto : getProdutos()){
            produtos.append(produto.toString());
            produtos.append("Qtd:");
            produtos.append(produto.getQuantidade());
            produtos.append(" ");
        }
        produtos.append("]");

        return produtos.toString();
    }

    //Método toString para representar a classe em forma de texto
    @Override
    public String toString(){
        return "Pedido{" +
               "codigo=" + codigo +
               ", cliente=" + cliente +
               ", produtos=" + getProdutosComprados() +
               ", total=" + total +
               "}";
    }
}
