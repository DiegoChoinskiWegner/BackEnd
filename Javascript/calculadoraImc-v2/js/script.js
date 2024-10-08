function start() {
  var buttonCalculateImc = document.querySelector('#button-calculate-imc');
  buttonCalculateImc.addEventListener('click', handleButtonClick);

  var inputWeight = document.querySelector('#input-weight');
  var inputHeight = document.querySelector('#input-height');

  weight = inputWeight;
  height = inputHeight;
  
  handleButtonClick();
}

var inputWeight = document.querySelector('#input-weight');
var inputHeight = document.querySelector('#input-height');


weight = inputWeight;
height = inputHeight;

function calculateImc(weight, height) {
  var resultadoImc = weight / (height * height);
  return resultadoImc
}




function rangeImc(){ 
  var resultado = Number(calculateImc(weight, height)); 

  if(resultado >= 16 & resultado < 16.9){
    return 'Muito abaixo do Peso'
  } 
  else if (resultado >= 17 && resultado <= 18.4){
    return "Abaixo do Peso";
  } 
  else if (resultado >= 18.5 && resultado <= 24.9){
    return  "Peso Normal";
  } 
  else if (resultado >= 25 && resultado <= 29.9){
    return  "Acima do Peso";
  } 
  else if (resultado >= 30 && resultado <= 34.9){
    return  'Obesidade grau I';
  } 
  else if (resultado >= 35 && resultado <= 40){
    return  "Obesidade grau II";
  } 
  else if (resultado >= 40.1){
    return  "Obesidade grau III";
  } 
  else if(resultado <= 16){
    return  "IMC inválido";
  } 
  else {
    return "teste"
  }

}


function handleButtonClick() {
  var imcResult = document.querySelector('#imc-result');
  var imcRange = document.querySelector('#imc-range');

  var weight = Number(inputWeight.value);
  var height = Number(inputHeight.value);

  

  var imc = calculateImc(weight, height);
  var formattedImc = imc.toFixed(2).replace('.', ',');
  imcResult.textContent = formattedImc + " " + typeof(imc);
  
  var rangeResult = String(rangeImc());
  imcRange.innerText = rangeResult + " " + typeof(rangeResult);
  
}

start();
