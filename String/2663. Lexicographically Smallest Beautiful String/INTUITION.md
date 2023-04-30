# Intuition

since we want `the lexicographically smallest string of length n, which is larger than s and is beautiful`, it's intuitively to check `n-1` character first.

first, we iterate backwards from `i=n-1` to `i=0` and increment `s[i]` lexicographically.
after increment `s[i]` within valid range (first k English characters), we check current `s[i]'` is beautiful or not by helper function `checkBautiful`:

since `s` is already beautiful string initially, we only need to check `i-1` and `i-2` position if there exists:
- AA palindrome
- AXA palindrome

> we only need to check palindrome whose length is 2 or 3, because if none of these two exists, we won't get longer palindrome.

```py
def checkBautiful(arr, i):
    if i-1 >= 0 and arr[i-1] == arr[i]: # check AA palindrome
        return False
    if i-2 >= 0 and arr[i-2] == arr[i]: # check AXA palindrome
        return False
    return True
```

```py
for i in range(n-1, -1, -1):
    for ch in range(arr[i]+1, ord("a")+k):
        arr[i] = ch
        if checkBautiful(arr, i):
            # continue to construct lexicographically smallest beautiful string

return "" # we can't construct larger beautiful string
```

once we found valid character to make `s` larger and beautiful by replacing `s[i]`, we start to deal with `s[i+1:n]` since we need **lexicographically smallest** string.

we just reuse same checking logic to check from `i+1` to `n-1`.

since we want **lexicographically smallest**, let's replace each s[k] from "a" first where `i+1 <= k < n` and we only need "a", "b" and "c" as replacement for constructing **lexicographically smallest** beautiful string.

```
s = X X X X X X X X X {X X X X}
                    i  k -> n-1

replace s[k:n-1] with:
a if "a" is valid
a b
a b c
a b c a 
a b c a b

b if "a" is invalid. ex. s[i] = "a"
b c
b c a 
b c a b

c if both "a" and "b" are invalid. ex. s[i-1] = "a" and s[i] = "b" and we only can use "c" for s[k]
c a 
c a b
```

```py
if bautiful:
    k = i+1
    
    while k < n:
        mod = 0
        arr[k] = ord("a")+mod
        while not checkBautiful(arr, k):
            mod = (mod+1)%3
            arr[k] = ord("a")+mod

        k += 1
```

# Complexity

- time complexity

$$O(k*n^2)$$ but we won't get $O(n^2)$ because of "beautiful" constraint.

- space complexity

$$O(n)$$