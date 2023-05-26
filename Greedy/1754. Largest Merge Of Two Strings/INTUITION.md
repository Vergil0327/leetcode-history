# Intuition - Greedy

直覺想法就是哪個字符大就取誰的
最大的關卡就是, 當兩邊字符相等時該取誰的?

當初用了雙指針一路搜尋, 直到兩邊字符不相等時在看該取哪一邊
但這又有個問題是我到底是該整段取完還是兩邊相同的同步取完
想不到一個正確的greedy策略所以卡了好幾個test case

```
"uuurruuuruuuuuuuuruuuuu"
"urrrurrrrrrrruurrrurrrurrrrruu"

"guguuuuuuuuuuuuuuguguuuuguug"
"gguggggggguuggguugggggg"
```

但其實真正決定該取哪個首字符的條件是:

我們就看剩下的word1[i:]跟word2[j:]中, 誰較大即可
當當前首字符相等時, 先取剩下的字符較大的, 那就會更早取到較大的首字符

time: $O(n^2)$