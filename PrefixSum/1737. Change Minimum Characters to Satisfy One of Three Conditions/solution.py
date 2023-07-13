class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        n = 26
        arr1, arr2 = [0]*n, [0]*n
        for ch in a:
            arr1[ord(ch)-ord("a")] += 1
        for ch in b:
            arr2[ord(ch)-ord("a")] += 1

        presum1 = [0] * (n+1)
        presum2 = [0] * (n+1)
        for i in range(1, n+1):
            presum1[i] = presum1[i-1] + arr1[i-1]
            presum2[i] = presum2[i-1] + arr2[i-1]
        
        res = presum1[n]-max(arr1) + presum2[n]-max(arr2) # 3rd condition - one distinct character
        for i in range(n):
            # set arr1[i] as upperlimit
            # sum(arr1[i+1:]) + sum(arr2[:i+1])
            if i < n-1:
                res = min(res, presum1[n]-presum1[i+1] + presum2[i+1])
            
            # set lowerlimit of arr1 is arr1[i]
            # sum(arr1[:i]) + sum(arr2[i:])
            if i >= 1:
                res = min(res, presum1[i] + presum2[n]-presum2[i])
            
        return res
