package com.diegowegner.clientes.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "produtos")
public class Produto {

    @Id
    private String id;
    private String categoria;
    private String nome;
    private double preco;
}
