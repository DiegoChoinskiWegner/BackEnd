package controller;

import java.util.Scanner;

import model.Animal;
import repository.AnimalRepository;

public class AnimalController {
    
    static Scanner input = new Scanner(System.in);

    public static void adicionaAnimal(){
        int novoId = AnimalRepository.ANIMAIS.size()+1;
        System.out.println("Digite a Familia que o animal pertence:\n");
        String novoFamilia = input.nextLine();
        System.out.println("Digite a Espécie do animal:\n");
        String novaEspecie = input.nextLine();
        System.out.println("Digite o nome do Som que o animal emite:\n");
        String novoSonsVocais = input.nextLine();
        
        AnimalRepository.addAnimal(new Animal(novoId, novoFamilia, novaEspecie, novoSonsVocais));
    }


}
