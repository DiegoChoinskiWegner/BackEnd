package com.diegowegner.crud.controller;

import com.diegowegner.crud.model.User;
import com.diegowegner.crud.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> get(){
        return this.userService.getList();
    }

    @PostMapping
    public User post(@RequestBody User user){
        return this.userService.addUser(user);
    }

    @PutMapping
    public User put(@RequestBody User user, @RequestParam String id){
        user.setId(id);
        return this.userService.editUser(user);
    }

    @DeleteMapping
    public String delete(@RequestParam String id){
        this.userService.deleteUser(id);
        return "Usuário deletado com sucesso";
    }

}
