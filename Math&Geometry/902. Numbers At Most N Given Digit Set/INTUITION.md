# Intuition

```py
n = len(str(targets))
m = len(digits)
```

構造出的長度小於n時, 構造出來的數肯定都比較小:
這時如果構造長度是一位數的話, 一個位數有m種digits可選, 所以有`m ** 1`種可能
組成二位數有`m ** 2`種可能
組成N位數有`m ** n`種可能
這些都可以累加起來

最後再查看長度相等時有哪些構造方法
直覺想到的是從左到右, 從高位到低位
1. 如果構造的數字, 與n的同位數字相等, 那就看後面
2. 如果構造的數字小於n的同位數字的, 那後面位數都可以任意構造

所以我們可以用bisect_right找出能用的digits有哪些, 找出upperbound
如果`j = bisect_right(digits, target[i])`
我們分情況討論

```
ex. digits=[3,4,5,6], n = 645
```

如果今天digits=[3,4,5]
那們對於同樣三位數長度的構造, 我們第一位數三種都可選
並且由於首位數都比n還小, 所以後面每一位也都有len(digits)種可能可選
所以第一位數有`bisect.bisect_right(digits, "6")`種可能
剩下兩個位數都有`len(digits)`種可能
所以再加上`bisect.bisect_right(digits, "6") * len(digits)**2`即可

但現在digits = [3,4,5,6]
所以首位數放3,4,5都是跟前面狀況一樣, 所以是:
```py
j = bisect.bisect_right(digits, "6")
res += j * len(digits)**2
```

但在首位數放6的情況下, 我們下個位數變成不可以超過"4"
所以必須再往下討論
```
    6    4    5
放3 1 * len(digits)**2
放4 1 * len(digits)**2
放5 1 * len(digits)**2
放6 1 * bisect.bisect_right(digits, "4"), 然後看下一位數
```

所以這邊我的處理方法是
在找出`upperbound = j = bisect.bisect_right(digits, t[i])`後
如果首位數小於target[i], 那直接加上`res += j * len(digits)**(tLength-i-1)`即可

不然的話就加上`res += (j-1) * len(digits)**(tLength-i-1)`
然後我們在sameDigit.append(digits[j-1])
```py
sameDigit = []
for i in range(tLength):
    j = bisect.bisect_right(digits, t[i])
    if digits[j-1] == t[i]:
        res += (j-1) * len(digits)**(tLength-i-1)
        sameDigit.append(digits[j-1])
    else:
        res += j * len(digits)**(tLength-i-1)
        break
```

- 如果最後`sameDigit.length == len(str(n))`, 代表我們可以構造出一個跟n一模一樣的數
所以最後答案必須再加1
- 如果`sameDigit.length != len(str(n))`, 那代表在某個時候就會進到前面討論的那種情況, 在更之後的所有位數都可以任意挑選. 所以此時能構造的數目就是`res += j * len(digits)**(tLength-i-1)`

```
n   = X X X X X X X X
構造 = X X X X Y _ _ _ => 其中Y<X
這時構造方法就會是bisect_right(digits, "Y") * len(digits)**3
```

# Other Solution

其實真正要關注的就是跟str(n)相同位數的情況, 這情況要單獨特別處理
至於前面的`len(str(n))-1`位數都可以很快計算出來

```py
for l in range(1, len(str(n))):
    res += len(digits) ** l
```

而最後這情形我們可以用dfs來單獨處理

```py
k = len(str(n))
t = str(n)
def dfs(i):
    if i == k:
        res += 1
        return

    for d in digits:
        if d < t[i]:
            res += pow(len(digits), k-1-i)
        elif d == t[i]:
            dfs(i+1)
dfs(0)
return res

```