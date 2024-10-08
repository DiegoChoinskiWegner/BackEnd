package Livraria.src.baseDados;

import Livraria.src.entidades.Produto;
import Livraria.src.entidades.Pedido;
import Livraria.src.entidades.Cliente;
import Livraria.src.entidades.Cupom;
import java.util.ArrayList;
import java.util.List;


public class Banco {
    
    private List <Produto> produtos;

    private List<Pedido> pedidos;
    
    private List<Cupom> cupons;
    
    //private List<Frete> frete;

    private Cliente clientes;

    public Banco() {

        this.produtos = new ArrayList<>();
        
        this.pedidos = new ArrayList<>();
        
        //this.frete = new ArrayList<>();
        
        this.clientes = clientes;
        
        
        this.cupons = new ArrayList<>();
        cupons.add(new Cupom("CUPOM2", 2));
        cupons.add(new Cupom("CUPOM5", 5));
        cupons.add(new Cupom("CUPOM7", 7));
    }

    public Cliente getCliente() {
        return (Cliente) clientes;
    }

    //public Cliente[] getClientes() return (new Cliente cliente)

    public Cupom[] getCupons() {
        return cupons.toArray(new Cupom[cupons.size()]);
    }
    
    public Pedido[] getPedidos() {
        return pedidos.toArray(new Pedido[pedidos.size()]);
    }
    
    public Produto[] getProdutos() {
        return produtos.toArray(new Produto[produtos.size()]);
    }

    public void adicionarProduto (Produto produto) {
        produtos.add(produto);
    }

    /*public void removerProduto(Produto codigProduto){
        if(){

        } else {

        }
    }*/


    public void adicionarPedido (Pedido pedido) {
        pedidos.add(pedido);
    }

    //corrigir para Adicionar Cliente
    public void adicionarCliente(Cliente cliente) {
        clientes.add(cliente);
    }

    public void removerPedido(int pedidoExclusao) {
        
    }

    /*/Corrigir
    public void adicionarProduto (Produto produto) {
        produtos.add(produto);
    }*/

    
}