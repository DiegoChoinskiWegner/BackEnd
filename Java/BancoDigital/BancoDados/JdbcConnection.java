package BancoDados;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JdbcConnection{
  
  public static void main(String[]args){
    String url = "jdbc:mysql://localhost:3306/BancoDigital";
    String usuario = "DiegoWegner";
    String senha = "BB749serpro?";

    try {
      //carrega o driver do jdbc
      Class.forName("com.mysql.cj.jdbc.Driver");
      
      //Cria a conexão com o BD
      Connection conexao = DriverManager.getConnection(url, usuario, senha);

      //Criação das tabelas necessárias
      //String tabelaClientes = "CREATE TABLE IF NOT EXISTS clientes (cliente_id INT PRIMARY KEY, cliente_nome VARCHAR(20) FOREIGN KEY, cliente_sobrenome VARCHAR(35) FOREIGN KEY, cliente_cpf VARCHAR(12), cliente_telefone VARCHAR(14))";
      //String tabelaContas = "CREATE TABLE IF NOT EXISTS contas (conta_numero VARCHAR(7) PRIMARY KEY FOREIGN KEY, conta_agencia VARCHAR(3), conta_benficiario VARCHAR(50), conta_saldo ****FLOAT16)";
      //String tabelaMovimentacoes = "CREATE TABLE IF NOT EXISTS movimentacoes (movimenta_id INT PRIMARY KEY, movimenta_conta_entrada VARCHAR(11), movimenta_conta_saida VARCHAR(11), movimenta_conta_banco VARCHAR(7), movimenta_tipo_transacao INT, movimenta_valor_movimentado INT )";
     
      //conexao.createStatement().execute(tabelaClientes);
      //conexao.createStatement().execute(tabelaContas);
      //conexao.createStatement().execute(tabelaMovimentacoes);

      conexao.close();
    } catch (ClassNotFoundException | SQLException e){
      e.printStackTrace();
    }
  }

}