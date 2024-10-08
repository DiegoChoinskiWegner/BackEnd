package com.diegowegner.clientes.repository;

import com.diegowegner.clientes.model.Pedido;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PedidoRepository extends MongoRepository<Pedido, String> {
}
