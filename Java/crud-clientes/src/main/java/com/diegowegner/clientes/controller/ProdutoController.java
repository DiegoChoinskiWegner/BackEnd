package com.diegowegner.clientes.controller;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.model.Produto;
import com.diegowegner.clientes.service.ClienteService;
import com.diegowegner.clientes.service.PedidoService;
import com.diegowegner.clientes.service.ProdutoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/produto")
public class ProdutoController {
    @Autowired
    private ProdutoService produtoService;

    @GetMapping
    public List<Produto> get(){ return this.produtoService.getProduto();}

    @PostMapping
    public Produto post(@RequestBody Produto produto){ return this.produtoService.addProduto(produto);}

    @PutMapping
    public Produto put(@RequestBody Produto produto, @RequestParam String id){
        produto.setId(id);
        return this.produtoService.updateProduto(produto);
    }

    @DeleteMapping
    public String delete(@RequestParam String id){
        this.produtoService.deleteProduto(id);
        return "Produto deletado!";
    }

    //get mapping chamando service

    //putmapping

    //post

    //delete
}
