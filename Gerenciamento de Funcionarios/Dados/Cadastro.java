package Dados;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import Empresa.Funcionario;

public class Cadastro {

    public static List<Funcionario> listaFuncionarios = new ArrayList<Funcionario>();

    //"01 - Listar todos os funcionários.
    public static void listarFuncionarios(List<Funcionario> listaFuncionarios){
        if(listaFuncionarios != null){
            System.out.println(listaFuncionarios);
        } else {
            System.out.println("Não há funcionários cadastrados") ;
        }
    }




    //"02 - Cadastrar funcionário.
    public static void cadastrarFuncionario(){
        Funcionario novoFuncionario = new Funcionario();
        Cadastro.listaFuncionarios.add(novoFuncionario);
        System.out.println("Funcionário cadastrado com sucesso!");
    }

    //"03 - Pesquisar funcionário.
    public static void pesquisarFuncionario(Funcionario funcionarios){
        System.out.println("digite o numero de id do funcionário");
        Scanner entrada = new Scanner(System.in); 
        int idPesquisa = entrada.nextInt();

        if(idPesquisa == funcionarios.getId()){

        }
    }
    
    //"04 - Alterar funcionário.
    public static void alterarFuncionario(){
        
    }
    
    //"05 - Excluir funcionário.        
    public static void excluirFuncionario(){
        
    }
    
    //"06 - Sair.

}
