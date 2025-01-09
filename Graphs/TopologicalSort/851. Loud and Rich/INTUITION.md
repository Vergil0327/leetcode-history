# Intuition

題目不好看懂, 但基本上透過richer關係, 我們可以架構出整個graph
然後透過topological sort由富有到窮一路遍歷
並在過程中找出所有比他富有或資產相同的人裡, 最安靜的

這邊注意是`equal to or more`, 代表自己也包含在內,  所以如果沒有比自身quiet, 那也不會更新
所以我們就需要在整個topological sort的架構中進行這項判斷即可:

```py
for nxt in graph[node]:
    if quiet[res[node]] < quiet[res[nxt]]:
        res[nxt] = res[node]
```