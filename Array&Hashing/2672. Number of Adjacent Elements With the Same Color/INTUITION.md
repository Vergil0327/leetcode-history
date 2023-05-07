# Intuition

由於我們每次只塗改一個index的顏色, 所以我們每次塗改僅需要關心`index-1`, `index`, `index+1`這三個位置

所以我們可以用個**hashmap**來儲存每個index的顏色, 並且維護相鄰顏色相同的元素個數`cnt` (the number of adjacent elements with the same color after the ith query)

- 如果這次塗改的顏色跟上次一樣, 那麼相鄰顏色相同的index總個數就不會變
- 如果塗改顏色不同
  - 對於`index`來說, 我們就看左右鄰居顏色來決定
    - 如果跟左鄰居顏色相同, 那該次塗改貢獻1, `cnt += 1`
    - 如果跟右鄰居顏色相同, 那該次塗改貢獻1, `cnt += 1`
  - 對於`index-1`跟`index+1`來說
    - 如果顏色跟`index`塗改前的顏色相同(注意index塗改前必須有顏色, 亦即顏色不為`0`), 那麼總個數就少1, `cnt -= 1`