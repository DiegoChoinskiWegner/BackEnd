package Empresa;

public class Funcionario {
    
    private int id;
    private String nome;
    private String email;
    private String telefone;
    private String cargo;

    public int getId(){
        return id;
    }

    public void setId(int id){
        this.id = id;
    }

    public String getNome(){
        return nome;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }

    public String getEmail(){
        return email;
    }
    
    public void setEmail(String email){
        this.email = email;
    }
    
    public String getTelefone(){
        return telefone;
    }
    
    public void setTelefone(String telefone){
        this.telefone = telefone;
    }
    
    public String getCargo(){
        return cargo;
    }

    public void setCargo(String cargo){
        this.cargo = cargo;
    }

    @Override
    public String toString(){
        return "Funcionario [id = " + id + ", nome = " + nome + ", email = " + email + ", telefone = " + telefone + ", cargo = " + cargo + "]";
    }

    public Funcionario(int id, String nome, String email , String telefone, String cargo){
        super();
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.telefone = telefone;
        this.cargo = cargo;
    }
}