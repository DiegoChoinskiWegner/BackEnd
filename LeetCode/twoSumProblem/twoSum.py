"""
PROBLEM = Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
# Primeira solução proposta
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for nums in nums:
            i=0
            j=1
            if nums[i] + nums[j] == target:
                return i, j
            else: 
                if j > nums.len():
                    i = i+1
                else:
                    j = j+1
"""

"""
------ Ajustes da solução
-- Utilização de enumerate ao invés de iterara sobre o próprio array.

-- Nesse caso você está sobrescrevendo a variável nums com cada elemento.
for nums in nums:
 
-- Neste caso você itera sobre o array(nums) recuperando os valores de indice(i) e valor da posição(num)
for i, num in enumerate(nums):


--Correção de como usar o méthodo len()
if j > nums.len():

if j > len(nums):
"""


# Solução proposta com IA
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Armazenar os números da lista como chaves e seus respectivos índices como valores.
        num_index_map = {}

        #Itera sobre o indice e valor dos dados da lista nums
        for i, num in enumerate(nums):
            # complement será o numero que falta para se chegar ao target
            complement = target - num
            # compara o complement está no dicionário, se não estiver é adicionado.
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[num] = i
        return []

"""
Criação do dicionário: Um dicionário num_index_map é criado para armazenar os números da lista como chaves e seus respectivos índices como valores.
Iteração sobre a lista: A função itera sobre cada número num na lista nums usando enumerate para obter tanto o índice i quanto o valor do número.
Cálculo do complemento: Para cada número num, o complemento complement é calculado subtraindo num do target. O complemento é o outro número que, quando somado a num, daria o target.
Verificação no dicionário: Se o complement já está presente no dicionário num_index_map, significa que já encontramos o outro número que, quando somado a num, dá o target. Portanto, retornamos os índices dos dois números.
Atualização do dicionário: Se o complement não está presente no dicionário, adicionamos o atual num e seu índice i ao dicionário para futuras verificações.
Retorno de lista vazia: Se nenhum par de números for encontrado que satisfaça a condição, a função retorna uma lista vazia, indicando que não há solução.
"""



### CASO DE USO 1 ###

"""
Sistemas de Recomendação
Imagine um sistema de recomendação de produtos em uma loja online. O sistema poderia utilizar o problema Two-Sum para encontrar produtos que frequentemente são comprados juntos.

Como isso funciona:

Criação de um dicionário: Cada produto é associado a um ID numérico único.
Registro de compras: Ao registrar uma compra, armazenamos os IDs dos produtos adquiridos em uma lista.
Encontrando pares de produtos frequentemente comprados juntos: Para cada compra, calculamos a soma dos IDs dos produtos. Se essa soma já foi encontrada anteriormente, significa que há outros clientes que compraram esses mesmos produtos juntos.
Recomendação: Ao visualizar um produto, o sistema pode sugerir outros produtos que frequentemente são comprados junto com ele, baseado nos pares de produtos encontrados anteriormente.
"""

### OUTROS CASOS DE USO ###

"""
Análise de dados: Identificar padrões em grandes conjuntos de dados, como encontrar pares de números que se complementam para um determinado valor.
Processamento de imagens: Detectar bordas em imagens, onde a diferença de intensidade entre dois pixels adjacentes é igual a um determinado valor.
Criptografia: Alguns algoritmos de criptografia utilizam o conceito de somas para realizar operações de cifragem e decifragem.
"""

"""
E se ao invés de um target, tivessemos uma lista de targets??
"""
##CONTINUAR IMPLEMENTAÇÂO
class SolutionMoreSum:
    def moreSum(self, nums: List[int], target: List[int]) -> List[int]:
        num_index_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[num] = i
        return []