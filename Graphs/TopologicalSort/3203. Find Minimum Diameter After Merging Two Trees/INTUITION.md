# Intuition

很直覺的能想到是如果要最短直徑, 那肯定是正中心, 所以兩棵樹的中心相連接肯定會形成最短直徑
所以我們可以利用topological sort找出兩棵樹的中心點相連接
最短距離就是兩者topological sort 最長距離再+1(兩中心點相連的邊)

topological sort走到最後只會有兩種可能:
1. 剩下單獨一個節點
2. 剩下兩個節點

### 情況一:
如果剩單獨一個節點, 那麼這棵樹貢獻的diameter為走到中心的最長路徑

### 情況二:
如果topological sort走到最後出現兩個節點, 挑選任一節點, 貢獻的路徑為max(自身路徑, 另個節點路徑+1)

ex. example2的Tree1, 走到最後會剩下節點0跟2
節點0的最長路徑是2, 節點2的最長路徑是1, 兩節點中間還連著一條邊
所以如果選擇節點0, 貢獻diameter為max(2, 1+1) = 2
如果選擇節點2, 貢獻diameter為max(1, 2+1) = 3
由於我們最終是要求minimum diameter, 所有我們應該選擇節點0作為我們這棵樹的中心去相連

注意edge case：
- 當兩棵樹都只有單獨一個根節點時, diameter=1
- 另外就是如果Tree1, Tree2各自的diameter分別為diameter1, diameter2. 那麼兩棵樹相連後的最短diameter不會小於diameter1跟diameter2
  - ex. edges1=[[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], edges2=[[0,1],[0,2],[0,3]]
  - Tree1自身的diameter已經是7, 所以Tree1+Tree2相連雖然是6也沒用

# Other Intuition

from [@lee215](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/solutions/5389457/python-farthest-of-farthest/)

> Diameter:
> Find one farthest point i from 0,
> Find one farthest point j from i.
> [i, j] is a diameter

> The tree with smallest height:
> Take the middle points one diameter,
> the height is the ceil of half of diameter,
> which is (diameter + 1) / 2.

> Combine:
> Connnect two root of shortest tree
> The fathest from one tree to the other is **(d1 + 1) / 2 + 1 + (d2 + 1) / 2**.

因此概念是這樣:

我們可以透過兩次BFS去找出單顆樹的diameter:
1. 第一次BFS, 從任意點出發走到盡頭
2. 從盡頭一端出發走到另一端盡頭, 這次走的路徑即為最長路徑, 也就是diameter

找到兩顆樹各自的diameter後(diameter1 & diameter2), 兩顆樹連接後的diameter3為兩顆樹ceil(直徑/2)相加再加上中間連接的邊, 亦即`diameter3 = (ceil(diameter1/2) + ceil(diameter2/2) + 1)`
三個diameter取max即為答案


```py
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def findDiameter(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            queue = deque([0])
            seen = set()
            farthestNode = -1
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node in seen: continue
                    seen.add(node)

                    for nxt in graph[node]:
                        queue.append(nxt)
                        farthestNode = nxt
            
            queue = deque([farthestNode])
            seen.clear()
            longestPath = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node in seen: continue
                    seen.add(node)

                    for nxt in graph[node]:
                        queue.append(nxt)
                if not queue: break
                longestPath += 1
            return longestPath

        diameter1 = findDiameter(edges1)
        diameter2 = findDiameter(edges2)
        return max(diameter1, diameter2, ceil(diameter1/2)+ceil(diameter2/2)+1)
```