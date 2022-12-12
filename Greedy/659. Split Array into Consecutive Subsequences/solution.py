class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        nums.sort()
        need = defaultdict(int)
        for num in nums:
            if counter[num] == 0: continue

            if need[num] > 0: # if there is a valid seq., keep append valid num after
                need[num] -= 1
                counter[num] -= 1
                need[num+1] += 1 # we can keep appending num after
            else: # try to create new valid seq.
                if counter[num] > 0 and counter[num+1] > 0 and counter[num+2] > 0:
                    counter[num] -= 1
                    counter[num+1] -= 1
                    counter[num+2] -= 1
                    # use hashmap to store tail of valid seq.
                    # if num+3 exists, we can keep appending num from num+3
                    need[num+3] += 1
                else: # we can't append to any valid seq. and also can't create new seq.
                    return False

        return all(v == 0 for v in counter.values())