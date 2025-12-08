# Intuition

一開始想到雙指針(sliding window), 但仔細看這case:

```
hp = 20
damage = [1, 1, 1]
requirement = [20, 1, 1]
```

雙指針並不能給我們正確答案, 根據提示, 這題正解其實是:

1. Go from the last room to the first.
2. At each room i, calculate score(i).

Math
To get a point at room j sarting from room i:
hp - (damage from i to j) >= requirement[j]

Let's rearrange this:
hp + (damage from j + 1 to n) - (damage from i to n) >= requirement[j]

So that
hp + (damage from j + 1 to n) - requirement[j] >= (damage from i to n)

We iterate backward,

- sorted list `sl` stores the left side of the inequality.
- variable `total` stores the right side.

For each room i:

Add the value for k = i into sl.
Update total to be the damage from i to n.
Count how many items in sl are >= total.
This count equals score(i).
Add this score to the final result res