package Usuarios;

public class Cliente {
   
    

    private static String nome;
    private String sobrenome;
    private String cpf;
    private String telefone;
    
    public Cliente(String nome, String sobrenome, String cpf, String telefone){
        Cliente.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.telefone = telefone;
    }

    public static String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        Cliente.nome = nome;
    }

    public String getSobrenome(){
        return sobrenome;
    }
    
    public void setSobrenome(String sobrenome){
        this.sobrenome = sobrenome;
    }

    public String getCpf(){
        return cpf;
    }
    
    public void setCpf(String cpf){
        this.cpf = cpf;
    }

    public String getTelefone(){
        return telefone;
    }

    public void setTelefone(String telefone){
        this.telefone = telefone;
    }

}

