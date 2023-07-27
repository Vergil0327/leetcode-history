# Intuition

這是當初pass的想法

```
[X X X X X] [X X X X X] [X X X X]
         i               j
```
we want split arr like above and make `binary(arr[:i]) = binary(arr[i+1:j-1]) = binary(arr[j:])`

if we make prefix bin(arr[:i]) equal suffix bin(arr[j:]), then the middle part will also be determined.
we can further check if middle part is equal or not.

thus, we can use two pointers from both ends to determine prefix and suffix until two binary values are equal,
then, check middle part

1. left part: left = (left>>1)|arr[i]
2. right part: right |= arr[j]<<(n-1-j)
3. as for middle part, we need decrement middle part while i, j moving towards middle

since leading zeros are valid, this condition makes problem tricky

example 1. arr = 10101
prefix = 1, suffix = 1, middle = 010 = 2 => not equal
but prefix = 1, suffix = 01, middle = 01 => all equal

thus, we can keep moving j if arr[j] is leading zero to shrink middle-part

所以當初的想法變寫成下面這種形式
每當移動left-part, middle -= 1<<(j-i) if arr[j] == 1
然後移動right:
```py
while j > i+1 and right < left:
    if arr[j]:
        right |= 1<<(n-1-j)
    middle >>= 1
    j -= 1
```
然後當兩者一樣時就判斷middle:

```py
if left == right == middle: # check middle
    return [i, min(j+1, n-1)] # => for edge case: arr = [0,0,0,0,0]
```
但由於這邊會遇到如果left已經等於right, 那麼上一步的j其實就不會移動
所以才套了個min(j+1, n-1)

然後再考慮arr[j] == 0時, 我們可以增加suffix的leading zeros來縮小middle
```py
# shrink middle if arr[j] == 0
while j > i+1 and right == left and arr[j] == 0:
    middle >>= 1
    j -= 1

    if middle == left:
        return [i, j+1]
```

整體如下
```py
def threeEqualParts(self, arr: List[int]) -> List[int]:
    n = len(arr)
    
    middle = 0
    for v in arr:
        middle = (middle<<1) | v

    left = right = 0
    i = 0
    j = n-1
    while i < j+1:
        left = (left<<1)|arr[i]
        if arr[i]:
            middle -= 1<<(j-i)

        while j > i+1 and right < left:
            if arr[j]:
                right |= 1<<(n-1-j)
            middle >>= 1
            j -= 1
        
        if left == right == middle: # check middle
            return [i, min(j+1, n-1)] # => for edge case: arr = [0,0,0,0,0]

        # shrink middle if arr[j] == 0
        while j > i+1 and right == left and arr[j] == 0:
            middle >>= 1
            j -= 1

            if middle == left:
                return [i, j+1]
        
        i += 1
        
    return [-1, -1]
```

雖然會過, 但感覺這步
```py
if left == right == middle: # check middle
    return [i, min(j+1, n-1)] # => for edge case: arr = [0,0,0,0,0]
```
是比較有瑕疵的, 而且也利用了python方便的特性讓bit超過一般常見的32位, 64位

所以接下來才是個比較好的做法

# Greater Solution

由於要分配成三個相等的part, left = middle = right

由於leading zeros是沒有作用的, 所以實際三個part會如下所示:

```
00000 1XXXXXX 00 1XXXXXX 0000000 1XXXXXX
        left      middle          right
```

所以我們一開始可以先判斷1的數量有多少

```py
count1 = sum(arr)
```

1. 如果count1 = 0, 那可以直接返回`[0, n-1]`
2. 如果count1%3 != 0, 那代表肯定無法分配成三等份, 直接返回`[-1, -1]`
3. 再來我們可以先來決定right的部分
   1. `count1//3`就是right擁有的1的數量, 所以我們可以由後往前找出right
4. 再來就開始找left
   1. 先跳過leading zeros
   2. 再來用two pointers, 每當left[i] == right[j]那就i, j = i+1, j+1. 但如果left[i] != right[j], 那就代表無法找出合法的left, 返回[-1, -1]

     ```py
     XXXXXXXX ... XXXXXXXX
     i->          j->
     left         right
     ```
5. 等到我們有left和right後, 再來看middle是不是也相等即可
6. 最終就可以得到left, middle, right的頭尾index