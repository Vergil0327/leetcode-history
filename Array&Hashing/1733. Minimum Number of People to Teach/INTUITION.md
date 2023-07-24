# Intuition

由於只能教一種language給複數人, 那我們就遍歷所有語言x
然後查看每個語言不通的friendship組合 => 兩邊語言set沒有交集
然後對於當前語言x, 誰不會就教誰, 然後teached += 1
最後看教哪種語言x可以教最少人即可

# Complexity

- time complexity
$$O(n * len(friendships))$$
