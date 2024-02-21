class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        presum1 = list(accumulate(nums1, initial=0))
        presum2 = list(accumulate(nums2, initial=0))
        diff = [x-y for x, y in zip(presum1, presum2)]

        n = len(diff)
        rightMax = [diff[-1]]*n
        for i in range(n-2, -1, -1):
            rightMax[i] = max(diff[i], rightMax[i+1])

        rightMin = [diff[-1]]*n
        for i in range(n-2, -1, -1):
            rightMin[i] = min(diff[i], rightMin[i+1])

        leftMax = [diff[0]]*n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], diff[i])

        leftMin = [diff[0]]*n
        for i in range(1, n):
            leftMin[i] = min(leftMin[i-1], diff[i])

        score = max(presum1[-1], presum2[-1])
        for i in range(n-1):
            # score = presum1[n] - (diff[right+1]-diff[left])
            score = max(score, presum1[-1] - (rightMin[i+1]-leftMax[i]))

        for i in range(n-1):
            # score = presum2[n] + (diff[right+1]-diff[left])
            score = max(score, presum2[-1] + (rightMax[i+1]-leftMin[i]))
        return score
    

class Solution2:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(A, B):
            res = cur = 0
            for i in range(len(A)):
                cur = max(0, cur + A[i] - B[i])
                res = max(res, cur)
            return res

        return max(sum(nums2) + kadane(nums1, nums2), sum(nums1) + kadane(nums2, nums1))