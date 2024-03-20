# Intuition

brute force:
```py
n = len(binary)

SET = set([""])
for i in range(n):
    nxt = SET.copy()
    for prev in SET:
        nxt.add(str(int(prev + binary[i])))
    SET = nxt

return len(SET)-1
```

01 : {0,1}
00 : {0}

010: {0,1} + 0 = {0,10}
011: {0,1} + 1 = {0,1,11}

11 : {1} + 1
10 : {1} + 0

110 : {1,11} + 0
111 : {1,11} + 1

100 : {1, 10} + 0
101 : {1, 10} + 1

以0為開頭只有"0"是unique good subseq.
我們先撇除"0"這個edge case來看的話, 我們討論以0或1做結尾的unique good subseq.

```
    binary[i]
{XXXXX}1
{XXXXX}0
```

定義dp0: the number of unique good subseq ending with 0
定義dp1: the number of unique good subseq ending with 1

1. 所以當binary[i] == 0時, 這時能更新dp0, `dp0 = dp0+dp1`
2. 當bianry[i] == 1時, 更新`dp1 = dp0+dp1+1`, 其中1是binary[i]本身能作為一個新的unique good subseq.

那整個遍歷一遍後, 就能得到所有1開頭並且以0結尾和1結尾的unique good subsequence了

最終答案就是dp0 + dp1 + edge case 0 if 0 exists
