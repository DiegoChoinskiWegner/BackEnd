package com.diegowegner.crud.repository;

import com.diegowegner.crud.model.User;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UserRepository extends MongoRepository<User, String> {
}
