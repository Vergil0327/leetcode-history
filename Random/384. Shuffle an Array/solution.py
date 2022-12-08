# get two random index and swap
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        i = random.randint(0, len(self.nums)-1)
        j = random.randint(0, len(self.nums)-1)
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Shuffle algorithm: O(n)
# correct random algorithm must generate n! possibilities
# Proof:
# for nums[0], we got n possibilities from randomly generating index within [0, n-1]
# for nums[1], we got n-1 possibilities from randomly generating index within [1, n-1]
# for nums[2], we got n-2 possibilities from randomly generating index within [2, n-1]
# ... and so on
# therefore, we got n * (n-1) * ... * 1 = n! possibilities
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums.copy()
        n= len(nums)
        for i in range(len(nums)):
            # ! generate random value from [i, n-1]
            r = random.randint(i, n-1)
            nums[i], nums[r] = nums[r], nums[i]
        return nums
