package Livraria.src.console;

import Livraria.src.baseDados.Banco;
import Livraria.src.entidades.*;
import Livraria.src.negocio.ClienteNegocio;
import Livraria.src.negocio.PedidoNegocio;
import Livraria.src.negocio.ProdutoNegocio;
import Livraria.src.utilidade.LeitoraDados;

import java.util.Optional;

public class Start {

    private static Cliente clienteLogado = null;

    private static Banco banco = new Banco();

    private static ClienteNegocio clienteNegocio = new ClienteNegocio(banco);
    private static PedidoNegocio pedidoNegocio = new PedidoNegocio(banco);
    private static ProdutoNegocio produtoNegocio = new ProdutoNegocio(banco);

    /**
     * Método utilitário para inicializar a aplicação.
     * @param args Parâmetros que podem ser passados para auxiliar na execução.
     */
    public static void main(String[] args) {

        System.out.println("Bem vindo ao e-Compras");

        String opcao = "";

        while(true) {

            if (clienteLogado == null) {

                System.out.println("Digite o cpf:");

                String cpf = "";
                cpf = LeitoraDados.lerDado();

                identificarUsuario(cpf);
            }

            System.out.println("Selecione uma opção:");
            System.out.println("1 - Cadastrar Livro");
            System.out.println("2 - Excluir Livro");
            System.out.println("3 - Consultar Livro");
            //TODO Desafio: Consultar Livro(nome)
            System.out.println("4 - Cadastrar Caderno");
            System.out.println("5 - Excluir Caderno");
            //TODO Desafio: Consultar Caderno(matéria)
            System.out.println("6 - Consultar Caderno");
            System.out.println("7 - Fazer pedido");
            System.out.println("8 - Excluir pedido");
            System.out.println("9 - Consultar pedido");
            //TODO Desafio: Consultar Pedido(código)
            System.out.println("10 - Listar produtos");
            System.out.println("11 - Listar pedidos");
            System.out.println("12 - Deslogar");
            System.out.println("13 - Sair");

            opcao = LeitoraDados.lerDado();

            switch (opcao) {
                //Cadastrar Livro
                case "1":
                    Livro livro = LeitoraDados.lerLivro();
                    produtoNegocio.salvar(livro);
                    break;
                //Excluir Livro
                case "2":
                    System.out.println("Digite o código do livro");
                    String codigoLivro = LeitoraDados.lerDado();
                    produtoNegocio.excluir(codigoLivro);
                    break;
                //Consultar Livro
                case "3":
                    //TODO Cadastrar Caderno
                    break;
                
                //Cadastrar Caderno
                case "4":
                    Caderno caderno = LeitoraDados.lerCaderno();
                    produtoNegocio.salvar(caderno);
                    break;
                
                //Excluir Caderno 
                case "5":
                    Pedido pedido = LeitoraDados.lerPedido(banco);
                    Optional<Cupom> cupom = LeitoraDados.lerCupom(banco);

                    if (cupom.isPresent()) {
                        pedidoNegocio.salvar(pedido, cupom.get());
                    } else {
                        pedidoNegocio.salvar(pedido);
                    }
                    break;

                //Consultar Caderno    
                case "6":
                    
                    break;

                //Fazer pedido
                case "7":
                    
                    break;

                //Excluuir pedido
                case "8":
                    System.out.println("Digite o código do pedido");
                    String codigoPedido = LeitoraDados.lerDado();
                    pedidoNegocio.excluir(codigoPedido);
                    break;

                //Consultar pedido
                case "9":
                    
                    break;
                
                //Listar produtos - Pronto
                case "10":
                    produtoNegocio.listarTodos();
                    break;
               
                //Listar pedidos - Pronto
                case "11":
                    pedidoNegocio.listarTodos();
                    break;
                
                //Deslogar - PRONTO
                case "12":
                    System.out.println(String.format("Volte sempre %s!", clienteLogado.getNome()));
                    clienteLogado = null;
                    break;
                
                //Sair - PRONTO
                case "13":
                    System.out.println("Aplicação encerrada.");
                    System.exit(0);
                    break;

                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        }
    }

    /**
     * Procura o usuário na base de dados.
     * @param cpf CPF do usuário que deseja logar na aplicação
     */
    private static void identificarUsuario(String cpf) {

        Optional<Cliente> resultado = clienteNegocio.consultar(cpf);

        if (resultado.isPresent()) {

            Cliente cliente = resultado.get();
            System.out.println(String.format("Olá %s! Você está logado.", cliente.getNome()));
            clienteLogado = cliente;
        } else {
            System.out.println("Usuário não cadastrado.");
            System.exit(0);
        }
    }
}
