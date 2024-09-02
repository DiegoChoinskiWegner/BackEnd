package Main;

import java.util.Scanner;

import Dados.Cadastro;
import Empresa.Funcionario;
import Teste.TesteCadastrro;

public class Main {

    static boolean ordering = true;

    public static void menu(){
        System.out.println("Bem vindo ao cadastro de funcionários.\t");
        System.out.println("01 - Listar todos os funcionários.");
        System.out.println("02 - Cadastrar funcionário.");
        System.out.println("03 - Pesquisar funcionário.");
        System.out.println("04 - Alterar funcionário.");
        System.out.println("05 - Excluir funcionário.");        
        System.out.println("06 - Sair.\t");        
    }

    public static void main(String[] args) {
        
        menu();

        Scanner input = new Scanner(System.in);

        do{
            int choice = input.nextInt(); 
            switch(choice){
            case 1:
                Cadastro.listarFuncionarios(Cadastro.listaFuncionarios);
                menu(); 
                break;
                
            case 2:
                Cadastro.cadastrarFuncionario();
                System.out.println("\nCadastro de funcionarios");
                break;
                
            case 3:
                //Cadastro.pesquisarFuncionario(null);
                System.out.println("\nPesquisa de funcionarios");
                break;
                
                
            case 4:
                //consulta();
                System.out.println("\nAltera funcionario");
                break;
                
            case 5:
                //consulta();
                System.out.println("\nExclui funcionario");
                break;
                
            case 6:
                //consulta();
                System.out.println("\nSair do programa");
                break;
            
            case 7:
                TesteCadastrro.teste1();
                break;
            
            default:
                System.out.println("\nOpção inválida.");

               
            }
        }while(ordering);   
    }
}

