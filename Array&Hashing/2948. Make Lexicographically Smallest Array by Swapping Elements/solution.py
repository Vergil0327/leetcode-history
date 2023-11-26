
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        v2idx = defaultdict(list)
        for i, num in enumerate(nums):
            v2idx[num].append(i)
        counter = Counter(nums)
        
        res = [-1]*n
        arr = sorted(set(nums))
        i = 0
        while i < len(arr):
            indices = []
            num = []
            j = i
            while j < len(arr) and (not num or arr[j] <= num[-1]+limit):
                num.append(arr[j])
                indices.extend(v2idx[arr[j]])
                j += 1
            
            indices.sort()
            k = 0
            for x in num:
                while counter[x]:
                    res[indices[k]] = x
                    k += 1
                    counter[x] -= 1
                
            i = j
        return res
