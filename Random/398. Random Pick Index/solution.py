# space: O(n)
class Solution:
    # time: O(n)
    def __init__(self, nums: List[int]):
        self.pool = defaultdict(list)
        for i, num in enumerate(nums):
            self.pool[num].append(i)
    # time: O(1)
    def pick(self, target: int) -> int:
        return random.choice(self.pool[target])


# reservoir sampling
# space: O(1)
class Solution_TLE:
    # time: O(1)
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    # time: O(n)
    def pick(self, target: int) -> int:
        n = len(self.nums)
        cnt = 0
        pick = -1
        for i in range(n):
            if self.nums[i] != target: continue
            if random.randint(0, cnt) == 0: # for i-th target, 1/i to choose
                pick = i
            cnt += 1

        return pick
