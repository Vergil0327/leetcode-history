class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for num in nums[1:]:
            kk = num-nums[0]
            if kk == 0: continue
            if kk%2 != 0: continue
            
            paired = defaultdict(int)
            for num in nums:
                if num-kk in paired:
                    paired[num-kk] -= 1
                    if paired[num-kk] == 0:
                        del paired[num-kk]
                else:
                    paired[num] += 1

            if len(paired) == 0: # found k
                k = kk//2

                paired = defaultdict(int)
                for num in nums:
                    if num in paired:
                        paired[num] -= 1
                        if paired[num] == 0:
                            del paired[num]
                        continue
                        
                    res.append(num+k)
                    paired[num+kk] += 1
                    
                return res
