package com.diegowegner.compras.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "produtos") //nome da tabela
public class Produto {
    @Id
    private String id;
    private String nome;
    private String tamanho;
    private String cor;
    private Double preco;
}
