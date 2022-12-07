### BFS + Union-Find

由於這題Graph可以是disconnected的，所以這題主要要求的是:

`所有connected component能分成的maximum groups的總和`

因此主要的子問題為
`每個Connected Component，最大能分成幾個groups?`

1. 第一部分，求Connected Components

首先我們可以得知，我們需要利用`Union-Find`來協助我們找出所有Connected Components. (BFS, DFS也可以，但這題有給邊，使用union-find比較方便)

將所有的邊union完後，每個擁有共同祖先的node的便為同一個connected component

2. 第二部分，求每個Connected Component的Max Groups

    再來我們就遍歷每個connected component，利用BFS求出最大的層數，並同時確認是否能合法分出group來

   1. 求最大group:
   
      以每個node作為起始點開始層序遍歷，找出最大層數

      BFS的最大層數即為max groups
   2. 確認是否可分割

      奇數層節點不可有環的存在(必須是bipartite graph)

最後還有一個地方可優化的是，很明顯地
`如果要BFS能夠最大層數，我們必須從最外層的node開始遍歷`

### Intuition

1. since graph can be disconnected, we need to find every connected component
	- use Union-Find
2. max groups of connected component is max layers of BFS
3. start BFS from outer-most node to get max layers

based on 2. & 3.,
we can use indegree to find outer-most node (just like preparation of topological sort), then use BFS to get max groups of each connected component

`answer = sum(every max groups of each connected component)`