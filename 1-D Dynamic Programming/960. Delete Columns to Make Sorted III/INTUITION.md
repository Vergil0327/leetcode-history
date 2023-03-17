# Intuition

這題其實是一個很巧妙的LIS變化題
我們看一下`strs`, 我們要求的是要刪除最少column使得每一row的strs[i]最長

想一下LIS, s="XXXXXXXXX"
如果是單一個s, 最少的刪除數使得s是有序的那就先找出他的LIS, len(s)-len(LIS) 就是他的最少刪除數

這題也是一樣概念，我們要看的是刪除哪些column, 所以我們要把每個strs[i]的同column看作一起，想成是一個character
這樣當第i-th column的每個character都大於等於第j-th column時，代表i-th column可以接在j-th column後面
那一樣，一但我們column by column的求出LIS後, 答案就是`len(strs[0]) - max length of LIS`
```
strs=[
       LIS[0] LIS[1] LIS[2] LIS[3]
                             _
         X     X      X      X     X X X X...
         Y     Y      Y      Y     Y Y Y Y...
         Z     Z      Z      Z     Z Z Z Z...
                             -
     ]         j             i
```