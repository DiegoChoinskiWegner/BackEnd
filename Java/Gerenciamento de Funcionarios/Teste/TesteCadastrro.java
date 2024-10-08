package Teste;

import Dados.Cadastro;
import Empresa.Funcionario;

public class TesteCadastrro {
    public static void teste1(){
        Funcionario novoFuncionario = new Funcionario(01,"Diego", "diego@empresa.com.br", "(41)988776655", "Diretor");
        Cadastro.listaFuncionarios.add(novoFuncionario);
    }
}
