class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        length = 1
        while n < k:
            n = n*10+1
            length += 1

        modulos = set()
        while n%k not in modulos:
            if n%k == 0: return length
            modulos.add(n%k)

            n = (n*10+1)%k
            length += 1
        return -1