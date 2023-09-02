# Intuition

標準sliding window題目
我們只要維護一個k-length的sliding window並且:
- 用**Hashmap**去維護該window有多少個distinct characters
- 以及一個變數`windowSum`來維護sum of sliding window

再根據題意, 只要`長度為k`且`distinct characters數目>=m`時, 即為合法sliding window
我們在這個合法條件下持續更新`res`即可
