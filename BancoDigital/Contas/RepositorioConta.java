package Contas;

import java.util.ArrayList;
import java.util.List;

import Contas.Conta;


//Para o caso de não possuir BD


public class RepositorioConta implements IRepositorioConta {

    //Implementa lista para as contas criadas
	List<Conta> listaContas = new ArrayList<Conta>();

    //Adiciona a conta nova na lista.
	@Override
	public boolean salvaConta(Conta conta) {
    
		try {

			listaContas.add(conta);

		} catch (Exception e) {
			return false;
		}

		return true;
	}

    //Deleta conta pelo numero da conta
	@Override
	public boolean deletarContaPorNumero(int numero) {

		for (Conta conta : listaContas) {
			if (conta.getNumero() == numero) {
				listaContas.remove(conta);
			}
		}

		return false;
	}


    //Lista todas as contas cadastradas
	@Override
	public List<Conta> listarConta() {
		return this.listaContas;
	}

    //Altera conta  pelo numero
	@Override
	public boolean alteraConta(Conta conta) {

		for (Conta conta1 : listaContas) {
			if (conta1.getNumero() == conta.getNumero()) {
				
				listaContas.remove(conta1);
				listaContas.add(conta);
			}
		}
		return false;
	}

}