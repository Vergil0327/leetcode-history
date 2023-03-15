class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = int(1e9+7)
        arr.sort()
        n = len(arr)
        res = 0

        # [X X] X X X X X X [X X X] X X X X X
        #    i      j        k
        for j in range(1, n-1):
            i, k = 0, n-1
            while i < j:
                countI, countK = 1, 0

                # count duplicate
                while i+1 < j and arr[i] == arr[i+1]:
                    countI += 1
                    i += 1
                while j < k and arr[k] > target-arr[i]-arr[j]:
                    k -= 1
                # start from here,  arr[i] + arr[j] + arr[k] might be equal to target
                while j < k and arr[k] == target-arr[i]-arr[j]:
                    countK += 1
                    k -= 1
                res += countI * countK
                res %= MOD
                i += 1
        return res
    
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = int(1e9+7)
        counter = Counter(arr)
        nums = sorted(list(counter.keys()))
        n = len(nums)
        
        res = 0
        for i, num in enumerate(nums):
            j = i
            k = n-1
            SUM = target-num
            while j <= k:
                currSUM = nums[j] + nums[k]
                if currSUM > SUM:
                    k -= 1
                elif currSUM < SUM:
                    j += 1
                else:
                    if i < j < k:
                        res += counter[nums[i]] * counter[nums[j]] * counter[nums[k]]
                        res %= MOD
                    elif i == j < k:
                        # C counter[nums[i]] 取 2
                        res += math.comb(counter[nums[i]], 2) * counter[nums[k]]
                        res %= MOD
                    elif i < j == k:
                        res += counter[nums[i]] * math.comb(counter[nums[k]], 2)
                        res %= MOD
                    else: # i == j == k
                        res += math.comb(counter[nums[j]], 3)
                        res %= MOD
                    j, k = j+1, k-1
        return res