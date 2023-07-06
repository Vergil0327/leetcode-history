# Intuition

```
coins = 1 1 1 4
coins = 1 2 3 4
coins = 1 3 4 5
```

首先先想到對coins排序, 因為在湊數字時一定是小coin先湊，然後慢慢把maximum number of consecutive integer加上去
如果當前都湊到的最大連續數為`res`, 那麼我們的下個目標是湊齊res+1, res+2, ...
如果下個coins[i]大於res+1, 那麼我們永遠湊不出res+1這個數
但如果下個coins[i] <= res+1, 那麼就可以自己或跟之前某些數湊成res+1
ex. 如果coins[i] = res, 那就跟之前的1構成res+1
ex. 如果coins[i] = res-1, 那就跟之前的2構成res+1

所以只要coins[i] <= res+1, 那麼我們就能一路連續構成到res+coins[i]