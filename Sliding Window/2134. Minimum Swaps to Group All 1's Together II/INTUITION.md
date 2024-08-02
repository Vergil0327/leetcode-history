# Intuition

see ex.3 nums = [1,1,0,0,1]

由於是circular array => 我們可以嘗試將兩個nums重複排在一起來想
nums = [1,1,0,0,1] + [1,1,0,0,1]

nums總共有3個1 => 目標是找出連續3個1相連的最低swap數
所以我們可以用sliding window找出window size = sum(nums)的時候, 此時window size - sum(nums)就是swap的數量
也就是sliding window裡zero的個數就是當下需要swap的個數
至於circular的部分, 就透過兩個重複array接在一起, 然後sliding window整個掃過一遍就會考慮到了

所以我們移動fixed size sliding window whose length equals sum(nums)
然後觀察每個位置的sliding window, sliding window裡的zero個數就是swap個數
找全局最小即可

# Optimized

我們不需要併接兩個nums, 我們利用`index%len(nums)`這技巧, 然後遍歷`2*len(nums)`長度, 即可模擬circular array了