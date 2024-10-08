package com.diegowegner.clientes.controller;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.service.ClienteService;
import com.diegowegner.clientes.service.ProdutoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/clientes")
public class ClienteController {

    @Autowired
    private ClienteService clienteService;

    @GetMapping
    public List<Cliente> get(){ return this.clienteService.getCliente();}

    @PostMapping
    public Cliente post(@RequestBody Cliente cliente){ return this.clienteService.addCliente(cliente);}

    @PutMapping
    public Cliente put(@RequestBody Cliente cliente, @RequestParam String id){
        cliente.setId(id);
        return this.clienteService.updateCliente(cliente);
    }

    @DeleteMapping
    public String delete(@RequestParam String id){
        this.clienteService.deleteCliente(id);
        return "Usuário deletado!";
    }

}
