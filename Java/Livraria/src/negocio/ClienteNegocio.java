package Livraria.src.negocio;

import Livraria.src.baseDados.Banco;
import Livraria.src.entidades.Cliente;
import java.util.Optional;

public class ClienteNegocio {
    
    private Banco bancoDados;

    public ClienteNegocio(Banco bancoDados){
        this.bancoDados = bancoDados;
    }

    public Optional<Cliente> consultar(String cpf){
        if (bancoDados.getCliente().getCpf().equals(cpf)){
            return Optional.of(bancoDados.getCliente());
        } else {
            return Optional.empty();
        }
    }

    //Tentativa cadastro de cliente
    public void cadastrar(String nome){
        if (bancoDados.getCliente().getNome().equals(nome)){
            System.out.println("Cliente já cadastrado");
        } else {
            
        }
    }

}
