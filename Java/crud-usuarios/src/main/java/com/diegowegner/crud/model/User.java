package com.diegowegner.crud.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "users")
public class User {
    @Id
    private String id;
    private String nome;
    private int idade;
    private String cpf;
    private String email;

}
