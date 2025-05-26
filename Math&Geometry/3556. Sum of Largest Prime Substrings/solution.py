class Solution:
    def is_prime(self, num: int) -> bool:
        """
        在檢查質數時, 2 和 3 已經被排除了。
        剩下的質數都可以寫成 6k±1 的形式(k 為正整數）, 也就是 5, 7, 11, 13, 17, 19, ...
        這是因為除了 2 和 3 以外, 其他數字如果不是 6k±1, 一定能被 2 或 3 整除。

        所以, i 從 5 開始, 每次加 6, 分別檢查 i 和 i+2(也就是 6k-1 和 6k+1), 這樣就能有效率地跳過所有明顯不是質數的數字, 只檢查有可能是質數的數字。

        這樣可以大幅減少不必要的整除判斷, 提高質數判斷的效率。
        """
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)

        primes = set() # avoid duplicate
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring[0] == '0' and len(substring) > 1:
                    continue
                num = int(substring)
                if self.is_prime(num):
                    primes.add(num)
        primes = sorted(primes, reverse=True)
        return sum(primes[:3]) if len(primes) >= 3 else sum(primes)