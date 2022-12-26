# Intuition

simulate process from base case: `n=1 s="1"`

```
 n = 1,  s = "1"
 n = 2,  s = "11"
 n = 3,  s = "21"
 n = 4,  s = "1211"
 n = 5,  s = "111221"
 n = 6,  s = "312211"
 n = 7,  s = "13112221"
 n = 8,  s = "1113213211"
 n = 9,  s = "31131211131221"
 n = 10, s = "13211311123113112211"
```

每次由左往右把`s`分成若干個substring，每個substring是一串字符相等的連續字串

```
ex.
n = 5時，將n=5的s分成["1","2","11"]
n = 6時，將n=4的s分成["111","22","1"]
```

然後計算每個substring的長度，或者說是每個字符出現的頻率，組成pairs

```
ex.
n = 5時，pairs=[["1", 1],["2", 1],["1", 2]]
n = 6時，將n=5的s分成[["1", 3],["2", 2],["1", 1]]
```

然後再依序把frequency與字符組回成字串即可

# Complexity

- time complexity:

O($n^2$)

- space complexity

$$O(n)$$