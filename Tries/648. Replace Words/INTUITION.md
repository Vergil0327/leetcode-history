### Trie

首先透過dictionary建立Trie

然後對於sentence裡的每個word
一一透過Trie來找尋是否有`root`的存在

- 一但有就取代並停止往下搜尋
- 沒有就保留原word