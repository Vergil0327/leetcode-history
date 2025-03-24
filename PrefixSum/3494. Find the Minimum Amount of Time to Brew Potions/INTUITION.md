# Intuition

這題講的是每個魔法師依序調劑藥品
**一但完成**, 必須馬上交給下個人, 一路交下去

第一輪肯定沒問題
但如果第二輪的開始時間太早, 有可能交到後面會有魔法師還在調上一輪藥品

所以我們維護每個魔法師當輪的最終完成時間`finish_t`, 其中`finish_t[i]`代表第i為魔法師在輪會在`finish_t[i]`時間完成

所以我們對於第j輪藥劑, 我們可以基於上次的結束時間, 計算出當輪次至少需要多少時間, 定義為`require_t`

所以對於當輪藥劑`j`
第i位魔法師, 他最終完成時間為第i到n-1位法師的處理時間加總: finish_t[i] + (skill[i] + skill[i+1] + ... + skill[n-1]) * mana[j]

那整體取最大值就能得出該藥劑完成的最快時間`require_t`

```py
n, m = len(skill), len(mana)

finish_t = [0] * n
for j in range(m):
    require_t = 0
    for i in range(n):
        next_finish_t = finish_t[i] + sum(skill[j] for j in range(i, n)) * mana[j]
        require_t = max(require_t, next_finish_t)

    # ...
```

那既然得出了最終時間`require_t`, 我們在反過頭來更新每個魔法師的finish_t[i]即可

```py
for j in range(m):
    # ....

    finish_t[n-1] = max(finish_t[n-1], require_t)
    for i in range(n-2, -1, -1):
        finish_t[i] = finish_t[i+1] - skill[i+1] * mana[j]
```

那最終整體框架為:

```py
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        presum_skill = list(accumulate(skill, initial=0))

        finish_t = [0] * n
        for j in range(m):
            require_t = 0
            for i in range(n):
                next_finish_t = finish_t[i] + sum(skill[j] for j in range(i, n)) * mana[j]
                require_t = max(require_t, next_finish_t)
            
            finish_t[-1] = max(finish_t[-1], require_t)
            for i in range(n-2, -1, -1):
                finish_t[i] = finish_t[i+1] - skill[i+1] * mana[j]

        return finish_t[-1]
```

但這樣會是O(m*n^2), 很明顯裡面的`sum(skill[j] for j in range(i, n))`可以透過prefix sum優化

所以最終O(m*n)版本為:

```py
def minTime(self, skill: List[int], mana: List[int]) -> int:
    n, m = len(skill), len(mana)
    presum_skill = list(accumulate(skill, initial=0))

    finish_t = [0] * n
    for j in range(m):
        require_t = 0
        for i in range(n):
            next_finish_t = finish_t[i] + (presum_skill[n]-presum_skill[i]) * mana[j]
            require_t = max(require_t, next_finish_t)
        
        finish_t[-1] = max(finish_t[-1], require_t)
        for i in range(n-2, -1, -1):
            finish_t[i] = finish_t[i+1] - skill[i+1] * mana[j]

    return finish_t[-1]
```

### Complexity

time: O(n*m)
space: O(n)