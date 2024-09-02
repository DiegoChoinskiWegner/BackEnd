package Contas;

/*Transformação da classe em Interface
**

public interface Conta {
    private int agencia
    public String getCliente(); == Cliente.getNome()
    public int getTipo();
    public int getNumero();
    public int getSaldo();

}

**
**
**
**
**
*/
public class Conta {
    private int agencia;
    private int numero;
    private String beneficiario;
    public double saldo;
    

    public Conta(int agencia, int numero, String beneficiario, double saldo){
        this.agencia = agencia;
        this.numero = numero;
        this.beneficiario = Usuarios.Cliente.getNome();
        this.saldo = saldo;

    }
    

    public int getAgencia() {
        return agencia;
    }
    
    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }
    
    public int getNumero() {
        return numero;
    }
    
    public void setNumero(int numero) {
        this.numero = numero;
    }
    
    public String getBeneficiario() {
        return beneficiario;
    }
    
    public void setBeneficiario(String beneficiario) {
        this.beneficiario = beneficiario;
    }

    public double getSaldo(){
        return saldo;
    }

    public void setSaldo(double saldo){
        this.saldo = saldo;
    }

    //public double updateSaldo(double saldo, double novoSaldo){
    //    this.saldo = saldo + novoSaldo;
    //    return saldo;
    //}


}
