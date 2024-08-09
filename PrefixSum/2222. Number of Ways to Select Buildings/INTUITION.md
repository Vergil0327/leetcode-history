# Intuition

Return the number of valid ways to select 3 buildings.
- 當中間為"1", 唯一合法可能為"010"
- 當中間為"0", 唯一合法可能為"101"

所以我們就遍歷中間s[i], 然後看對於`s[i]`來說, 左右prefix, suffix有多少個1或0, 相乘即為合法pattern數目

time: O(n)
space: O(n)

# Optimized

只有兩種pattern: "010", "101"
所以拆開來看:

1. "010": 對於右邊的"0"來說, 他可以跟前面prefix的"01"組成合法pattern, 貢獻的合法pattern數目為pattern的數目
2. "101": 對於右邊的"1"來說, 他可以跟前面prefix的"10"組成合法pattern, 貢獻的合法pattern數目為pattern的數目

所以我們持續遍歷s[i]並更新紀錄過往的"01", "10" pattern在`zeroones`, `onezeros`即可

```py
def numberOfWays(self, s: str) -> int:
    zeros = ones = onezeros = zeroones = 0
    result = 0
    for char in s:
        if char == '0':
            zeros += 1
            onezeros += ones
            result += zeroones # 右端點為char "0", 左邊有zeroones個"01" pattern
        else:
            ones += 1
            zeroones += zeros
            result += onezeros # 右端點為char "1", 左邊有onezeros個"10" pattern
    return result
```


time: O(n)
space: O(1)