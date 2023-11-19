class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10**9 + 7
        
        x = y = 0
        for i in range(max(a.bit_length()-1, n), n-1, -1):
            if (a>>i)&1:
                x |= 1<<i
        for i in range(max(b.bit_length()-1, n), n-1, -1):
            if (b>>i)&1:
                y |= 1<<i
        
        for i in range(n-1, -1, -1):
            bit1 = (a>>i)&1
            bit2 = (b>>i)&1
            
            if (bit1 and bit2) or (not bit1 and not bit2):
                x |= 1<<i
                y |= 1<<i
                
            if x > y:
                y |= 1<<i
            else:
                x |= 1<<i
        return x*y%mod
