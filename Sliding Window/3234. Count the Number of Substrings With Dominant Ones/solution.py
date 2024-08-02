class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        right_one = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if s[i] == "1":
                right_one[i] = right_one[i+1]+(s[i]=="1")

        ones = sum(1 for ch in s if ch == "1")
        res = 0
        for require_zero in range(1, ceil(sqrt(ones))+1): # 從1開始, 不包含"0"的substr並不適用以下邏輯
            l = r = zero = 0
            while r < n:
                zero += int(s[r] == "0")
                r += 1
                while l < r and zero >= require_zero:
                    one = r-l-zero
                    if right_one[r] + one >= zero*zero:
                        need_ones = max(0, zero*zero-one) # zero*zero-one 可能出現負數
                        res += max(0, right_one[r] - need_ones + 1) # 可能出現負數
                    zero -= int(s[l] == "0")
                    l += 1

        # contribution of consecutive ones
        for i in range(n):
            res += right_one[i]
        return res
