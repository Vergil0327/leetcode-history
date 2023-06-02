# Intuition

see example 1:
```
pressedKeys = "22233"
1st pressed:
a

2nd pressed:
aa
b

3rd pressed:
aaa
ba
ab
c

4th pressed:
aaad
bad
abd
cd

5th pressed:
aaadd
aaae
badd
bae
abdd
abde
cdd
ce
```

generally speaking:

define dp[i]: the total number of possible text messages considering s[:i]

```

X X X X X X X X X X X [X]
X X X X X X X X X X [X X]
                     j
X X X X X X X X X [X X X]
                   j   i -> if s[i] == s[j], we can combine s[j:i] into one character, then dp[i] += dp[j-1]
```

1. after appending s[i], we can transfer state from dp[i-1] to dp[i]. this is base case we can get.
   - that is, `dp[i] += dp[i-1] `
2. if pressedKeys[i] == pressedKeys[j] where j-character_options <= j < i, we can trasfer state from dp[j-1] to dp[i]
   - thus, `dp[i] += dp[j-1] if s[j:i] can transfer to valid character`

thus, we can build each keycap's valid length first

```py
# pressed key: maximum number of characters/state.
length = {"2":3, "3":3, "4":3, "5":3, "6":3, "7":4, "8":3, "9":4}
```

only if length of s[j:i] is within length[s[i]], the s[j:i] is valid character
then based on analysis above, we can get our state transfer fn
```py
# after append[i]:
dp[i] += dp[i-1]

if s[i] == s[i-1]: # traverse backwards and update dp[i] if s[j:i] can transfer into valid character
    # dp[i] += dp[j-1] if s[j:i] is valid
    l = length.get(s[i], 0)
    for j in range(i-1, max(0, i-l), -1):
        if s[i] == s[j]:
            dp[i] += dp[j-1]
        else:
            break
```


