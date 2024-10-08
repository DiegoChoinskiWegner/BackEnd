import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        System.out.println("Seja bem Vindo ao CRUD Animais\n");
        System.out.println("Escolha uma opção do menu abaixo\n");
        System.out.println("01- Cadastrar animal.");
        System.out.println("02- Editar animal.");
        System.out.println("03- Deletar animal.");
        System.out.println("04- Ver todos os animais cadastrados.");
        System.out.println("05- Sugestão de melhoria.");
        System.out.println("06- Sair.\n");

        try (Scanner entrada = new Scanner(System.in)) {
            switch (entrada.nextLine()) {
                case "1":
                    System.out.println("Animal Cadastrado");
                    break;
            
                case "2":
                    System.out.println("Animal Cadastrado");
                    break;
            
                case "3":
                    System.out.println("Animal Cadastrado");
                    break;
            
                case "4":
                    System.out.println("Animal Cadastrado");
                    break;
            
                case "5":
                    System.out.println("Animal Cadastrado");
                    break;
            
                case "6":
                    System.out.println("Animal Cadastrado");
                    break;
            
                default:
                    break;
            }
        }
        


    }

    
}
