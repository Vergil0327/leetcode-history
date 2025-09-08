# Intuition

palindrome

X -> mirror -> X X
XX -> mirror -> XX XX
XXX -> mirror -> XXX XXX
XXXX -> mirror -> XXXX XXXX

對於長度小於binary_string(n)的所有binary string, 必定滿足數值 <= n
所以我們就遍歷所有bit length, 然後看有多少合法palindrome

由於palindrome是前後翻轉構造而來, 只需關注前半段即可
總長度為1: [1,1] => 1
總長度為2: [1,1] => 11
總長度為3: [10,11] => 可構造出: 101, 111
總長度為4: [10,11] => 可構造出: 1001, 1111
總長度為5: [100,111] => 可構造出: 10001, 10101, 11011, 11111
總長度為6: [100,111] => 可構造出: 10001, 10101, 11011, 11111
所以總長度小於n.bit_length()的所有合法palindrome數有:
```py
res = 1 # for "0"
for i in range(1, L):
    half = (i+1)//2
    mn, mx = 1<<(half-1), (1<<half)-1
    res += mx-mn+1
```

再來考慮當長度恰好等於n.bit_length時的合法回文數
=> 用binary search去猜, 並且確認是否為`<= n`的合法解
```py
half = (L+1)//2
mn, mx = 1<<(half-1), (1<<half)-1
l, r = mn, mx
while l < r:
    mid = r - (r-l)//2
    palindrome = build(mid, L)
    if palindrome <= n:
        l = mid
    else:
        r = mid-1

palindrome = build(l, L)
if palindrome <= n:
    res += l - mn + 1
```