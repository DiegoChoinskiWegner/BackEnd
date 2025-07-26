 
"""Problemas
Iterar sobre uma lista e modificá-la ao mesmo tempo: Quando você usa for x in nums1 e remove elementos com remove(),
isso altera os índices da lista, resultando em elementos não removidos corretamente.

Soma direta de m + n para redefinir o tamanho de nums1: Isso não está manipulando corretamente os 
elementos relevantes já definidos por m em nums1."""        
        

// Solução A - Complexidade O(m+n) - 100% testes - 17.74MB de memória

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
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

func merge(self, nums1 List[int], m int, nums2 List[int], n int) None{
	last :=	m + n - 1
	m -= 1
	n -= 1

	while m>=0 && n >=0{
		if nums[m]
	}
}