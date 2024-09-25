# Intuition

let `dp[i]` be the minimum cost to form the prefix of length i of target.

### base case

```py
n = len(target)

dp = [inf] * (n+1)
dp[0] = 0
```

再來就開始更新dp
我們從target的prefix開始找, 遍歷words看存不存在於words[i]裡
如果有, 就代表target[l:r]可以從target[l:l]透過words[i]轉化過來, 
```
dp[r] = dp[l] + 1
```

等到target[l:r]不存在於words裡時, 就移動左端點, `l -> l+1 = l'`, 然後看target[l':r]存不存在於words裡
如果有, 那就能推進dp[r] = dp[l'] + 1

如果dp[l']之前可以透過target[l:l']轉化的話, 這時dp就會正確更新, 不然就會繼續維持在inf

如果target[l:r], target[l+1:r], ...一直到target[r:r]都不存在於words裡的話, 就代表我們無法更新dp, 可以直接返回-1

等到全部遍歷完後, 最終我們就看最終要組成長度為`n`的target需要多少個words[i]的prefix, 也就是`dp[n]`

# Approach

1. 移動sliding window target[l:r] for r in range(1, n+1)
2. 如果target[l:r]為words[i]的prefix, 那就能更新dp[r] = dp[l]+1
3. 如果都不是, 那就移動左端點`l`, 看下個target[l+1:r]能不能更新dp
