package Contas;

public class ContaCorrente /*implements Conta*/{
    private int tipo;
    private int numero;
    private int saldo;
    private int chequeEspecial;

    public int getTipo(){
        return tipo;
    }

    public void setTipo(int tipo){
        this.tipo = tipo;
    }

    public int getNumero(){
        return numero;
    }

    public void setNumero(int numero){
        this.numero = numero;
    }

    public int getSaldo(){
        return saldo;
    }

    public void setSaldo(int saldo){
        this.saldo = saldo;
    }

    public int getChequeEspecial(){
        return chequeEspecial;
    }

    public void setChequeEspecial(int chequeEspecial){
        this.chequeEspecial = chequeEspecial;
    }




}
