from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        slist = SortedList()
        n = len(nums)
        l, r = 0, 0 # [l, r)
        while r < n:
            num = nums[r]
            r += 1
            
            while r-l-1 > indexDiff:
                slist.remove(nums[l])
                l += 1

            if r>l+1:
                i = slist.bisect_left(num)
                # sorted list = [XXXX i XXXX], binary search: list[i] >= num 
                # check list[i]-num <= diff
                # also check num-list[i-1] <= diff
                if i != len(slist) and abs(slist[i]-num) <= valueDiff: return True
                if i > 0 and abs(num-slist[i-1]) <= valueDiff: return True
            slist.add(num)
        return False

# Bucket sort
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v // valueDiff, 1) if valueDiff else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= valueDiff:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > indexDiff:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - indexDiff] // valueDiff if valueDiff else nums[i - indexDiff]]

        return False