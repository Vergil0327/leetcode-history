# Intuition

```
00 -> 10 -> same as third
01
    - 010 ->  001 -> 101
    - 011 ->  
        - 0110 -> 0101 -> 0011 -> 1011
        - 0111 -> end
10
    100 -> 110 -> end
    101 -> same as second
11
```

相當於:
```
   1110110
-> 1110011
-> 1111011
```

然後我們的目標是從高位往低位, 高位盡可能都是1

所以從可行的操作來看
- 只要是"00", 我們肯定轉換成"10"這樣數值最大
- 但要是"01", 從上面推導可發現, 只要後面還有`0`, 那肯定能透過`10->01`操作把後面的`0`慢慢的換上來然後再將`"00"`變成`"10"`


1. 所以我們排除leading zeros後
2. 把遇到的每個0都跟後面的**remining zeros**組合成`00`然後轉成`10`, 直到整個binary string裡的`remain zeros=1`
3. 最後一位`0`後的每一位都是`1`

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$