from math import sqrt

def generatePrimeUntil(n: int):
    isPrime = [0, 0] + [1] * (n-2)

    for i in range(2, int(sqrt(n))+1):
        if not isPrime[i]: continue
        # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
        for j in range(i*i, n, i):
            isPrime[j] = 0


"""
在檢查質數時, 2 和 3 已經被排除了。
剩下的質數都可以寫成 6k±1 的形式(k 為正整數）, 也就是 5, 7, 11, 13, 17, 19, ...
這是因為除了 2 和 3 以外, 其他數字如果不是 6k±1, 一定能被 2 或 3 整除。

所以, i 從 5 開始, 每次加 6, 分別檢查 i 和 i+2(也就是 6k-1 和 6k+1), 這樣就能有效率地跳過所有明顯不是質數的數字, 只檢查有可能是質數的數字。

這樣可以大幅減少不必要的整除判斷, 提高質數判斷的效率。
"""
def is_prime(self, num: int) -> bool:
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
