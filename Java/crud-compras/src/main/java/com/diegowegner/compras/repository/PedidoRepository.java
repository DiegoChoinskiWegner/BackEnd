package com.diegowegner.compras.repository;

import com.diegowegner.compras.model.Pedido;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PedidoRepository extends MongoRepository<Pedido, String> {
}
