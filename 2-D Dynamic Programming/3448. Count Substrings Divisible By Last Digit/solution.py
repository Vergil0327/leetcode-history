class Solution:
    def countSubstrings(self, s: str) -> int:        
        n = len(s)
        def count(nums: List[int], digit: int) -> int:
            count = [0] * digit
            count_new = [0] * digit

            # base case: r=0 (餘數為0), empty string: "", 亦即本身就能被digit整除
            # "" + "ABCDi" = "ABCDi" % d == 0的意思
            count[0] = 1

            res = remainder = 0
            for i in range(n):
                # update count[r]
                for r in range(digit):
                    count_new[r*10 % digit] += count[r]

                # Swap arrays to prepare for next iteration
                count, count_new = count_new, [0]*digit

                # 以nums[i]結尾的餘數
                remainder = (remainder * 10 + nums[i]) % digit

                # 如果nums[i]就是last digit `d`, 計入個數
                if nums[i] == d:
                    res += count[remainder]

                # "XXXi" 自身計入個數
                # Add current prefix as a new way to reach this remainder
                count[remainder] += 1
            return res

        nums = [int(d) for d in s]

        res = 0
        for d in range(1, 10):
            res += count(nums, d)
        return res
