package com.diegowegner.clientes.service;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.repository.ClienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ClienteService {

    @Autowired
    private ClienteRepository clienteRepository;

    public List<Cliente> getCliente() {
        return this.clienteRepository.findAll();
    }

    public Cliente addCliente(Cliente cliente) {
        return this.clienteRepository.save(cliente);
    }

    public Cliente updateCliente(Cliente cliente) {
        return this.clienteRepository.save(cliente);
    }

    public void deleteCliente(String id) {
        this.clienteRepository.deleteById(id);
    }
}
