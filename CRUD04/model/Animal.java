package model;

public class Animal{

    private int id;
    private String familia;
    private String especie;
    private String sonsVocais;


    //Método Construtor
    public Animal(int id, String familia, String especie, String sonsVocais){
        this.id = id;
        this.familia = familia;
        this.especie = especie;
        this.sonsVocais = sonsVocais;

    }

    

    //GETTER and SETTER dos Atributos
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFamilia() {
        return familia;
    }
    
    public void setFamilia(String familia) {
        this.familia = familia;
    }

    public String getEspecie() {
        return especie;
    }

    public void setEspecie(String especie) {
        this.especie = especie;
    }

    public String getSonsVocais() {
        return sonsVocais;
    }

    public void setSonsVocais(String sonsVocais) {
        this.sonsVocais = sonsVocais;
    }

    
}