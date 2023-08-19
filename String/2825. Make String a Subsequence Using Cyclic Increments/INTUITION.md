# Intuition

我們可以任意選取str1的subset, 將字符全部往後推進一位, 也就是:

```
a -> b

b -> c

x -> y

y -> z

z -> a
```

由於要看能不能在至多一次的操作下，使得str2為str1的一個subsequence

這代表str2要依序出現在str1裡, 由於我們可以任意選取`str1[i]`進行操作, 這代表`str1[i]`其實可以有兩種狀態:

1. 原本的`str1[i]`
2. 進行操作後的`str1[i]`


那這樣我們用`j`指針代表我們當前缺少的str2[j], 並且遍歷str1:

只要`str1[i] == str2[j]`或`operation(str1[i]) == str[j]`, 那我們就能移動`j`指針, 一但`j`指針走到`len(str2)`就代表str1的subsequence可以組成str2了

# Complexity

- time complexity:

    $O(n)$

- space complexity

    $O(n)$