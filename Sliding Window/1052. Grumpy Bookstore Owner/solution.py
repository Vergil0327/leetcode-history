class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        l = r = 0
        res = curr = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        while r < n:
            if grumpy[r] == 1:
                curr += customers[r]
            r += 1

            while l < r and r-l > minutes:
                if grumpy[l] == 1:
                    curr -= customers[l]
                l += 1
            res = max(res, curr)
        return res