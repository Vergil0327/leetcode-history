# Intuition

目標是要把word或reversed(word)能剛剛好的放進直行或橫列裡去

所以:
1. 首先, 我們可以先遍歷每個橫列, 再遍歷每個直行
2. 然後看這些非`#`的直行橫列長度有沒有等於`len(word)`
   1. 如果沒有, 那肯定為False. 繼續往下找
   2. 如果有, 那就比對看看這段直行橫列組成的string能不能填進word或reversed(word)

確認方式也很簡單, 方法如下
`" "`可填入任意字母, 所以我們只需要比對非空位置有沒有與word[i]或reversed(word)[i]相等即可

```py
revWord = word[::-1]
def check(s):
    valid = validRev = True
    for k in range(len(word)):
        if s[k] == " ": continue
        if s[k] != word[k]:
            valid = False
        if s[k] != revWord[k]:
            validRev = False

    return valid or validRev
```

