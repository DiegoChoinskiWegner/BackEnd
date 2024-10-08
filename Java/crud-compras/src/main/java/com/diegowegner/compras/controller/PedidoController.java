package com.diegowegner.compras.controller;

import com.diegowegner.compras.model.Pedido;
import com.diegowegner.compras.model.Produto;
import com.diegowegner.compras.service.PedidoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/pedidos")
public class PedidoController {
    @Autowired
    private PedidoService pedidoService;

    @GetMapping
    public List<Pedido> get(){
        return this.pedidoService.getPedidos();
    }

    @PostMapping
    public Pedido post(@RequestBody Pedido pedido){
        return this.pedidoService.addPedido(pedido);
    }

    @PutMapping
    public Pedido put(@RequestBody Pedido pedido, @RequestParam String id){
        pedido.setId(id);
        return this.pedidoService.updatePedido(pedido);
    }

    @DeleteMapping
    public Pedido delete(@RequestParam String id){
        this.pedidoService.deletePedido(id);
    }

    public Pedido adicionaProduto(@RequestBody Produto produto, List<Produto>){
        return null;
    }

}
