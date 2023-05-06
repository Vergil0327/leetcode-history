# Intuition

這題首先必須想到的是:

對於subsequence來說，由於每個nums[i]都是可選可不選
所以即使我們對nums排序後，答案結果依然不變

因此我們可以試著對nums先排個序，這樣在找`min`跟`max`也方便很多

那在排序之後我們可發現`nums`會是這樣的一個情況

`nums = MIN X X X X X X X X X MAX`

再來重要的一點來了，如果這整段區間內`MIN + MAX <= target`的話，那有幾種subsequence?

如果我們有`l`, `r` pointer, 這時我們固定`l`左邊界後
在這[l+1,r]範圍內，每個數不管選或不選，subsequence都是合法的
所以這時在固定`l`的情況下有 `2**(r-l)` 種合法subsequence

MIN [X X X X X X X X X MAX]
l                       r   -> we can pick or not to pick nums[i] where i from l+1 to r
                            -> cnt += 2 ** (r-l)

這時計算的想法就很清楚了

我們左邊界`l`可以一步一步走，每走一步就移動`r`找出`nums[l] + nums[r] <= target`的合法區間
這時就 `cnt += 2 ** (r-l)`

等到`r`走到`l`左邊後，代表已經不可能有subsequence了，我們可以直接break, 跳出循環

由於`r-l`有可能會到10^5, 所以我們可以預先處理一下 [2^0, 2^n] 並對1e9+7取餘數
這樣也不用一直重複計算 `pow(2, r-l, int(1e9+7))`

# Complexity

- time complexity
$$O(nlogn)$$ for sorting

- space complexity
$$O(n)$$
