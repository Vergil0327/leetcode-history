# Intuition

2D prefix sum的概念, 題意要求的是從左上(0,0)到右下(i,j)的整個矩形XOR值

所以我們能用2D prefix sum的概念:
到(i,j)為止的矩形XOR剛好是: `preXOR[i-1][j]^preXOR[i][j-1]^preXOR[i-1][j-1]^mat[i][j]`

1. preXOR[i-1][j] = mat[i-1][0]^...^mat[i-1][j]
2. preXOR[i][j-1] = mat[i][0]^...^mat[i][j-1]

上面兩者互相XOR後會發現`preXOR[i-1][j-1]`這段XOR了兩次
所以我們還得在XOR一次`preXOR[i-1][j-1]`回來

所以最終XOR[i][j] = mat[i][j] XOR preXOR[i-1][j]


```
mat:
a b c
d e f

prefix xor:
a a^b a^b^c
d d^e d^e^f

從上面可發現我們要的:
a    a^b        a^b^c
a^d  a^b^d^e    a^b^c^d^e^f

相當於
a    a^b                a^b^c
d^a (a^b)^(a^d)^a^e     (a^b^c)^(a^b^d^e)^(a^b)^f

左邊 XOR 上面 XOR 左上 XOR matrix[i][j]
```

那再來我們只要在遍歷過程中, 利用priority queue去維護一個k-size的min heap
即可找出k-th largest value
