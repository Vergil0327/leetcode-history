# Intuition

這題最直覺的暴力解法是
```py
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [1] * (n+1)
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        suffix = [1] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        
        for i in range(n-1):
            if gcd(prefix[i+1], suffix[i+1]) == 1: return i
        return -1
```

但會發現這樣相乘起來到最後數值會非常大, 在最後的步驟算gcd會非常久
```py
for i in range(n-1):
    if gcd(prefix[i+1], suffix[i+1]) == 1: return i
```

由於我們是要在[0,n-1]找一個split，使得左右兩邊沒有共同的因數，因此我們可以先用prefix sum的概念先算出由左到右在每個`i`位置上的總因數個數為多少

```py
right = defaultdict(int)
for num in nums:
    facs = getFactors(num)
    for fac in facs:
        right[fac] += 1
```

然後我們在由左到右遍歷，看看split在`i`位置上時，左側的因數為哪些
然後再看左右兩邊有沒有共同的因數

根據題意, 遍歷範圍為[0,n-1]
每當我們把一個數加到左側，那右側就要扣掉: `right[fac] -= 1`

一但右側不再包含該因數, 亦即`right[fac] == 0`時，代表該因數不再是共同的因數
因此也從左側扣掉: `del left[fac] if right[fac] == 0`

一但我們發現一個位置是，左側沒有任何因數存在時(因為把該因數從右側移到左側後，右側為0且我們也同步從左側刪除)
代表該位置就是一個合適的split位置
由於index越靠前越好，因此找到的第一個合法index就直接返回即可

```py
left = defaultdict(int)
for i in range(n-1): # check split at i
    for fac in factors[i]:
        left[fac] += 1

        right[fac] -= 1

        if right[fac] == 0: # doesn't share fac in both left and right anymore
            del left[fac]
```