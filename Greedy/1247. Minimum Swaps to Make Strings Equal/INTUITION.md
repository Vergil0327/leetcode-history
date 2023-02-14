# Greedy
## Intuition

首先如果`x`跟`y`的數量不是偶數的話，那肯定兩個肯定無法相等，直接返回`-1`

再來由於交換必定是成對的，因此我們可以記錄其中一邊要交換的字符是什麼
而且我們只要紀錄s1[i] != s2[i]的位置即可

```py
stack = []
for i in range(len(s1)):
    if s1[i] != s2[i]:
        stack.append(s1[i])
```

由於我們已經排除掉不可能的情況，因此剩下的情況僅剩兩種

如果是`xx`跟`yy`交換，那麼僅需交換一次
如果是`xy`跟`yx`交換，那麼需要交換兩次

盡量優先以`xx`跟`yy`的方式，這樣一次交換即可，`swap += 1`
如果s1這邊要換的是`xx`，那麼就是跟s2的`yy`交換，由於必定是成對的，所以我們只看一邊即可

等到無法以`xx`跟`yy`方式交換後，剩下的就用`xy`跟`yx`交換的方式，這情形需要`swap += 2`


因此我們可以對stack排個序，這樣會變成`[xxxxxxxxxxyyyyyyyyyyyyy]`
不管怎樣，排序後遍歷過去
兩個兩個看，就會自然盡量地優先以`xx`或`yy`的方式計算了

這樣遍歷過去後頂多就只有xy交界處有可能是以`xy`的形式跟對面交換(如果`x`, `y`是奇數個才會，偶數則不會發生)

兩種情況
1. `xxxx...xxx [xy] yyyy...yyyy`，x跟y是奇數個
2. `xxxx...xxxx [] yyyyy...yyyy`，x跟y是偶數個

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity

$$O(n)$$