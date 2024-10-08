package BancoDados;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class exemploConexao{
  
  public static void main(String[]args){
    String url = "jdbc:mysql://localhost:3306/BancoDigital";
    String usuario = "DiegoWegner";
    String senha = "BB749serpro?";

    try {
      //carrega o driver do jdbc
      Class.forName("com.mysql.cj.jdbc.Driver");
      
      //Cria a conexão com o BD
      Connection conexao = DriverManager.getConnection(url, usuario, senha);

      conexao.close();
    } catch (ClassNotFoundException | SQLException e){
      e.printStackTrace();
    }
  }

}