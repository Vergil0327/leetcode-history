# Intuition

```
example 3.
values = 1 3 1 4 1 5
         i k       j
         i   k     j
         i     k   j
         i       k j
```

fix arr[i], arr[j] as choosing vertices, then choose an arr[k] as 3rd vertex, then:

```
score(arr[i:j]) = score(arr[i:k]) + score(arr[k:j]) + arr[i]*arr[k]*arr[j]

=> dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i]*arr[k]*arr[j])
   where dp[i][j] = minimum score for arr[i:j] (both inclusive)
```

這題首先要想到是當我們選擇arr[i], arr[j]兩點後
我們可以任選arr[k] where i < k < j作為第三個點頂點形成三角形
```
X X X X X X X X X X
i     k           j    
```
當我們選擇arr[i], arr[j], arr[k]後, 此時當前選擇的分數為`arr[i]*arr[k]*arr[j]`
然後我們在繼續在剩下的區間劃分三角形, 也就是:

我們定義dp[i][j] = minimum score for arr[i:j] (both inclusive) by using i & j as 2 vertices for triangle

那麼狀態轉移很自然地為:
``
dp[i][j] = dp[i][k] + dp[k][j] + arr[i]*arr[k]*arr[j]
         以(i,k)為頂點＋以(k,j)為頂點+當前選擇(i,k,j)
```
```
1  2

4  3
```
透過example來看會更清楚, 當我們arr[i], arr[j] = 1, 4時
如果k = 2, [123]一個三角形
如果k = 3, [134]一個三角形
然後再看 [i:k] 跟 [k:j] 這區間內的三角形, 其中頂點為(i & k)及(k & j)
