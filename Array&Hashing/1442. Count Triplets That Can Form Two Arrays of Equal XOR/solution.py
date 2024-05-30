class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        prexor = [0]
        for num in arr:
            prexor.append(prexor[-1]^num)
        
        count = Counter()
        count[0] = 1
        res = 0
        for i in range(n):
            mid = prexor[i+1]
            for j in range(i+1, n):
                right = prexor[j+1]^prexor[i+1]
                left = right^mid
                res += count[left]
            count[mid] += 1
        return res
