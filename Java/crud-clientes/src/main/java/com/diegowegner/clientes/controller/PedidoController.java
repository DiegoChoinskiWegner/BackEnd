package com.diegowegner.clientes.controller;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.model.Pedido;
import com.diegowegner.clientes.service.ClienteService;
import com.diegowegner.clientes.service.PedidoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/pedido")
public class PedidoController {

    @Autowired
    private PedidoService pedidoService;

    @GetMapping
    public List<Pedido> get(){ return this.pedidoService.getPedido();}

    @PostMapping
    public Pedido post(@RequestBody Pedido pedido){ return this.pedidoService.addPedido(pedido);}

    @PutMapping
    public Pedido put(@RequestBody Pedido pedido, @RequestParam String id){
        pedido.setId(id);
        return this.pedidoService.updatePedido(pedido);
    }

    @DeleteMapping
    public String delete(@RequestParam String id){
        this.pedidoService.deletePedido(id);
        return "Pedido deletado!";
    }
}
