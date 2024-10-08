package com.diegowegner.clientes.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "clientes")
public class Cliente {

    @Id
    private String id;
    private String nome;
    private String sobrenome;
    private String telefone;
    private String email;
    private String profissao;
}
