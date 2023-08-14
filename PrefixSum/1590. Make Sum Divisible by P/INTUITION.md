# Intuition

```
X X X [X X X X] X X 
       j     i
要找到一段最小的nums[j:i]使得`(sum(nums) - sum(nums[j:i]))%p == 0`

we want (presum[n] - (presum[i+1] - presum[j]))%p = 0 and make i-j minimum
=> presum[n]%p == (presum[i+1]-presum[j])%p == remainder
=> (presum[i+1]%p - presum[j]%p + p)%p == remainder
=> (presum[i+1]%p - remainder + p)%p == presum[j]%p
```

所以:
如果我們在遍歷過程中用hashmap存下hashmap[presum[i+1]%p] = i
那我們就能透過hashmap找到presum[j]%p, 其中j = hashmap[presum[j]%p] = hashmap[(presum[i+1]%p - remainder)+p)%p]
因此我們就能更新res = min(res, i-j) i-j < n
如果i-j == n代表我們把整個nums都給移除掉, 這不合題目敘述

**base case**

hashmap的初始條件`{0:-1}`
sum為0時, index=-1

這對應的狀況是我們扣掉一段presum[i]使得 (presum[n]-presum[i+1])%p = 0
這時這段扣掉的subarray長度為`i+1`
所以我們相當於給了presum[j]為零0, j=-1, 這時i-j就會是我們扣除的subarray長度

```
ex. 
  [X X X X X X X] X X X X X X
-1             i
```