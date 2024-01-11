# Intuition

先想到對nums排序, 這樣可以透過binary search找出`nums[0:j] where nums[j] <= m`
```py
j = bisect_right(nums, m)-1
```

再來就看該如何高效查找maximum XOR among `x XOR nums[0:j]`

如果我們將原quries對m做由小到大排序的話, j也會由小到大遞增
那我們就可以由小到大的一個一個將**小於等於m**的nums[j]加入到Trie裡
再透過Trie找出maximum XOR

XOR要最大, 那就是要找一個nums[j], 其中nums[j]從高位開始, 每個bit位上都盡量跟`x`相反
- x[i] 代表i-th bit of x, nums[j][i] 代表i-th bit of nums[j]
- x[i] == 0 => nums[j][i] == 1
- x[i] == 1 => nums[j][i] == 0

那這樣Trie是個很好查找maximum XOR的數據結構
我們要做的是將每個nums[j]從高位bit到低位bit加入到Trie裡

那我們在找max(x XOR nums[j])時, 我們就從高位bit開始
如果x的當前i-th bit是`b`, 那Trie就找有沒有`1-b`存在, 沒有的話再往`b`找
如此一來就能找到與x相互XOR的最適nums[j]

所以總結一下:
- 將nums排序
- 將queries排序(記得紀錄原本index)
- 將所有`<= queries[i].m`的nums[j]加入到Trie裡
- 透過Trie找出maximum_xor(x)
- 更新res[queries[i].index]

那這樣時間複雜度就是: O(sorting + queries.length * log(nums.length))
