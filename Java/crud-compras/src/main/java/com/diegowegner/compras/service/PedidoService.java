package com.diegowegner.compras.service;

import com.diegowegner.compras.model.Pedido;
import com.diegowegner.compras.repository.PedidoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PedidoService {
    @Autowired
    private PedidoRepository pedidoRepository;

    //CREATE
    public Pedido addPedido(Pedido pedido){return this.pedidoRepository.save(pedido);}

    //READ
    public List<Pedido> getPedidos(){ return this.pedidoRepository.findAll();}

    //UPDATE
    public Pedido updatePedido(Pedido pedido){return this.pedidoRepository.save(pedido);}

    //DELETE
    public void deletePedido(String id){
        this.pedidoRepository.deleteById(id);
    }


}
