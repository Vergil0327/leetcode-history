# Intuition

nums[i]全部都是正數，所以乘積會越乘越大
那這樣我們可以用two pointers (或稱sliding window) 來移動左右邊界討論合法subarray區間


以下是一個左閉右開的區間`[l, r)`
只要`[l, r)`這段區間乘積小於k, 我們就持續移動右邊界
一但 `乘積>= k` 我們就移動左邊界縮小乘積

那這樣一來我們可以如何計算subarray呢?
我們看底下的示意圖:


```py
curr = 1
while r < n:
    curr *= nums[r]
    r += 1

    while l < r and curr >= k:
        curr //= nums[l]
        l += 1

    # do something
```

[X X X X X X X] X Y
 l              r ->
[X]
[X X]
[X X X]
[X X X X]
[X X X X X]
[X X X X X X]
[X X X X X X X] 共 r-l 個

我們每移動r，只要乘積小於k，就代表我們找到固定左邊界的合法subarray
如果說上面那段[l,r)乘積小於k的話，那就有`r-l`個以l作為左邊界的subarray

如果下一個nums[r]加入後乘積 >= k了，那我們就移動左邊界`l`
這時變成

X X X [X X X X X] X
       l          r

      [X]
      [X X]
      [X X X]
      [X X X X]
      [X X X X X] 共 r-l 個 subarray

這時如果說[l, r)這段區間乘積小於k的話，同理
我們又找到`r-l`個以`l`作為左邊界的合法subarray

因此我們只要在上面comment `# do something` 的位置持續加上所有以`l`為左邊界的合法subarray個數即可

```py
curr = 1
answer = 0
while r < n:
    curr *= nums[r]
    r += 1

    while l < r and curr >= k:
        curr /= nums[l]
        l += 1

    if curr < k:
        answer += r-l
return answer
```

# Complexity

- time complexity
$$O(n)$$

- space complexity

$$O(1)$$