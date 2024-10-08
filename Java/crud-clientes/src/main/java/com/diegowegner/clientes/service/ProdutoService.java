package com.diegowegner.clientes.service;

import com.diegowegner.clientes.model.Cliente;
import com.diegowegner.clientes.model.Produto;
import com.diegowegner.clientes.repository.ProdutoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProdutoService {
    @Autowired
    private ProdutoRepository produtoRepository;

    public List<Produto> getProduto() {
        return this.produtoRepository.findAll();
    }

    public Produto addProduto(Produto produto) {
        return this.produtoRepository.save(produto);
    }

    public Produto updateProduto(Produto produto) {
        return this.produtoRepository.save(produto);
    }

    public void deleteProduto(String id) {
        this.produtoRepository.deleteById(id);
    }
}
