"""
# Intuition

1. 首先, 想到可以先計算出max_length, 這可以greedily去找, 從nums[0]開始, 找出max number of alternating sign.
    - 但因為後續要找出這個alternating sequence的max sum, 所以用個list去紀錄sequence[i]的正負號
2. 再來就簡單了, 用雙指針找出符合sequence[i]正負號的最大nums[i]即可

note. 空間上應該能更進一步優化, 只紀錄一開始的正負號跟max sequence length即可
"""


sign = lambda x: 1 if x > 0 else -1

t = int(input()) 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    sequence_sign = [sign(nums[0])]
    for i in range(1, n):
        if (x := sign(nums[i])) != sequence_sign[-1]:
            sequence_sign.append(x)
 
    j = res = 0
    cur = nums[0]
    for i in range(n):
        s = sign(nums[i])
        if s == sequence_sign[j]:
            cur = max(cur, nums[i])
        else:
            res += cur

            j += 1
            cur = nums[i]
    res += cur # don't forget to sum up last value
    print(res)