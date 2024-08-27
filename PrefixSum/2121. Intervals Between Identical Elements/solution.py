class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        v2idx = defaultdict(list)
        for i in range(n):
            v2idx[arr[i]].append(i)

        res = [0] * n
        for indices in v2idx.values():
            presum = list(accumulate(indices, initial=0))
            m = len(indices)
            for i in range(m):
                k = indices[i]
                res[k] = i * k - presum[i] + (presum[m]-presum[i]) - (m-i) * k
        return res