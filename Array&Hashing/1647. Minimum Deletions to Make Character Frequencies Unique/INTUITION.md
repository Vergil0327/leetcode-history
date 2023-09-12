# Intuition

first, collect all the frequencies

F1, F2, F3, F4, ...

for any duplicate frequency, we need to decrement until no duplicate
since frequency only `n` at most, if we iterate empty frequency `i` from 1 to n and iterate frequency we have `f` from lowest to highest, which means two pointers.

also use a hashset `seen` to check if we have duplicate frequency.

iterate f and keep adding f into a hashset `seen` and keep moving `i` to collect all the available frequencies.

we can use **monotonically increasing stack**:

once i < f, all freq within [i:f-1] are available unseen frequency, then set i to next unseen min freq, `f+1`
```py
if f not in seen:
    seen.add(f)
    while i < f:
        stack.append(i)
        i += 1

    # update i to f+1, next unused freqency
    i = f+1
```

once f in seen, we found duplicate and we want `f` to become some unseen frequency with min_steps.
we can make f become stack.pop() or 0 if stack is empty.
then `res += f - (stack.pop() if stack else 0)`