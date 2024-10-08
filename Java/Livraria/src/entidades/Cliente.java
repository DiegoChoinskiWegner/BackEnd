package Livraria.src.entidades;

public class Cliente {
    
    //variaveis privadas
    private String nome;
    private String cpf;

    public Cliente() {
        this.nome = "Diego Wegner";
        this.cpf = "08122029965";
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

}


