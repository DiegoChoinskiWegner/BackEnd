package repository;

import model.Animal;
import java.util.ArrayList;

public class AnimalRepository {
     
    public static ArrayList<Animal> ANIMAIS = new ArrayList<>();

    public static void addAnimal(Animal animal){
         ANIMAIS.add(animal);
    }

    public static void updateAnimal(int id, Animal animal){
        ANIMAIS.add(0, null);
    }

    public static void listarAnimais(){
        System.out.println(ANIMAIS);
    }

    public static void deletaAnimal(int id){
        ANIMAIS.remove(0);
    }

   
}