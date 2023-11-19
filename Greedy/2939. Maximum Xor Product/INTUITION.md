# Intuition

由於要找出`a'*b'`乘積最大, 我們由高位往低位看i-th bit

首先: 大於n位以上的bit我們無法更動, a'[i] = a[i], b'[i] = b[i]
再來: 
```
a[i] b[i]
  0     0 -> 透過XOR set 1
  1     1 -> set 1

  a', b'越相近, 乘積越大. ex. "1101" * "111" vs "1111" * "101" = 13*7 vs 15*5
  1     0 -> set smaller min(a', b')[i] = 1
  0     1 -> set smaller min(a', b')[i] = 1
```
