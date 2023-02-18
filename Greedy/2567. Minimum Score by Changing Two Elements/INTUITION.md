# Intuition

因為只看兩個值的絕對值，所以我先對nums排序

我們能調換兩個值，所以**我們總是能讓最小分數為零**
兩個值都換同個數，或是任一值換成跟某個數相同，那麼min score即為0

我們要盡可能降低score，就代表我們調換的數值原本差越大越好
對於一個排序後的nums

我們肯定是盡可能減少頭跟尾的差值，也就是nums[0]跟nums[-1]的差值，這樣 max score 才會縮小

那我們能做的策略其實最終只有三種

1. 我們調換nums[0], num[1]，這樣max score = nums[-1]-nums[2]，

2. 我們調換nums[-1], nums[-2]，這樣max score = nums[-3]- nums[0]

3. 我們調換nums[0], nums[-1]，這樣max score = nums[-2]-nums[1]

所以我們只要看三種可能哪一種得到的score最小即可