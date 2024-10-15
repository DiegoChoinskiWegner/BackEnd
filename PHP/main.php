<?php


//PHP

//Variaveis
$nome = 'Diego';
$t = 0;

//Variavel de variaval
$Diego = 'Wegner';

//concatenar é com . e não +
echo 'o meu nome é ' .$nome;
echo 'o meu nome é ' .$$Diego;
//compara valores

//Array
$arr = ['banana', 'maca', 'pera'];

if ($nome !== 'Diego'){
    echo 'teste de comparação';
}else{
    echo 'teste dois';
}

//Loop
for ($i = 0; $i < 6; $i++){
    echo $i;
    echo '<hr>';
}

while($t < 6){
    echo $t;
    echo '<hr>';
    $t++;
}

//Funções 
function printNumero($n){
    echo $n;
}

printNumero(30);

//Classes
class Pessoa{
    public $nome;
    public $cpf;
    public $rg;
    public function __construct($nome, $cpf, $rg){ 
        $this->nome = $nome;
        $this->cpf = $cpf;
        $this->rg = $rg;
    }

    public function printPessoa(){
        echo $this->nome;
        echo $this->cpf;
        echo $this->rg;
    }



}

$pessoa = new Pessoa("Diego", '98736457', '27635422')



?>