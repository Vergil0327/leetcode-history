# Intuition

after sorting:
[x1, x2, x3, x4, x5, x6]

group1: [Y]
group2: [Y, Y]
group3: [Y, Y, Y]
...
groupK: [Y, Y, Y, ..., Yk]

如果目標group size是k的話, 那到該group為止必須有`(1+k)*k/2`個elements
所以我們可以有個presum來計算我們到目前為止有多少available elements

由於裡面放什麼數字沒有限定, 所以我們先排個序然後從小到大依序分配到group裡

所以透過presum[i]我們可以得知到目前為止有多少available elements
然後再透過我們下個要建構的target group, 我們可以得知我們需要`require = (1+k)*k/2`個elements
一但presum[i] >= require, 那target group += 1
最後看我們最多能組成多少target group即可