### Bit Operation

首先我們最直覺的想法應該是
我們就用減法，減幾次就是除幾次
但這樣如果`dividend=2^30, divisor=1`，我們就要減2^30次，明顯效率很低

因此這邊我們可以藉由binary search的模式，我們透過**bit operation**
我們每次成功減了一次，我們就將`divisor` *= 2，亦即`divisor<<1`
同時我們必須記錄我們放大`divisor`幾次，所以利用一個變數`base`來紀錄

但如果我們的`dividend`小於`divisor`呢?
那我們就再將`divisor`變回**1**，然後重複再一次，直到`dividend`小於最初的`divisor`

另外這邊必須注意`正負號`，所以再利用另一個**boolean**來紀錄是否為負

最後別忘記最後的答案必須介於[-2**31, 2**31-1]之間

### Optimized Solution

既然我們有了上面由小減到大的解法
反之，我們也可以從大減到小，來提高效率
透過一個while loop來找出最大可減多少，並同時紀錄減多少次(`base` variable)
依序減下來即可

**Intuition**

***inspired by binary search***

let's use bit operation to multiply **divisor** by 2 (let's say it **divisor*** after multiplication) at each iteration until dividend < **divisor**

if dividend < **divisor***, repeat above iteration again from original **divisor**

- use boolean value to store answer is negative or not
- also be careful of lowerbound and upperbound [-2^31, 2^31-1]