package Contas;

import java.util.List;

import Contas.Conta;

//para o caso de não possuir BD

public interface IRepositorioConta {

	public boolean salvaConta(Conta conta);
	public boolean deletarContaPorNumero(int numero);
	public List<Conta> listarConta();
	public boolean alteraConta(Conta conta);
	
}