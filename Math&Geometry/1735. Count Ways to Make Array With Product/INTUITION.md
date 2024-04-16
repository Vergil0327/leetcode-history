# Intuition
    
推薦[@HuifengGuan](https://www.youtube.com/watch?v=ROde-ATrCBs&ab_channel=HuifengGuan)的影片詳解

首先想到是將k分成質因數後然後再從裡面組合出n-size的array

假設n=3, k = a * b * b * c => 這些prime factors中要取出3個來
=> 相當於在這四個數之間放兩個擋板:

a | b | b  c = a * b * (b*c) = a * b * (c*b)
a | b  b | c = a * (b*b) * c = a * (b*b) * c (duplicate)
a  b | b | c = (a*b) * b * c = (b*a) * b * c

=> C(3, 2) => 3個間隔位置中挑兩個位置放擋板


但實際上看example, n=2, k=6=2*3
ways = [1,6], [2,3], [3,2], [6,1]

變成他n-size array中其實是允許分成空的, 只是空代表1

```
ways = [_, 2*3], [2, 3], 後面只是duplicate先不管
     = [1, 2*3], [2, 3]
```

=> 相當於在三個數中放一個擋板, 隔出size=2的array
=> 1 | 2 3 = 1*(2*3) = 1*(3*2)
=> 2 | 3 = 2*3 = 3*2

意思是如果我們有k個prime factors, 要分出n-size group並且group可為空的話, 那有幾種分法?
答案是: **C(k+n-1, n-1) = C(k+n-1, k)**

意思是我們在k個選擇裡, 在加上n個空位, 那這樣總共有k+n-1個間隔
然後一樣插入n-1個擋板分出n-size group
那這樣最終求出的, 就是我們要的方法數

所以在看回剛剛的n=2, k=6=2*3
我們得先找出每個unique permutations後, 再用插入隔板的方法去計算

ex. C(k+n-1, n-1) = C(2+2-1, 2-1) = C(3, 1), 就是可以想成k = 2*3*1*1 = 2*1*3*1 = ...各種排列, 然後3個間隔裡選位置放入1個隔板
並只計算unique permutations

時間複雜度來看, 這樣還是不好計算的

所以這題除了要想到**C(k+n-1, n-1)**這個數學結論外
還得再想到另外一個突破口是:  我們不要整個prime factors排列來看, 我們個別個別來分出n-size group

ex. n=3, k = a * b * b * c * c * c * c

我們就看:
1. a: C(1+3-1, 3-1) = C(3,2)
2. b*b: C(2+3-1, 3-1) = C(4,2)
3. c*c*c*c: C(4+3-1, 3-1) = C(6,2)

最後在全部相乘, 那就得到n-size array的所有方法數了


## Helper function Cmn

1. 預處理Cmn
```py
m = n = 1001
comb = [[0]*n for _ in range(m)]

for i in range(m):
    comb[i][i] = comb[i][0] = 1
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
```


2. 直接計算Cmn
```py
def Cmn(m, n):
    cnt = 1
    for i in range(n):
        cnt *= m - i
        cnt /= i + 1
    return cnt
```