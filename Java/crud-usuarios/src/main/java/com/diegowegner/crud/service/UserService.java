package com.diegowegner.crud.service;

import com.diegowegner.crud.model.User;
import com.diegowegner.crud.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    //READ METHOD
    public List<User> getList(){
        return this.userRepository.findAll();
    }

    //CREATE METHOD
    public User addUser(User user){
        return this.userRepository.save(user);
    }

    //UPDATE METHOD
    public User editUser(User user){
        return this.userRepository.save(user);
    }

    //DELETE METHOD
    public void deleteUser(String id) {
        this.userRepository.deleteById(id);
    }

}
