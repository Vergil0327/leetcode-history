class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]:
        #         pos.append(i)
        pos = [i for i in range(len(nums)) if nums[i]]

        # tot = 0
        # for i in range(k):
        #     tot += abs(pos[i]-pos[k//2])
        # res = tot
        res = tot = sum(abs(pos[i]-pos[k//2]) for i in range(k))

        n = len(pos)
        for i in range(n-k):
            mid = i+k//2
            tot -= abs(pos[i]-pos[mid])
            tot += abs(pos[i+k]-pos[mid+1])
            tot += k//2 * (pos[mid+1]-pos[mid])
            tot -= (k-1-k//2) * (pos[mid+1]-pos[mid])
            res = min(res, tot)

        offset = sum(abs(i-k//2) for i in range(k))
        return res - offset