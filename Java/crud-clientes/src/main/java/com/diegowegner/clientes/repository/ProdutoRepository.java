package com.diegowegner.clientes.repository;

import com.diegowegner.clientes.model.Produto;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ProdutoRepository extends MongoRepository<Produto, String> {
}
