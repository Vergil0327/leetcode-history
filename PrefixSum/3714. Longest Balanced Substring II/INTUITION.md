# Intuition

覺得這題是個非常好的題目, 只要理解prefix + hashmap去求得subarray中字母數目的概念就能解

一開始想到三種可能:
1. all-equal characters: a*k, b*k or c*k
這簡單, 沒什麼好說, 遍歷一遍找連續相同字母subarray即可

2. exactly two distinct characters: (a+b)*k
`exactly`不能透過sliding window + hashmap
這邊直接用prefix sum + hashmap

首先拆分出三種可能: (a,b), (b,c), (a,c)
以(a,b)為例, 如果要找一段subarray, 數目上是a == b, 那麼我們只要找到prefix sum中的兩個位置, 那麼(a-b)的差值是一樣的地方即可
假設`i`, `j`分別是兩個key = (# of a - # of b)的位置, 由於差值相同, 那麼這段subarray就正好會是a, b兩者數目相等的subarray
但由於我們還必須滿足`c`的數目必須是**0**, 因為當前case已設定只會有2個distinct number

所以我們的key還得加入c的數目, 改為(# of a - # of b, # of c)
這樣兩段prefix sum扣除後的subarray, c的數目就會是0

```py
# distinct 2
# three possible combination: (a,b), (b,c), (a,c)
ans2 = 0
positionAB = {}
positionAC = {}
positionBC = {}
for i in range(n+1):
    keyAB = (presumA[i] - presumB[i], presumC[i])
    if keyAB in positionAB:
        j = positionAB[keyAB]
        ans2 = max(ans2, i-j)
    if keyAB not in positionAB:
        positionAB[keyAB] = i
    
    keyAC = (presumA[i] - presumC[i], presumB[i])
    if keyAC in positionAC:
        j = positionAC[keyAC]
        ans2 = max(ans2, i-j)
    if keyAC not in positionAC:
        positionAC[keyAC] = i
    
    keyBC = (presumB[i] - presumC[i], presumA[i])
    if keyBC in positionBC:
        j = positionBC[keyBC]
        ans2 = max(ans2, i-j)
    if keyBC not in positionBC:
        positionBC[keyBC] = i
```


3. all three characters present.: (a+b+c)*k

一開始想到number of third characters = current length - # of a - # of b, 但感覺沒麼用

但其實這個case是上個case的延伸, 我們要找的其實就是b跟c兩者跟a的差值作為key的位置, 一但發現兩個相同key的位置, 那麼這段subarray就代表著b,c兩者跟a的差值都會是0

presum + hashmap: 定義key = (count_b - count_a, count_c - count_a)
假設發現兩次`key = (b跟a差x個, c跟a差y個)`, 那麼這兩個位置`i`, `j`的prefix sum差值互相扣掉後, nums[i:j]就會是a,b,c三者相同長度的合法subarray
由於要找的是最長subarray, 所以hashmap要記得是**第一個發現的位置**

```
ex. A B {A A B C B C}
         j         i
```