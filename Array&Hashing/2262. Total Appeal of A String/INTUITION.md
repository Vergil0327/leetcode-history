# Intuition

對於這種題目, 有想到是要查看每個s[i]的貢獻值然後再加總
但可惜沒能想出如何去除重複

這題想法是這樣:
找出每個s[i]有所貢獻的subarray有多少, 亦即含有s[i]的所有substr
那這樣就能知道s[i]的appeal貢獻值有多少

```
ex. [X X X X X X X] a [X X X X X X X X X X]
         left                right
```
對於a來說, 他的substr有`left*right`個

但由於為了去除重複計算, ex. [X a X X X a X], 含有a的subarray個數我們統一在最左邊的a計算
那這樣含有s[i]的substr = 左邊界可到最後一個s[i] occurence的位置+1 * 右邊所有character個數
```
abbca
a = left * right = 1 * 5
 b = left * right = 2 * 4
  b = left * right = 1 * 3
   c = left * right = 4 * 2
    a = left * right = 4 * 1

亦即對於一個[X X X X X a {X X X X X X X a X X X X X}]
                     j                i             n
                        l                       r
對於s[i]的貢獻 = (i-j) * (n-i)
```