package Livraria.src.negocio;

import Livraria.src.baseDados.Banco;
import Livraria.src.entidades.Pedido;
import Livraria.src.entidades.Produto;
import java.util.Optional;

public class ProdutoNegocio {

    //variaveis
    private Banco bancoDados;

    public ProdutoNegocio(Banco banco){
        this.bancoDados = banco;
    }

    //Metódo para salvar novo Produto na loja(Livro ou Caderno)
    public void salvar(Produto novoProduto){
        String codigo = "PR%04d";
        codigo = String.format(codigo, bancoDados.getProdutos().length);
        novoProduto.setCodigo(codigo);

        //caso de produto já cadastrado
        boolean produtoRepetido = false;
        for (Produto produto: bancoDados.getProdutos()){
            if(produto.getCodigo() == novoProduto.getCodigo()){
                produtoRepetido = true;
                System.out.println("Produto já cadastrado!");
                break;
            }
        }

        //caso de produto não cadastrado
        if(!produtoRepetido){
            this.bancoDados.adicionarProduto(novoProduto);
            System.out.println("Produto cadastrado com sucesso !");
        }
    }

    //Consulta item
    public Optional<Produto> consultar(String codigo) {

        for (Produto produto: bancoDados.getProdutos()) {

            if (produto.getCodigo().equalsIgnoreCase(codigo)) {
                return  Optional.of(produto);
            }
        }

        return Optional.empty();
    }

    /**
     * Exclui um pedido a partir de seu código de rastreio.
     * @param codigo Código do pedido
     */
    public void excluir(String codigo) {

        int pedidoExclusao = -1;
        for (int i = 0; i < bancoDados.getPedidos().length; i++) {

            Pedido pedido = bancoDados.getPedidos()[i];
            if (pedido.getCodigo().equals(codigo)) {
                pedidoExclusao = i;
                break;
            }
        }

        if (pedidoExclusao != -1) {
            bancoDados.removerPedido(pedidoExclusao);
            System.out.println("Pedido excluído com sucesso.");
        } else {
            System.out.println("Pedido inexistente.");
        }
    }

    //Consulta e lista todos os produtos
    public void listarTodos(){
        if(bancoDados.getProdutos().length == 0){
            System.out.println("Não há produtos cadastrados!");
        } else {
            for (Produto produto: bancoDados.getProdutos()){
                System.out.println(produto.toString());
            }

        }   
    }

}
