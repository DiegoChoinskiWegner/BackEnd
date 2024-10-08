package com.diegowegner.clientes.repository;

import com.diegowegner.clientes.model.Cliente;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ClienteRepository extends MongoRepository<Cliente, String> {
}
