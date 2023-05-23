# Intuition

since palindrome is symmeric, consider first half only for
even:
    n = intLength//2
    100 -> 100001
    101 -> 101101
    102 -> 102201
    ...
    999 -> 999999

    XXX -> XXX + XXX

odd: 
    n = intLength//2+1
    100 -> 10001
    101 -> 10101
    102 -> 10201
    ...
    999 -> 99999
    
    XXY -> XXYXX

the problem to find k-th palindrome becomes finding k-th largest positive number
and we can see that if n = 3, total number of valid palinedrome is `100~999 = 900`,
that is `9 * 10**(n-1)`.

thus, if `queries[i] > 9*10**(n-1)`, there is no valid answer for queries[i]

then:

- intLength%2 = odd
  - first_half = 10**(n-1) + (queries[i]-1)
  - second_half = flip(first_half)
  - palindrome = first_half * 10^n + second_half

- intLength%2 = even
  - first_half = 10**(n-1) + (queries[i]-1) # including center -> first_half = XXXXY, we need to flip XXXX only
  - second_half = flip(first_half//10)
  - palindrome = first_half * 10^(n-1) + second_half


# Other Solution

我們可看到我們會需要翻轉first_half
比起用數學計算翻轉, 我們轉成string來處理會更加方便

前面同樣是:
- isEven = intLength%2 == 0
- n = intLength//2 if isEven else intLength//2+1
  - ex. intLength = 3, [XX]X
  - ex. intLength = 4, [XX]XX
- limit = 9 * 10**(n-1)
  - 10...0 ~ 99...9
  - if queries[i] > limit: res.append(-1)

後面我們可知
```py
first_half = str(10**(n-1) + (queries[i]-1))
second_half = first_half[::-1][intLength%2:]
```