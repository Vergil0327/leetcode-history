# s.length <= 800 => 800 1-bit at most
# reduce_step[i]: required steps for number which contains `i` 1-bit to be reduced to 1

reduce_step = [0] * 801
# reduce_step[1] = 0 # base case
for i in range(2, 801):
    reduce_step[i] = reduce_step[i.bit_count()] + 1

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        @cache
        def dfs(i, setBits, smallerThanS):
            if i == len(s):
                if setBits > 0 and reduce_step[setBits]+1 <= k and smallerThanS:
                    return 1
                return 0

            end = 2 if smallerThanS else int(s[i])+1
            res = 0
            for d in range(0, end):
                res += dfs(i+1, setBits + int(d == 1), smallerThanS or d < int(s[i]))
            
            return res% 1_000_000_007
        return dfs(0, 0, False)