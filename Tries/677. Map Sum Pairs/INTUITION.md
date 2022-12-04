### Trie

借用[leetcode 1804. Implement Trie II (Prefix Tree)](../1804.%20Implement%20Trie%20II%20(Prefix%20Tree)/)的概念，我們可以維護一個`prefixCount`

當我們在insert字母的時候，沿著路徑增加**val**，這樣當我們在query總共有多少個單字含有`key`作為prefix時，直接返回`prefixCount`即可

而在更新的時候，由於當單字已存在時，我們必須直接更新它的**val**，因此我們可以很直覺的想到我們需要一個`hashmap`來維護每個`key`所對應的**val**是多少

- 如果key不存在，也就是還沒有新增過的話，我們沿路將val加到`prefixCount`
- 如果key存在於`hashmap`裡，那我們沿路更新delta value即可. (delta = current val - past val)