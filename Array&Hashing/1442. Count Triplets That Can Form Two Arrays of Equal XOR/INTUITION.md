# Intuition

經典的prefix sum + hashmap題型, 首先要知道的是:

- left XOR Mid = Right => left = Rright XOR Mid

- prefixXOR[i:j] = prefixXOR[0:j]^prefixXOR[0:i-1]

可看出XOR有類似prefix sum的性質

因此我們arr可以分成:

```
{arr[0] ^ ... ^ arr[i-1]} {arr[i] ^ ... ^ arr[j]}{arr[j] ^ ... ^ arr[n-1]}
    prefixXOR[0:i-1]         prefixXOR[i:j-1]      prefixXOR[j:k] where j <= k < n
```

遍歷i可以得到prefixXOR[:i], 我們希望找到一段XOR(subarray[x:i]) = prefixXOR[0:i]^prefixXOR[0:x] == prefixXOR[j:k]

因此透過ＸＯＲ特性, 我們可以得知:
- prefixXOR[0:x] = prefixXOR[j:k]^prefixXOR[0:i]
- 我們要找prefixXOR[x:i] == prefixXOR[j:k]的合法subarray

由於prefixXOR[x:i] = prefixXOR[0:i]^prefix[0:x] == prefixXOR[j:k]
因此可以得知prefixXOR[0:x] = prefixXOR[j:k]^prefixXOR[0:i]

因此我們遍歷i, j就能得到prefix[0:i]跟prefix[i+1:j]
我們希望`prefix[0:i] == prefix[i+1:j]`, 所以prefixXOR[0:x] = prefix[i+1:j]^prefix[0:i]
所以我們透過hashmap `Count`就能知道: 有多少`prefixXOR[0:x]`就有多少合法triplet使得prefix[x:i] == prefix[i+1:j]