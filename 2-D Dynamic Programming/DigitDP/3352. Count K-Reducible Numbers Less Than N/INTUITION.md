# Intuition

```
1
11 -> 1
111 -> 11 -> 10 -> 1
1111 -> 10 -> 1
11111 -> 101 -> 10 -> 1
111111 -> 110 -> 10 -> 1
1111111 -> 111 -> 11 -> 10 -> 1
```

一開始毫無思緒, 先試著觀察出pattern
從上可大概有個感覺能推出關係式, 然後預先計算出每個數所需的reduce steps:

定義reduce_step[i]: required steps for number `i` to be reduced to 1

ex. "001", "010", "100" => one step => "1"
"011", "101", "110" => 2 (= "10") => 1

狀態轉移: reduce_step[num] = [num's setBits] + 1

```py
reduce_step = [0] * 801 # `s.length <= 800` => 800 1-bit at most
reduce_step[1] = 0
for i in range(2, 801):
    reduce_step[i] = reduce_step[i.bit_count()] + 1
```

再來只要能找出所有合法string, 便能總和出答案 => digit DP

- 如果當前`s[i] == 0`:
  - 如果當前組的字串已經小於`s`, 那當前i-th position就可以放`0`或`1`
  - 如果當前字串沒有小於`s`, 那當前i-th position只能放`0`
- 如果當前`s[i] == 1`:
  - 如果當前組的字串已經小於`s`, 那當前i-th position就可以放`0`或`1`
  - 如果當前沒有小於`s`, 那i-th postition能放`0`或`1`

而這其實就改一下digit dp的框架即可, 同時為了計算所需操作次數, 我們還得紀錄當前有多少個1-bit:

```py
def dfs(i, setBits, smallerThanS):
    end = 2 if smallerThanS else int(s[i])+1
    res = 0
    for d in range(0, end):
        res += dfs(i+1, setBits + int(d == 1), smallerThanS or d < int(s[i]))
    
    return res% 1_000_000_007
```

base case:

```py
if i == len(s):
    # 當前組出來的字串, 其所需操作數為: reduce_step[s'] = reduce_step[setBits] + 1
    if setBits > 0 and reduce_step[setBits]+1 <= k and smallerThanS:
        return 1
    return 0
```