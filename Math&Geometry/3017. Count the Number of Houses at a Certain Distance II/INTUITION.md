# Intuition

首先發現整個圖形會是對稱的:
- 兩端會是線性
- 中間部分會是一個環

```
O-O-O-O-X- Cycle -Y-O-O-O-O-
 left    middle    right
```

加上數據規模到$10^5$, 這題看起來會像是math problem, 並且應當分區討論, 兩端線性跟中間環來討論
我們先定義x < y, 這樣我們就能以節點`x`跟節點`y`做出分界:

但首先, 我們先看沒有cycle的情況, **example 3**:
```
 A -> B -> O -> O -> O -> ...
i=0.  1    2.   3.   4
```

先看節點A:
一個edge, A只能走到i=1
兩個edge, A能走到i=2
...

節點B:
一個edge, 走到i=0跟i=3 => 走到i=0其實就是A走到B的反方向pair
兩個edge, 走到i=4
...

所以我們可以計算只往右邊節點的情況, 最後數目在乘以2就好

所以從這邊可以先知道, 假如x=y的話, 代表沒有中間的環
這種純線性的特殊情況我們就可以這麼計算:

我們遍歷`n-1`個edges `0 <= k <= n-1`,
- 對於1個edge, 亦即k=1的情況, 有n-1種情況:
    - i=0 -> i=1
    - i=1 -> i=2
    - 直到i=n-2 -> i=n-1

- 對於2個edge, 亦即k=2的情況則有`n-2`種往右方向的pair

全部計算完後由於每種pair都可以相反過來(u -> v) == (u <- v)
所以每種情況在乘以2即為答案

## x == y時:

```py
pair = [0]*n
for k in range(1, n):
    pair[k-1] += n-k

return [p*2 for p in pair]
```

到這邊有個感覺是, 我們要計算的是從每個點出發, 每次往兩端走, 如果走到`x`或`y`再多條shortcut
計算的是每多走一步, 我們從當前位置能走到哪些點, 這些點的數目也就代表能產生多少pair

如果對於i-th point來說, 我們定義dp[t] = the number of pairs at t steps where 1 <= t <= n-1
最終結果的res[t-1] = 每個點的dp[t]的總和

*note. **res**是0-indexed, **t**是1-indexed*

那麼再來就是這個dp[t]該如何計算?


首先我們前面看到這三個group分別為:
```
O-O-O-O-X- Cycle -Y-O-O-O-O-
   left    middle    right
```

所以首先起點可能從:
- left
- middle
- right
這三個地方出發

那他們在走`t`步後形成的pair, 則有可能是:
- left
  1. left + left
  2. left + middle: left -> x -> middle (left center)
  3. left + right
- right
  1. right + right
  2. right + middle: middle (right center) <- y <- right
  3. right + left
- middle
  1. middle + middle
  2. middle + left
  3. middle + right

整理一下, ex. left+right跟right+left這兩種其實可以是同個pair只是反向, 計算上就是計算一邊再乘以2即可
所以我們在走`t`步的情況下的可能pair有以下這幾種情況
1. left + left: 兩點都在left區域
2. right + right: 兩點都在right區域
3. left + right: left -> x -> y -> right 或反向
4. left + middle (left center)
5. right + middle (right center)
6. middle + middle

所以我們只要把這幾種情況都加總起來, 就知道`t`個edges總共有多少個pair

那麼`1.`, `2.`兩種情況都是線性無分岔, 數同種情況可用個**helper func1**來計算
再來`3.`單獨計算, **helper func2**
而`4.`, `5.`兩種情況都是線性經過`x`或`y`分岔, 應當也能用同個**helper func3**計算
最後`6.`也單獨計算, **helper func2**

所以我們只要實作出這幾個helper function, 即可.

size:

- left = 長度為`x-1`的單鏈
- right = 長度為`n-y`的單鏈
- middleCycle = 長度為`y-x+1`的環


## helper func1

首先是單鏈:

我們的點必須介於`1 <= i <= size` (1-indexed)
那我們找另一點`j = i+t`並且同樣也必須落在`1 <= j <= size` => 可導出`1 <= i <= size-t`
所以對於`i`來說, 他有`(size-t) - 1 + 1`個`j`可作為配對
```py
def func1(size):
    count = [0]*n
    for t in range(1, n+1):
        idx = t-1
        l, r = 1, size-t
        count[idx] += max(0, r-l+1) # 用max(0, value)來避免加總到無意義的負數(r<l)
    return count
```

