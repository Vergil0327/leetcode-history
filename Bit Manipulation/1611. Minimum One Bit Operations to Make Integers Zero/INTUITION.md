# Intuition

[English Version](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/solutions/4345383/observation-nov-day-30-daily-challenge/)

10^9轉2進制為"111011100110101100101000000000"
=> 30位

首先轉成bit來想

ex. n = 4 (0b100) answer=7

101 op1
111 op2
110 op1
010 op2
011 op1
001 op2
000 op1

高位轉為0的手段只有op2, 但能消除的前提是"1"後面必須帶"100000..."
所以目標是把當前的bit整理成"110000000...",然後消除最高位的1後, 再一次地把1從低位推上來消除
110000000 -> 010000000->010000001->010000011->010000010->010000110->010000111->010000101...

而將n轉為0的最快速方法就是從左往右依序將高位的1消除掉
ex. "1111":
1111->1101->1100->0100->0101->0111->0110->0010->0011->0001->0000

所以為了整理成"110000000...", 必須透過"1000..."慢慢下手
我們看"100000..."可以怎用:
ex. 1 -> 0
ex. 10 -> 11 -> 01 -> 00 = 10 -> 11 -> 01 (previous result)
ex. 100 -> 101 -> 111 -> 110 -> 010 (previous result)
ex. 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 (previous result)

2^0 = dp[0] = 1
2^1 = dp[1] = 2 + dp[0]
2^2 = dp[2] = 4 + dp[1]
2^3 = dp[3] = 8 + dp[2]
...
2^k = dp[k] = 2^k + dp[k-1]

然後在看非2^k次方的數值, 由上面推導可觀察出:
如果現在數值是101, 101 = 100 + 1 = dp[2]-dp[0]
1010 = 1000 + 10 = dp[3] - dp[1]
1011 = 1000 + 11 = 1000 + 10 + 1 = dp[3]-(dp[1]-dp[0])
=> iteration: res = dp[0] => res = dp[1]-res => res = dp[3]-res
=> res = dp[k] - res

that is, 
```py
res = 0
res = dp[0] - res
res = dp[1] - res
res = dp[3] - res
```
=> in iteration form:
```py
res = dp[k] - res where k is log2(LSB)
```

所以我們首先先建出dp[i] table, 然後再將n表示成: 2^a + 2^b + 2^c + ...
因此我們可以用iteration持續求出LSB, 然後計算出最終結果:

Apporach:
1. LSB = n & -n
2. 那麼`k`就等於`int(log2(lsb))`
3. 所以res = dp[k] - res
4. 反覆進行iteration 求出res
