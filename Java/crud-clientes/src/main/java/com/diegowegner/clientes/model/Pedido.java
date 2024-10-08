package com.diegowegner.clientes.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@Data
@AllArgsConstructor
@Document(collection = "compras")
public class Pedido {
    @Id
    private String id;
    private Cliente cliente;
    private List<Produto> produtos;
    private double valor;
}
