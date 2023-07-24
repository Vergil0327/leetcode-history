# Intuition

作法跟求base-2沒有任何區別, 僅需要處理當remainder < 0的情況:


```
# base 2 func

check last digit by N%2 or N&1.
If it's 1, you get 1.
If it's 0, you get 0.

shift to right n >> 1.
This actually do two things:
2.1 Minus 1 if last digit is 1.
2.2 Divide N by 2.
```

```
So if after doing "remainder = n % negBase" and 
"n = n/negBase", we get negative remainder, we do 
following.
remainder = remainder + (-negBase)
n = n + 1

ex.
  prevN = curN * (-2) + remainder
  //when remainder <0, add +2-2 on right side, where use +2 to make the remainder positive 
  prevN = curN *(-2) + remainder + 2 -2
  prevN = curN *(-2) -2 + remainder + 2
  prevN = (-2) * (curN +1) + remainder+2
```

[See this article - Convert a number into negative base representation](https://www.geeksforgeeks.org/convert-number-negative-base-representation/)
