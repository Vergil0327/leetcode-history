# Intuition

這題Brute Force的解法為直接DFS全部情形即可，但看數據範圍肯定會超時

由於我們每次拿取都是從最左或最右，從兩側的話中間會是個連續區間，因此我們可以逆向思考

比起我們該拿哪些，我們改成我們拿走哪些後仍符合答案，找出中間能移除的最大區間後扣掉，剩下的兩側即為答案

因此這個問題可以改成一個Sliding Window的問題

首先基本的判斷為a, b, c字數少於k時，我們不可能得到答案
```python
counter = Counter(s)
if counter["a"] < k or counter["b"] < k or counter["c"] < k:
    return -1
```

再來就是透過sliding window, 找出中間最大的區間使得整個字串扣掉中間區間的字符後, 仍符合
`counter["a"] >= k and counter["b"] >= k or counter["c"] >= k`即可