# Intuition

詳細影片解析參考: [@HuifengGuan](https://www.youtube.com/watch?v=7VDPEki9qX4&ab_channel=HuifengGuan)

s = X X X X X X X X {A B C D i}

我們看"ABCDi"這段
A
AB = A*10 + B
ABC = A*100 + B*10 + C
ABCD = A*1000 + B*100 + C*10 + D
ABCDi = A*10000 + B*1000 + C*100 + D*10 + i

如果`ABCDi % d = r`, 那麼如何知道`i`是不是能被d整除?
由於`i = ABCDi - ABCD0`
所以如果`ABCD0 % d = r`這條件也符合時, 因為"ABCDi"跟"ABCD0"同餘, 所以代表`i`能被`d`整除

那如果要看"Di"能不能被`d`整除呢?
就同理, 看`ABC00 % d = r`這條件有沒有成立

所以如果我們能知道`A0000`, `AB000`, `ABC00`, `ABCD0`的個數, 那麼就能知道多少`BCDi`, `CDi`, `Di`, `i`能被`d`整除

也就是知道餘數`r`的個數有多少個, 例如`x`個, `count[r] = x`
那麼當前餘數為`r`的所有substring後面再多補一個"0"時, 再除`d`所得到的餘數個數就能更新成: `count_new[r*10 % d] += count[r] for r in range(d)`

s = "ABCDi"
round1: "A", count[A%d] = r, 求出"A"對各種`d`時餘數的個數
round2: "AB", 會再繼續求出count[A*10 % d], count[B%d]. 那這時就能知道對於"AB" substring, 過往的"A0"是否同餘, 以及"AB"對於digit `d`是否餘數為0

核心概念就像是用prefix sum + hashmap來考量餘數來找出有多少合法substring
ex. nums = "123 | 456", 如果"123456"餘數為`r`, "123000"餘數也為`r`, 那麼"456"就能被該digit整除

# Approach

First, let's understand what the code is doing at a high level:

1. The solution iterates through each possible last digit (1-9)
2. For each last digit, it finds all substrings ending with that digit that are divisible by it
3. The final result is the sum of all valid substrings found

```py
def count(nums: List[int], digit: int) -> int:
    """
    This helper function counts substrings that:

    - End with the specified digit
    - Are divisible by that digit
    
    Parameters:
    - nums: The input string converted to a list of integers
    - digit: The last digit we're currently checking (1-9)
    """
```

```py
count = [0] * digit
count_new = [0] * digit
```

These arrays track remainders when dividing by the current digit:

- count[r] stores how many ways we can get remainder r using previous digits
- count_new is used to calculate the next state
- Length is digit because when dividing by d, remainders can only be 0 to d-1

```py
count[0] = 1  # base case

# Initialize with one way to get remainder 0 (empty string)
```

```py
for r in range(digit):
    count_new[r*10 % digit] += count[r]
```

This is a key part that handles the transition when adding a new digit:

- For each existing remainder r
- Multiply by 10 (shifting left)
- Take modulo with current digit
- Add to the count of the new remainder

```py
if nums[i] == d:
    res += count[remainder]
```

If current digit matches the target last digit:

- Add count of all ways to reach current remainder
- These represent valid substrings ending at current position

```py
count[remainder] += 1
```

Add current prefix as a new way to reach this remainder

Finally, in the main function:

```py
nums = [int(d) for d in s]
res = 0
for d in range(1, 10):
    res += count(nums, d)
return res
```

- Convert string to integers
- Sum results for all possible last digits (1-9)
- Return total count

# Complexity

time: O(n)

The solution uses dynamic programming with remainder tracking to efficiently count valid substrings. The time complexity is O(n * 9 * 9) = O(n), where n is the string length, because:

- Outer loop runs 9 times (digits 1-9)
- Inner loop processes each character once
- Remainder transitions take constant time (max 9 operations)

space: O(1)

Space complexity is O(1) as the count arrays are bounded by the maximum digit (9).