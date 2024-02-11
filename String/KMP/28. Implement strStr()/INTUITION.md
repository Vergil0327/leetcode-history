# Dynamic Programming

## Intuition

- build: 利用`dp`紀錄`needle`的狀態轉移過程
- search: 透過`dp`去匹配`haystack`，透過`dp`可知道
  - `haystack[i]`如果與`dp`匹配可以繼續下去
  - 如果不匹配，便透過`dp`儲存的訊息找到上一個狀態(previous longest prefix state)

`haystack`某部分與全部匹配，代表這部分與`needle`也互相匹配
