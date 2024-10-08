package com.diegowegner.clientes.service;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.model.Pedido;
import com.diegowegner.clientes.repository.PedidoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PedidoService {
    @Autowired
    private PedidoRepository pedidoRepository;

    public List<Pedido> getPedido() {
        return this.pedidoRepository.findAll();
    }

    public Pedido addPedido(Pedido pedido) {
        return this.pedidoRepository.save(pedido);
    }

    public Pedido updatePedido(Pedido pedido) {
        return this.pedidoRepository.save(pedido);
    }

    public void deletePedido(String id) {
        this.pedidoRepository.deleteById(id);
    }
}
