# Intuition

```
X X [X X X X X X]
     j         i
```
我們要找一段最長的subarray使得母音個數是偶數
所以對於任意一段subarray, nums[j:i], 我們希望vowels of s[j:i] - vowels of s[:j-1] = even number

所以我們只需關心母音個數對2的餘數即可
如果到nums[:i]為止的母音個數對2取餘是 `(a%2,e%2,i%2,o%2,u%2)`
如果我們在先前找到一段也是`(a%2,e%2,i%2,o%2,u%2)`的prefix array
那麼兩者個數相減就會是一段母音個數為偶數的subrray

所以我們可以用個hashmap `vowels`, 以`(a%2,e%2,i%2,o%2,u%2)`作為key來紀錄index

ex.
vowels[(a%2,e%2,i%2,o%2,u%2)] = i
vowels[(a'%2,e'%2,i'%2,o'%2,u'%2)] = j-1

那麼兩個index相減即為我們要的subarray長度

*note. 我們也可以用bitmask作為hashmap的key*
