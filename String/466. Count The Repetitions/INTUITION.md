# Intuition

這題brute force的方式就是遍歷`str1`一遍，反覆環形找尋有幾個s2，並將重複的次數除以s2的重複次數即可

但如果要更高效率的話，那我們就得找出重複的pattern的起點與終點

想法依舊是從brute force去做延伸，我們可以想成兩個無限長的`s1`及`s2`，我們持續紀錄`s1`與`s2`每個相同字符的index位置到hashmap中，key則為他們各自index對長度取餘，使`i`,`j`落在`[0,m]`與`[0,n]`之間

一但我們從hashmap裡發現上個相同的key時，代表我們已經cycle/repeat了一次完整循環，我們可以找出`i`, `j`一個cycle的長度必且透過`(s1*n1 - i) // (i- prev_i)`找出我們後續程度還會重複幾次這個pattern

等到遍歷完`str1`後，透過index `j` 移動的距離除以`len(s2)`就知道這段距離是幾個`s2`組成，再除以`n2`即可知道有多少個`str2`