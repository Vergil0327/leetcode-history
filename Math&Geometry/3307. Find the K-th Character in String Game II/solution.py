from math import ceil, log2

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # n = 1
        # op = 0
        # while n < k:
        #     n *= 2
        #     op += 1
        op = ceil(log2(k))
        n = pow(2, op)

        shift = 0
        for i in range(op-1, -1, -1):
            if k > n//2: # 代表是透過操作得到的
                if operations[i] == 1:
                    shift = (shift+1)%26

                k = k-n//2
            # else:
            #     do nothing

            n //= 2
        
        return chr(ord("a") + shift)