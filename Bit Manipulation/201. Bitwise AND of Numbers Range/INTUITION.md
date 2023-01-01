# Intuition

actually, what we need to find is common prefix in binary format

ex. `26` to `30`
```
Their binary form are:
11010
11011
11100　　
11101　　
11110
```

we just keep shifting `left` & `right` to right until we found common prefix in binary format. also, we need to record how many bit position we shift

once we found common prefix, we shift common prefix back

# Optimized Solution

[here](https://leetcode.com/problems/bitwise-and-of-numbers-range/solutions/593317/simple-3-line-java-solution-faster-than-100/?orderBy=most_votes)

```
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right-1)

        # just return right directly because while-loop already execute right&=left
        return right
```