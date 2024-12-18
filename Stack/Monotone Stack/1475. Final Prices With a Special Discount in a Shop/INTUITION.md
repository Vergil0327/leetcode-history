# Intuition

```
X X X X X {X X X X X X}
        i  j->
```

對於prices[i]來說, 要找一個小於等於prices[i]並且離最近的prices[j]
這樣會耗費O(n^2)時間來搜索

但這邊我們可以反過來想, 想成對於每個prices[j], 我們往回看有沒有合法的prices[i]

因此可以利用monotonic increasing stack
我們把遍歷過的每個price都加入到stack, 一旦`prices[stack[-1]] >= prices[j]`
代表對於當前的prices[j]來說, stack[-1]為合法的prices[i]
然後我們可以一路利用stack往回找所有合法的prices[i]

最終時間複雜度就是:O(n)