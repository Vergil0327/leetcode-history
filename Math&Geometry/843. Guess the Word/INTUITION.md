# Intuition

```python
matches = master.guess(word)
```

- if `matches` == 6, it means we found it
- if `matches` != 6, we narrow possible candidates by it

**How to narrow results ?**

since secret word has exact match with current word with exact `matches` characters,
the possible candidates are those also has exact `matches` characters with current word.

if `matches` is 4, it means 4 characters are correct and 2 characters are wrong.

if there is a word compared with current word with *more* or *less* matches, it can't be secret word because it must exist one wrong character at least.

therefore, because secret word has exactly `x` matches with word, we can just search in the candidates, and only keep the ones that have exact `x` matches with word.

**Why choose guess word randomly?**

to avoid artificial worst case.

if we always choose first item to guess, maybe there is a worst case that all the worst candidates are in the begining

# Complexity

- time complexity
O($n^2$)

- space complexity
$$O(n)$$