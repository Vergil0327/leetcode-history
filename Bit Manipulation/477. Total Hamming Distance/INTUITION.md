# Intuition

首先我們如果brute force的話, 我們可以用個hashmap看每個數有多少
counter = Counter(nums)

在去除重複後遍歷每個key，算他們的Hamming distance，也就是:
`ans += countOneBit(keys[i]^keys[j]) * counter[keys[i]] * counter[keys[j]]`

但這樣會是個O(n^2)的解法，會超時(TLE)

因此我們換個角度想，bit最多就32位，我們可以逐位計算而非湊成pair再計算

對於每一位bit來說，我們看他這位bit是`1`還是`0`把他們分成兩邊
分成兩邊後`1`的個數如果是`x`, 而`0`的個數為`y`的話
那就代表對於所有nums來說, 組成pair後在這個bit位上能貢獻的有效Hamming distance為 `x * y`
(在該位bit上，同是1或同是0組成的pair的hamming distance為0)

因此遍歷完32位bit後就知道每個bit位上的hamming distance加總為多少了

`ans += (# of 1 for i-th bit) * (# of 0 for i-th bit) for i in range(32)`

# Complexity

- time complexity
$$O(32n)$$

- space complexity
$$O(1)$$