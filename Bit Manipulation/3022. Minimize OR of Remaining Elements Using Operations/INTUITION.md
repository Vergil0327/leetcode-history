# Intuition

1. 求min(OR(nums))
2. 可以透過nums[i]&nums[i+1]來降低possible value of the bitwiase OR of nums
3. 1 <= nums.length <= 10^5
4. 0 <= nums[i] < 2^30 => 最多29個bit
5. 從時間複雜度來看感覺是要 O(N * 29bit)
6. 由於要minimum possible value, 所以要盡可能利用k operations優先消除高位bit (from MSB to LSB)
7. 每個bit總共有n個數會OR在一起, 如果k次操作後仍存在著一個數在該bit為1, 那代表該bit是無法透過操作消除的

從高位往低位, 逐位i-th bit來看:

```
                  i
bit = XOR(nums) = X X X X X X X X X X X X X X X X X
                nums[0]
                nums[1]
                ...
                nums[i]
```

從高位往低位, 先嘗試看看能不能消除i-th bit

最終如果要花大於`k`次操作, 那代表移除不了這位bit, 更新最終答案`res`
但如果`操作數<= k`, 繼續看i+1-th bit

```py
for i in range(29, -1, -1):
    test = (1<<i)
    cnt = val = 0
    for num in nums:
        if val == 0:
            val = test&num
        else:
            val &= test&num
        if val > 0:
            cnt += 1
    if cnt > k:
        res |= (1<<i)
```
我們把nums[i]全AND在一起, 並存在`val`
如果`val > 0`, 那麼我們肯定得花一次操作跟nums[i]進行AND操作直到`val`變0
我們紀錄需要多少次操作在`cnt`上, 如果`cnt > k`, 那代表該bit無法透過至多k次稍作消掉, 我們更新`res`

但會fail在這個test case: nums=[39,62,35,11,28,32], k=3, expected=38

想了一下發現: 我們每次只看i-th bit, 雖然操作數 <= k代表我們可以透過合法操作使得i-th bit為0
但有可能i-th bit的k次操作跟i+1 bit的k次操作, 兩邊操作的nums[i]並不一致
所以我們要確認的, 其實是到目前為止, 每個能成功透過k次操作消除的prefix bits

我們在看i+1 bit的過程中, 我們也要把前i次的結果給暫存起來
然後確認這第i+1 bit的過程中, 前i次是不是也不受影響

前i次如果是`res=1101001`:
那麼這第i+1次的確認過程中也必須同時那三個bit為0的位置在這i+1的操作中是不是也能滿足
而1的部分代表即使k次操作也無法消掉, 我們就不管

所以我們額外用個mask紀錄我們當前可以成功透過操作消除的prefix bit position
只要最後`cnt <= k`, 我們就更新`mask | (1<<i)`, 然後繼續看下個bit位置是不是也能讓前面的操作都合法
那如果`cnt > k`, 那就跟之前一樣, 我們僅更新`res`即可

```py
res = mask = 0
for i in range(29, -1, -1):
    test = mask | (1<<i)
    cnt = val = 0
    for num in nums:
        if val == 0:
            val = test&num
        else:
            val &= test&num
        if val > 0:
            cnt += 1
    if cnt > k:
        res |= (1<<i)
    else:
        mask |= (1<<i)

return res
```

# Complexity

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$