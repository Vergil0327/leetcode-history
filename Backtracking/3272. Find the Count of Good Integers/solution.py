class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        m = (n+1)//2

        self.visited = set()
        def count(num):
            s = str(num)
            n = len(s)
            if n == 1: return 1

            digits = [0] * 10
            for i in range(n):
                digits[int(s[i])] += 1
            
            tot = factorial(n)
            for i in range(len(digits)):
                cur = digits[i]
                if cur != 0:
                    tot //= factorial(cur) # remove duplicate permutations

            key = tuple(digits)
            if key in self.visited: return 0
            self.visited.add(key)

            if digits[0] == 0: return tot

            leading_0_perm = factorial(n-1)
            leading_0_perm //= factorial(digits[0]-1)

            for i in range(1, len(digits)):
                cur = digits[i]
                if cur != 0:
                    leading_0_perm //= factorial(cur)
            return tot-leading_0_perm

        def dfs(i, num):
            if i == m:
                return count(num) if num%k == 0 else 0

            has_center = 0 if n%2==1 and i == m-1 else 1
            res = 0
            for d in range(10):
                if i == 0 and d == 0: continue # no leading zeros
                cur = d*pow(10, i) + d*pow(10, n-i-1)*has_center
                res += dfs(i+1, (num + cur))
            return res

        return dfs(0, 0)

# solution by @lee215
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        m = (n + 1) // 2
        
        res = 0
        seen = set()
        for half in range(10 ** (m - 1), 10 ** m):
            palindrome = str(half) + str(half)[::-1][n % 2:]
            key = ''.join(sorted(palindrome))
            if int(palindrome) % k == 0 and key not in seen:
                seen.add(key)
                count = Counter(palindrome)
                
                cnt = (n - count['0']) * factorial(n - 1)
                for ch, freq in count.items():
                    cnt //= factorial(freq)
                res += cnt
        return res