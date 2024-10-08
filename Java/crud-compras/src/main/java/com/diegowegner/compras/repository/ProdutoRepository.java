package com.diegowegner.compras.repository;

import com.diegowegner.compras.model.Produto;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ProdutoRepository extends MongoRepository<Produto, String> {
}
