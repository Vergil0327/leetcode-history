# DFS

## Intuition

這題有兩個坑，很需要注意的地方是

1. 由於`next`指針的存在，我們在做橫向連接(Level Connect)的時候，可以持續往右搜尋，因此需要持續遞歸的往右找到盡頭
   1. 對於左節點來說，如果右節點存在，左節點則連接到右節點，否則則繼續透過`root.next`往右搜尋
   2. 對於右節點來說，持續透過`root.next`往右搜尋節點
2. 由於我們是左節點往右節點連接，左子樹往右子樹連接，因此我們必須保證右子樹得先完成所有橫向的連接。因此，`DFS必須先遍歷右子樹`!!!

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(stack)$$

## Real O(1) Space Solution

**Iterative Method**

`curr`: pointer指向當前node
`tail`: 目前level的leading node，用於橫向連接，tail.next會指向右邊的left node 或 right node
`head`: 下一層的root node

**Approach**

首先第一層`while curr:`不斷往下個level走
再來第二層`while curr:`則在當前level不斷往右走，連接`next` pointer
每個當前節點的左節點或右節點都判斷：
  - 如果`tail`不為None，代表當前節點的左側有個節點需要跟我們連接，我們必須將`tail.next`指向當前節點
  - 如果`tail`為None，代表當前節點左邊沒有節點需要連接`next`，我們可以將`head`指向當前節點，準備移向下個level
  - `tail`指向當前的節點，這樣在下一回合的第二層 while-loop，我們可以將`next`指向右側節點並持續往右連接

在第二層while-loop結束後，代表當前level已連接完畢，可以朝下個level進行，並再執行相同操作

```py
while curr:
    # ... level connecting process here

    # to next level
    curr = head
    tail = head = None # initial state
```