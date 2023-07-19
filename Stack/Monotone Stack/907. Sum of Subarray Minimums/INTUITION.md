# Intuition
```
   X        [X X X  {X]  X X}    X
prevSmaller          i       nextSmaller
```

我們可以查看每個arr[i]能貢獻多少subarray
=> 如果我們能知道 prevSmaller[arr[i]]=x, nextSmaller[arr[i]]=y
=> 這代表左邊界有(i-x)種選擇, 右邊界有(y-i)種選擇 => 所以總共有(i-x)*(y-i)個subarray的最小值是arr[i]

如果arr=[3,1,2,2,2,2,4], 如果有相同數, 為了避免重複計算
arr[i]必須只參與其中一邊, prevSmaller或nextSmaller
ex. 
[3,1,2,2,2,2,4], n = 7
     i -> prevSmaller = 1, nextSmaller = n (i=2, [2,2,2,2,4])
       i -> prevSmaller = 2, nextSmaller = n (i=3, [2,2,2,4])
         i -> prevSmaller = 3, nextSmaller = n (i=4, [2,2,4])
           i -> prevSmaller = 4, nextSmaller = n (i=5, [2,4])
相當於arr[i]=2固定為subarray的最左, 然後看他貢獻多少subarray

```py
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prevSmaller = [-1]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        nextSmaller = [n]*n
        stack.clear()
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                nextSmaller[stack.pop()] = i
            stack.append(i)
            
        res = 0
        M = 10**9+7
        for i in range(n):
            left = i-prevSmaller[i]
            right = nextSmaller[i]-i
            contrib = arr[i] * (left*right)
            
            res = (res + contrib) % M

        return res
```