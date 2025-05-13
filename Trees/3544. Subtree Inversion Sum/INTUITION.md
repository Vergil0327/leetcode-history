# Intuition

tree是以遞迴構造出的資料結構, 大多數情況都能用遞歸來解決, 所以想到用dfs來試試
dfs(node, prev)是基本結構, 此外我們還得紀錄當前已經翻轉過幾次`inverted`, 還有距離上次翻轉的節點距離`lastInvertDist`, 這樣才能判斷是否可以翻轉(翻轉必須至少距離為k), 因此:

dfs(node, prev, inverted, lastIvertDist): the sum of inverted tree at `node`, 再來就是跟著題意遍歷所有可能狀態

```py
class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        
        
        @lru_cache(None)
        def dfs(node, prev, inverted, lastInvertDist):
            # don't invert
            res = nums[node] * inverted
            inverted_res = nums[node] * inverted * -1
            for nxt in graph[node]:
                if nxt == prev: continue
                res += dfs(nxt, node, inverted, lastInvertDist+1)

                # can invert
                # should check if distance since last inverted parent is at least k
                if lastInvertDist >= k:
                    inverted_res += dfs(nxt, node, inverted*-1, 1)
            
            return max(res, inverted_res) if lastInvertDist >= k else res

        return dfs(0,0,1,k)
```

但可惜這樣會TLE
事後才發現我們的cache根本沒有發揮作用, 由於`lastInvertDist+1`這項如果沒有cap, 那可能會無止盡加上去
但實際上我們只需要知道他有沒有至少`k`即可, 所以應當加上`min(k, lastInvertDist+1)`, 這樣cache才會發會作用

修改後版本如下, 這樣cache就能正常發揮作用, 以避免重複計算了:

```py
class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @lru_cache(None)
        def dfs(node, prev, inverted, lastInvertDist):
            # don't invert
            res = nums[node] * inverted
            inverted_res = nums[node] * inverted * -1
            for nxt in graph[node]:
                if nxt == prev: continue
                res += dfs(nxt, node, inverted, min(k, lastInvertDist+1))

                # can invert
                # should check if distance since last inverted parent is at least k
                if lastInvertDist >= k:
                    inverted_res += dfs(nxt, node, inverted*-1, 1)
            
            return max(res, inverted_res) if lastInvertDist >= k else res

        return dfs(0,0,1,k)
```
    
結果這樣會MLE...
後來只好把`prev`這個代表當前節點的parent資訊從dfs拔掉, 另外用個list來表達, 節省cache的空間

另外還能透過BFS先找出樹節點的每個子節點, 而不用額外紀錄`parent`的資訊