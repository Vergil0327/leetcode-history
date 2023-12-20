# Intuition

```
X X X {X X X X X X}
       j         i
```

we want find `j` such that sum(nums[j:i]) >= k => presum[i]-presum[j-1] >= k
because nums[i] can be negative, sliding window doesn't work in usual way
see this example: nums=[84,-37,32,40,95], k=167, answer=3

```
84,-37,32,40,95
j       j     i
```
有兩個候選的j位置可滿足presum[i]-presum[j-1] >= k, 而我們要選更靠後的那個`j`
但由於有負數的關係, presum不是遞增的所以我們是找不出`j`的

那如果我們讓presum是遞增的話, 會如何?
ex. presum = [1,2,3,4]的話, 如果現在來了個presum[i] = 2
也就是:
```
 0 1 2 3  4 => index
[1,2,3,4] 2
          i
```
那麼我們是不是就不用後面的[2,3,4]了? 因為未來再有個presum[i']時, 當前i位置這個2的選擇都比後面的[2,3,4]來的優
我們這樣來看, 後續如果有個presum[i] 那們減去 presum[1]跟presum[4]都一樣是減去2
那麼當然選j=4那個位置比較好
那如果presum[i']-presum[4]已經 >= k了, 那麼`presum[i']-presum[2]=presum[i']-3`跟`presum[i']-presum[3]=presum[i']-4`也都會滿足presum[i]-presum[j] >= k
也就是我們希望presum[j]越小越好並且j越靠後越好, 這樣越能讓presum[i]-presum[j] >= k

因此我們在每次加入一個新的presum時, 要維護一個單調遞增的presum_j
但這題還有個不同的點是如果我們找到了一個合法的presum[i]-presum[j] >= k的解了呢?
那代表從[0,j]這段的presum我們都可以pop掉了, 因為未來從這位置或更靠前的presum[j']就算能跟當前presum[i]滿足presum[i]-presum[j'] >= k
那個長度也遠比presum[i]-presum[j]來得大 (因為0 <= j' < j)

因此我們要做的其實是用deque維護一個單調遞增的presum, 並且概念上像是用deque來求出sliding window maximum(see 239. Sliding Window Maximum)
所以我們:
1. 要加入presum[i]到presum時, 持續pop掉presum[-1]以維持單調遞增
2. 如果找到一個合法的presum[i]-presum[j] >= k, 更新answer並持續popleft掉presum[0]來剔除長度大於當前合法解的選擇
那最終就能求出Shortest Subarray with Sum at Least K

# Complexity

- time complexity: $O(n)$
- space complexity: $O(n)$