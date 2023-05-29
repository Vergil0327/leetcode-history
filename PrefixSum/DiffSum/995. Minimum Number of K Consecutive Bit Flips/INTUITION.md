# Intuition

以下兩種情況:
```
X X X X 0 ...
        i

X X X X 1 ...
        i
```

為了得到最少操作數
1. 當第`i`個數是1時, 我們不必動它
2. 但當第`i`個數是0時, 我們肯定得翻他, 翻了之後, 後面`k-1`個數也會跟著翻動

再來在看, 如果當nums[i]是1時, 且翻動的次數為奇數
那麼nums[i]實際上會是`0`

所以上面情況1得改為 `(nums[i]+flips)%2 == 0` 時, 我們就得翻動
```
X X X X 1 ...
        i and flips = 1
```

那這邊由於翻動的是一個subarray, 這邊很明顯提示我們可以用個差分數組`difference array`來標記我們的翻動次數

由於最後`nums[n-k+1:]`這段不能進行翻動, 所以我們分開成兩段來看
- nums[n-k+1:]這段只能檢查
  - 一但`(nums[i]+diff[i])%2 == 0`, 那麼就沒救了, 只能返回-1
- nums[0:n-k]這段可以任意翻動
  - 一但(nums[i]+diff[i])%2 == 0, 那麼就標記我們翻動的區間
    - diff[i] += 1, diff[i+k] -= 1, res += 1

有了以上思緒後, 就只要記得在遍歷過程中:
- 查看`(nums[i]+diff[i])%2`
- 以及更新diff[i]即可

整體框架為
```py
# [0:n-k] 可翻動
for i in range(n-k+1):
    diff[i] += diff[i-1] # 更新 diff[i]

    if (nums[i]+diff[i])%2 == 0:
        diff[i] += 1
        diff[i+k] -= 1
        res += 1

# [n-k+1:n-1]不可翻動
for i in range(n-k+1, n):
    diff[i] += diff[i-1]

    if (nums[i]+diff[i])%2 == 0:
        return -1
```