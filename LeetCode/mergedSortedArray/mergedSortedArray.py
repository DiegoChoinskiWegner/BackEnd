# Primeira solução proposta - Complexidade O((m+n)log(m+n)) - Passou em 30/59 testes
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = m + n

        itens_to_remove = []
        for x in nums1:
            if x == 0 or x is None:
                itens_to_remove.append(x)
                
        for x in itens_to_remove:
            nums1.remove(x)

        for x in nums2:
            nums1.append(x)
        
        nums1.sort()
        
"""Problemas
Iterar sobre uma lista e modificá-la ao mesmo tempo: Quando você usa for x in nums1 e remove elementos com remove(),
isso altera os índices da lista, resultando em elementos não removidos corretamente.

Soma direta de m + n para redefinir o tamanho de nums1: Isso não está manipulando corretamente os 
elementos relevantes já definidos por m em nums1."""        
        

# Solução proposta por IA - Complexidade O(m+n) - 100% testes - 17.74MB de memória
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1  # Última posição de nums1
        m -= 1
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        
        # Preenche com elementos restantes de nums2, se houver
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1



"""Caso de Uso 1 
1. Mesclagem de Resultados Paginados em Sistemas de Busca
Cenário
Imagine um sistema de busca, como o usado por um e-commerce, que consulta diferentes fontes de dados (bancos de dados locais e externos) para encontrar produtos. Cada fonte de dados retorna uma lista ordenada de resultados baseados em relevância ou preço. Para apresentar uma única lista ao usuário, o sistema precisa combinar esses resultados de forma eficiente, preservando a ordenação.

Exemplo
Resultados de fonte A: [10, 20, 30] (em ordem de preço crescente)
Resultados de fonte B: [15, 25, 35]
Solução: Mesclar ambas as listas ordenadas para exibir [10, 15, 20, 25, 30, 35] ao usuário.
Essa abordagem minimiza o tempo de resposta sem precisar reordenar todos os dados do zero, melhorando a experiência do usuário.
"""

"""Caso de Uso 2
2. Mesclagem de Logs de Sistema Ordenados por Tempo
Cenário
Em sistemas distribuídos, diferentes servidores ou serviços geram logs de eventos com timestamps ordenados. Para realizar análises ou depurar problemas, é necessário combinar esses logs em uma única linha do tempo ordenada.

Exemplo
Logs do servidor 1: [(10:00, "Start"), (10:05, "Ping"), (10:10, "Stop")]
Logs do servidor 2: [(10:02, "Connect"), (10:06, "Error")]
Solução: Mesclar os logs para produzir:
[ (10:00, "Start"), (10:02, "Connect"), (10:05, "Ping"), (10:06, "Error"), (10:10, "Stop") ]
Esse tipo de mesclagem permite reconstruir a sequência de eventos global, essencial para rastreamento de falhas ou análise de desempenho.
"""