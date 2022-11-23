這題目的是要找出重複的路徑刪除後，返回剩下的檔案路徑

1. 首先很明顯能知道的是我們可以用字典樹(Trie)來記錄我們的路徑

2. 如此一來問題變轉為[leetcode 652](../../Trees/652.%20Find%20Duplicate%20Subtrees/)，找出重複的subtree並刪除
   1. 首先我們得利用`Hashmap`與將子樹`序列化(serialization)`後才方便我們找出重複的子樹
   2. 但這題有點不一樣的是，重複的子樹與根節點無關，只要子樹重複便必須刪除，所以我們僅需用子節點的資訊來序列化
   ```python
   key += str(serialize(root.next[c])) + "$" + root.next[c].folder + "$" 
   ```
   3. 另外由於我們的序列化後的字串可能會很長，因此我們可以透過字串與單調遞增的數字作對映，來避免我們的serialized str過長。過長也會影響加入到hashmap時的效能
   4. 另外紀錄serialized string出現的頻率來幫助辨別是否有重複
   5. *注意* 這邊有個不好發現的問題是，我們在序列化的時候必須對我們字典樹(Trie)做排序，或者是使用SortedList來實作TrieNode。因為在序列化子節點時，不應該因為排序而產生不同的key

3. 將所有subtree序列化後，便可以透過DFS backtracking來找出未重複的路徑
   1. 這邊要注意，根據我們的序列化公式，所有leaf node的key都會是空字串，這會導致我們的所有leaf node的出現頻率會全部加總而導致評估duplicate錯誤。
   2. 因此在backtracking時必須同時確認key不為空字串且出現頻率超過一次