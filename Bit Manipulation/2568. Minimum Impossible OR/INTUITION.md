# Intuition

我們從二進位制來看，OR可以讓bit position變為1
所以我們只要檢查第一個沒有1的bit即為最小遺失的正整數

ex.
只要有1，就能讓第一個bit為1
只要有2 (1<<1)，就能讓第二個bit為1
只要有4 (1<<2)，就能讓第三個bit為1
只要有8 (1<<3)，就能讓第四個bit為1
並且在8以下的數都可以透過任意組合互相OR而形成
因此答案就是第一個遺失的2的倍數

```
   1 -> num = 1
  10 -> num = 2
  11 -> num = 3
   
 100 -> num = 4
 101 -> num = 5 -> 100 | 001
 110 -> num = 6 -> 100 | 010
 111 -> num = 7
1
```