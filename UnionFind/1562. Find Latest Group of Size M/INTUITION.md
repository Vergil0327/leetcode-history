# Intuition

用一個array代表bits [0,0,0,0,...]

我們的目標是知道:**什麼時候最後一次出現length為m的consecutive ones**

- union-find連通bit-1 => union(i,i+1), union(i,i-1)
  - 只有當bits[i]跟bits[i+1]都有1時才能連通union(i, i+1)形成consecutive ones
  - 同理, 也只有當bits[i]跟bits[i-1]都有1時, 才能union(i, i-1)
- 並用size[i]來紀錄當前的union的size
- 最後用hashmap來查看什麼時候出現m-size union以及它什麼時候消失
  - 每次union(x,y), size[x]跟size[y]次數少1, 但 size[union(x,y)]的次數+1
  - 用hashmap來查看當前是否存在target size的consecutive ones的size
      - 一旦出現, 我們就紀錄當前step, 最終返回的就是最後一次出現m-size consecutive ones的index (1-indexed)

*note: 由於數值範圍[1,n] -> 額外padding 0跟n+1來方便我們union, 免除out-of-bound error*