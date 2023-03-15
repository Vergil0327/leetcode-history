# Intuition

定義 dp[i]: the minimum possible total cost of separating sentence[:i] into rows

{XXX_XXXXX_XXXX}_{XXX}_ ..., k = 4
                j     i
                
{XXX_XXXXX}_{XXXX_XXX}_

想法是每遇到`" "`, 就代表找到一個word
如果`endIndex = i`, 我們可以往前移動`j`
當`j`遇到`" "`後`sentence[j:i]`就是個沒有leading space & trailing space的sub-sentence
只要**長度<= k**, 那就可以進行狀態轉移:
`dp[i] = min(dp[i], dp[j] + cost(sentence[j+1:i]))`

由於我們會往前找`" "`, 所以我們可以將sentence前面加個空格改成**1-indexed**
這樣我們才不會漏掉第一個word
因此我們的合法遍歷區間為[1,n], both inclusive

另外由於最後一個word沒有cost，但實際上sentence的最後也沒有trailing space
所以不會進行狀態轉移，所以最後答案就是最後一個合法的dp[i]

```py
dp = [float("inf")] * (n+1)
sentence = " " + sentence
for i in range(1, n+1):
    if sentence[i] == " ":
        for j in range(i-1, max(i-k-2, -1), -1):
            if sentence[j] == " ":
                dp[i] = min(dp[i], dp[j] + cost(sentence[j+1:i]))
```

**Base Case**

empty string -> 0 cost
dp[0] = 0