## helper func2

```
O-O-O-O-X--Y-O-O-O-O-
  left         right
```

left-to-right: 肯定是走shortcut `X-Y`
一樣來看(i, j) pair, 其中:

- i在left裡, `1 <= i <= left.size`
- j要在right裡, `1 <= j <= right.size`
  - j為`i+t`, 那他的上下界分別為
    - left至少也要經過`X`,`Y`然後在走一步後才能是`j`, 所以`left.size+X這個點+Y這個點+1步 = left.size+3 <= i+t`
    - 同樣地, i+t <= left.size + 2 + right.size
    - left.size+3 <= j=i+t <= left.size + 2 + right.size

所以綜合來看:
1. 1 <= i <= left.size
2. left.size+3 <= i+t <= left.size + 2 + right.size
3. 得出: max(1, left.size+3-t) <= i <= min(left.size, left.size+2+right.size-t)

```py
def func2(left, right):
    count = [0]*n
    for t in range(1, n+1):
        l, r = max(1, left+3-t), min(left, left+2+right-t)
        count[t-1] += max(0, r-l+1)
    return count
```

### helper func3

**left-to-middle** and **right-to-middle**

left to {middle_left or middle_right}: (i,j)

`x`這點在兩條分岔重疊, 單獨計算避免重複

- (i, middle_left exclude x) pair: i -> x -> middle_left
   1. 1 <= i <= left
   2. left+2 <= i+t <= left+1+middle_left
- (i, middle_right exclude x) pair: i -> x -> middle_right
   1. 1 <= i <= left
   2. left+2 <= i+t <= left+1+middle_right
- (i, x) pair: i -> x
  1. 1 <= i <= left
  2. i+t == left+1
  3. thus, 1 <= left+1-t => t <= left


```py
def func3(size, middle_left, middle_right):
    count = [0] * n
    # (i, middle_left exclude x)
    for t in range(1, n+1):
        l = max(1, size+2-t)
        r = min(size, size+1+middle_left-t)
        
        count[t-1] += max(0, r-l+1)

    # (i, middle_right exclude x)
    for t in range(1, n+1):
        l = max(1, size+2-t)
        r = min(size, size+1+middle_right-t)
        
        count[t-1] += max(0, r-l+1)

    # (i, x) where i in size
    for t in range(1, n+1):
        if t <= size:
            count[t-1] += 1
    return count
```

### helper func4

X-0-0-0-Y
|_______|

(i,j) = (i, i+t) pair
- clockwise = t
- counterclockwise = size-t
- 當`clockwise < counterclockwise`時, 代表這時的(i,i+t)pair確實是最短路徑 => 總共有`cycle_size`個點所以`+= cycle_size`
- 這邊有一點要注意的是, 我們前面的所有count[t]最後都要乘以2(同條路徑兩個方向), 但是當`clockwise == counterclockwise`時, 已經包含了兩個方向了, 所以這部分我們拆出來
    - ex. X - A - B - Y:
      - 當t=2時, (X,B), (A,Y), (B,X), (Y,A)

```py
def func4(size):
    count = [0]*n
    alreadyMultiply2 = [0]*n
    for t in range(1, n+1):
        clockwise = t
        counterclockwise = size-t
        if clockwise < counterclockwise: # clockwise的(i, i+t)是最短路徑, 這時(i,j)是合法pair
            count[t-1] += size
        elif clockwise == counterclockwise:
            alreadyMultiply2[t-1] += size
    return count, alreadyMultiply2
```

所以最終結果就會是:

```py
left = x-1
right = n-y

arr1 = func1(left)
arr2 = func1(right)
arr3 = func2(left, right)

middle_left_size = (y-x)//2
middle_right_size = (y-x+1)//2
arr4 = func3(left, middle_left_size, middle_right_size)
arr5 = func3(right, middle_right_size, middle_left_size)

middle = y-x+1
arr6, alreadyX2 = func4(middle)

tmp = [sum(arrs)*2 for arrs in zip(arr1, arr2, arr3, arr4, arr5, arr6)]
return [x+y for x, y in zip(tmp, alreadyX2)]
```

