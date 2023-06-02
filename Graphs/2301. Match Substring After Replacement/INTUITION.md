# Intuition

since what we want is a substring equal to `sub`, we can find all possible target first.

```py
targets = set()
n = len(sub)
for i in range(len(s)-n+1):
    t = s[i:i+n]
    targets.add(t)
```

Furthermore, `mapping` tell us how to change character, we can think this to be a graph problem and the `[oldi, newi] = mapping[i]` is a directed edge from **oldi** to **newi**

then, we just compare `sub` with every possible target `t`.

```py
for t in targets:
    # prune same characters
    i = 0
    while i < n and sub[i] == t[i]:
        i += 1
    
    if compare(sub[i:], t[i:]): return True
return False
```

and the helper function `compare` is just a simple dfs to compare character by character

**Optimization**

if sub[:i] already equals to t[:i], we can first i characters and just compare s[i:] with t[i:]

```py
for t in targets:
    # prune same characters
    i = 0
    while i < n and sub[i] == t[i]:
        i += 1
```