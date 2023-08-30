class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def findNextPermutation(num):
            nums = list(num)
            n = len(num)
            # 先找出跟哪個位置交換會變得更大
            i = n-1
            while i >= 1 and nums[i] <= nums[i-1]:
                i -= 1

            if i == 0: return sorted(num)

            i -= 1 # 這是我們要交換的位置

            # 找到比num[i]更大的數交換
            j = n-1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

            # 後面位數排序成最小
            nums[i+1:] = sorted(nums[i+1:])
            return "".join(nums)

        kth = num
        for _ in range(k):
            kth = findNextPermutation(kth)
        
        return self.calculateSwaps(kth, num)
    
    def calculateSwaps(self, dst, src):
        arr = list(src)
        n = len(arr)

        res = 0
        for i in range(n):
            cnt = 0
            for j in range(n):
                if arr[j] == "#": continue # already swap to front correct position
                if arr[j] != dst[i]:
                    cnt += 1
                else:
                    arr[j] = "#"
                    break
            res += cnt
        return res
