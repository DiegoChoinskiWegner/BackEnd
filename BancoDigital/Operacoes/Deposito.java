package Operacoes;

import java.util.Scanner;

import Contas.Conta;

public class Deposito {
    //Adiciona Saldo a conta do beneficiario logado
    
    public double depositarValor(Conta conta, Conta agencia, Conta saldo){
        Scanner valorScanner = new Scanner(System.in);
        double novoSaldo = valorScanner.nextDouble();
        updateSaldo(conta.saldo, novoSaldo);
            return conta.saldo = conta.saldo + novoSaldo;

    }

    private void updateSaldo(double saldo, double novoSaldo) {
    }

    
}
