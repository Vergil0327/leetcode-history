### Hashmap Solution

1. find every possible substring first

*length of substring = len(words) * len(words[0])*

1. check validity of substring

since each parts of substring should be permutations of `words` and its length is fixed, we can check validity by **hashmap**.

just iterate with `wordLen` as iteration step

### Sliding Window

首先最外面的循環是sliding window的起點，起點可以是0-wordLen任一點

由於每個word的長度是固定的，在sliding的過程中會有重複計算的部分，最外面大循環僅需考慮wordLen，然後滑動窗口到最後即可

```
如果wordLen = 3
i = 0, 3, 6, 9, ...
i = 1, 4, 7, 10, ...
i = 2, 5, 8, 11, ...
i = 3 -> 跟i=0重複了
```

然後在window裡，我們維護:
- substring的起始點: `head`(窗口左邊界)
- 窗口右邊界: `i`
- 更新word數: `found[word] += 1`
- 合法的word數: `count`

1. 如果index+wordLen越界或是不存在於`words`裡，移動左邊界`head`到這個invalid word的右邊界(i+wordLen)，然後繼續移動窗口尋找

2. 如果目前找到的word雖然合法，但目前窗口內的word數量超出`words`裡的數量，那麼sliding window仍然不合法，移動左邊界`head`然後重新移動`i`尋找

3. 如果目前的word是合法的，更新`count`跟更新`窗口內含有的word數目`，然後繼續移動右邊界`i`繼續往後尋找

如果目前窗口內為我們要的**concatenated substring**，亦即窗口內含有所有的words，紀錄結果
然後移動左邊邊界`head`繼續尋找