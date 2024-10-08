package com.diegowegner.compras.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.List;

@Data
@AllArgsConstructor
@Document(collection = "pedidos") //nome da tabela
public class Pedido {

    @Id
    private String id;
    private String filial;
    private ArrayList<Produto> produtos;
    private int valorCompra;




}
