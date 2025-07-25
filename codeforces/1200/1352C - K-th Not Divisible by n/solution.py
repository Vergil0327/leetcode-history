# Goal: Find the k-th positive integer not divisible by n.
# Since the sequence of numbers not divisible by n is monotonically increasing,
# we can use binary search to efficiently find the k-th such number.

# For a given number `num`, we calculate how many numbers up to `num` are not divisible by n:
# - Numbers divisible by n: `num // n`
# - Numbers not divisible by n: `num - num // n`
# - If this count is >= k, the answer is at most `num`, so we search lower.
# - If this count is < k, the answer is larger than `num`, so we search higher.
# - Special case: If count equals k but `num` is divisible by n, we need to search lower
#   to find the correct number not divisible by n.
# 對於當前猜測的值`mid`來說, 被n整除的數有`mid//n`個
# 所以`mid - mid//n`就代表`mid`前面這麼多個數不被`n`整除
# - 如果這數目`>= k`, `mid`可能是合法的, 然後繼續往下找
#     - 如果`mid==k`但是`mid%n == 0`, 我們仍會往下找到`mid-1`這個不被n整除的答案
# - 如果這數目`< k`, `mid`肯定不合法, 我們得更往上找

t = int(input())

def count(num, n):
    divisible = num//n
    return num - divisible

def findKth(n, k):
    l, r = 1, n*k
    while l < r:
        mid = l + (r-l)//2
        cnt = count(mid, n)
        if cnt >= k:
            r = mid
        else:
            l = mid+1
    return l

for _ in range(t):
    n, k = list(map(int, input().split()))
    print(findKth(n, k))
