# Intuition

核心思想是透過monotonic stack來維護string的字母順序

再來就Greedily判斷哪些字符可以加入，或是什麼時候字符可以替換刪除

我們的目標是一個字母順序最小且**含有所有字母且只出現一次**的string
因此我們先計算string裡每個字母出現多少次

```
counter = Counter(s)
```

再來透過hashset `has` 來記錄我們目前擁有哪些字母
如此一來，便會有以下情形:
1. 字母可以直接接在後面的情況
   1. stack is empty
   2. current letter is lexigraphically larger than previous one
2. 那如果不是上面第一點的情況，不能直接接在後面並且我們已經擁有這個字母了，因為我們維護的是一個字母順序單調遞增的序列，就算目前字母比較小，但我們已經有了，更早前面出現的這個字母肯定會比現在這個字母字母順序還小(有點Greedy的思想)，或者頂多就相同位置，所以這個字母就直接skip
3. 再來就是，我們還沒有這個字母，並且這個字母順序比前一個還小，這時我們就要判斷:
   - 如果前一個字母後面還會再遇到的話，那我們才可以把它pop掉，然後再加入現在這個字母，如果後面不會再出現，那就不能pop掉，不然我們就無法組成合法的答案了

最後整理一下，可以整理出Concise Version

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$