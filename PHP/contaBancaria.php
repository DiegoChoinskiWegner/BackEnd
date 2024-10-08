<?php

namespace App;

class ContaBancaria
{
    private string $banco ;
    private string $nomeTitular;
    private string $numeroAgencia;
    private string $numeroConta;
    private float $saldo;

    public function __construct(string $banco, string $nomeTitular, string $numeroAgencia, string $numeroConta, float $saldo){
        $this->banco = $banco;
        $this->nomeTitular = $nomeTitular;
        $this->numeroAgencia = $numeroAgencia;
        $this->numeroConta = $numeroConta;
        $this->saldo = $saldo;
    }

    public function getBanco(string $banco){
        return $this->banco;        
    }

    public function setBanco() : void{
    $this->banco = $banco;      
    }

    public function getNomeTitular(string $NomeTitular){
        return $this->nomeTitular;
    }

    public function setNomeTitular() : void{
        $this->nomeTitular = $nomeTitular;
    }

    public function getNumeroAgencia(string $numeroAgencia){
        return $this->numeroAgencia;
    }

    public function setNumeroAgencia() : void{
        $this->numeroAgencia = $numeroAgencia;
    }

    public function getNumeroConta(string $numeroConta){
        return $this->numeroConta;
    }

    public function setNumeroConta() : void{
        $this->numeroConta = $numeroConta;
    }

    public function getSaldo(string $saldo){
        return $this->saldo;
    }

    public function setSaldo() : void{
        $this->saldo = $saldo;
    }







    public function exibirDadosDaConta(): array{
        return[
            'banco' => $this->banco,
            'nomeTitular'=> $this->nomeTitular,
            'numeroAgencia'=> $this->numeroAgencia,
            'numeroConta'=> $this->numeroConta,
            'saldo' => $this->saldo
        ];
        

    }
}

$contaBancaria = new ContaBancaria();
var_dump($contaBancaria->exibirDadosDaConta());