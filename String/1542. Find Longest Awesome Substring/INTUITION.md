# Intuition

- s[i]: only 0-9 => 共十位
- substring最多只能有一個digit是奇數個

如果用長度為10的bitmask來表示每個digit的奇偶數的話, ex. 0000001010代表digit "1"跟"3" 為奇數

再來想到利用prefix sum找一段合法substing的概念

```
X X X X X X X X X X X X
          j           i
```

如果在`i`位置狀態為: 0000001010
那們我們只要往回找到`j`, 其狀態為0000001000或0000000010或0000001010這三種情形的substring都能使得s[j:i]為palindrome
所以我們用hashmap儲存**{ state: index }**
遍歷過程中再遍歷10個bit位來查找有沒有state_j使得state_i-state_j這段substring可以為:
- odd palindrome: 保留1個奇數個的digit, 其他湊成偶數.
    - 遍歷10個bit位, 查找hashmap看有沒有存在`state^(1<<j) for j in range(10)`使得只有該bit位為奇數個
- even palindrome: 找到一個跟自己bitmask狀態相同的, 這樣s[j:i]這段substring的digit就會全偶數個
    - 查找hashmap看過往有沒有跟自己相同state的prefix string

# Complexity

- time complexity:
    $$O(n*10)$$
- space complexity:
    $$O(2^10)$$