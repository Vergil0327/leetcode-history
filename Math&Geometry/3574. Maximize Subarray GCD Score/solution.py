class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count2 = []
        for num in nums:
            cnt = 0
            while num%2 == 0:
                num //= 2
                cnt += 1
            count2.append(cnt)

        res = 0
        for i in range(n):
            GCD = 0
            
            min_count2 = inf
            cnt = 0
            for j in range(i, n):
                GCD = nums[j] if i == j else gcd(GCD, nums[j])

                if count2[j] < min_count2:
                    min_count2 = count2[j]
                    cnt = 1
                elif count2[j] == min_count2:
                    cnt += 1

                length = j-i+1

                res = max(res, length * GCD * pow(2, int(cnt <= k)))
        return res