```py
count = Counter([0])

res = presum = 0
for i in range(n):
    presum = (presum+nums[i])%k
    res += count[presum]
    count[presum] += 1
```

想到prefix sum + hashmap, 但解決不了遇到相同subarray的問題.
ex. [2,2,2,2,2,2], k=6 => {2,2,2}, {2,2,2}

但有個條件還沒用到: `sorted in non-descending order`
如此一來, 要遇到subarray重複計算的情況, 只會在連續相同數subarray裡發生, ex. [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], [3,3,3,3,3,3,3,3,3,3]
所以對於擁有連續相同數值的subarray, 如果我們能進行**de-duplication**, 扣掉重複之後應該就會是答案

所以用雙指針找出identical number subarray
```py
i = 0
while i < n:
    j = i
    while j < n and nums[j] == nums[i]:
        j += 1
    
    L = j-i
    for length in range(1, L):
        if (length * nums[i]) % k == 0:
            res -= L - length # the number of subarray with size = `length`

    i = j
```

確認每種長度大小的subarray的貢獻, 扣除掉duplication後
即得到最終答案