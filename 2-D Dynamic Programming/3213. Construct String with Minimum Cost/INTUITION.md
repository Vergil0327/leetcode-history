# Intuition

直覺想到的是我們遍歷target, 然後看words裡有沒有符合的
為了節省效率, 可以將words建構成trie, 這樣就能逐字符的搜索了

整體框架如下:
我們就用dfs來一個個字符搜尋, 每次對target[i:]利用trie進行搜索時, trie都是重新new一個出來即可

```py
Trie = lambda: defaultdict(Trie)
IS_END = "ISEND"
COST = "COST"

tri = Trie()
for word, cost in zip(words, costs):
    root = tri
    for ch in word:
        root = root[ch]
    root[IS_END] = True
    root[COST] = cost if COST not in root else min(root[COST], cost)

n = len(target)
dp = [-1] * n
def dfs(i):
    if i == n: return 0
    remainLen = n-i
    for word, cost in zip(words)
    if dp[i] == -1:
        dp[i] = inf
        root = tri
        for j in range(i, n):
            if target[j] not in root: break

            root = root[target[j]]
            if root[IS_END]:
                dp[i] = min(dp[i], dfs(j+1) + root[COST])
    return dp[i]

res = dfs(0)
return res if res < inf else -1
```

但這樣實質上是O(n^2), 會TLE在這類型的case: target="aaa...", words=["a", "aa", "aaaa", "aaaaaa", ...]

會發現"a", "aa", "aaaa", 這些選擇會讓整個dfs搜索的分支變得相當多

要進一步優化的話
隨著我們陸續處理完target[:i], 剩餘的target[i+1:]部分照理說會淘汰掉長度大於**n-(i+1)**的words[j]

所以我們`zip(words, cost)`可以照長度排序, 這樣在遍歷可能選項時, 一但長度超出需就, 我們即可直接break

所以我們可以先將相同長度的 (words[i], cost[i]) 放在一起

```py
maxLen = max(len(word) for word in words)

# length2wordCost = {length: {word: cost}}
length2wordCost = [defaultdict(lambda: inf) for _ in range(maxLen+1)]
for word, cost in zip(words, costs):
    length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)
```

並找出存在的所有可能words[i]長度:

```py
lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]
```

那再來就一樣透過top-down dp (dfs + cache)來搜索即可
而且這次不再需要Trie, 我們用prune branches的方式直接利用dp搜索即可

```py
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        maxLen = max(len(word) for word in words)

        # length2wordCost = {length: {word: cost}}
        length2wordCost = [defaultdict(lambda: inf) for _ in range(maxLen+1)]
        for word, cost in zip(words, costs):
            length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)

        lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]

        n = len(target)

        dp = [-1] * n
        def dfs(i):
            if i == n: return 0
            if dp[i] != -1: return dp[i]

            dp[i] = inf
            for length in lengths:
                if i + length > n: break

                cost = length2wordCost[length][target[i:i+length]]
                if cost < inf: # target[i:i+length] exists in words
                    dp[i] = min(dp[i], dfs(i+length) + cost)
            return dp[i]
        ans = dfs(0)
        return ans if ans < inf else -1
```

由於top-down方式會 Memory Limit Exceeded (713 / 807 testcases passed)
我們改成bottom up的形式

```py
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        maxLen = max(len(word) for word in words)

        # length2wordCost = {length: {word: cost}}
        length2wordCost = [defaultdict(lambda: inf) for _ in range(maxLen+1)]
        for word, cost in zip(words, costs):
            length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)

        lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]

        n = len(target)

        dp = [inf] * (n+1)
        dp[0] = 0

        for i in range(n):
            for length in lengths:
                if i+length > n: break

                cost = length2wordCost[length][target[i:i+length]]
                if cost < inf:
                    dp[i+length] = min(dp[i+length], dp[i] + cost)

        return dp[n] if dp[n] < inf else -1
```

結果最後還是會MLE + TLE.......

覺得這題很沒必要, 應當Trie + DFS即可

最後試著以下幾個minor optimization:

1. 不使用defaultdict(lambda: inf) for length2wordCost, 用省記憶體的dict()
   - 因此後續更新dp[i+length]時, 必須提前判斷`if target[i:i+length] in length2wordCost` 
    
2. 用variable `word` 儲存string slicing `target[i:i+length]`這項結果, 加快處理速度

最終以**12898 ms Beats 25.12%**成績通過

```py
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        maxLen = max(len(word) for word in words)

        # length2wordCost = {length: {word: cost}}
        length2wordCost = [{} for _ in range(maxLen+1)]
        for word, cost in zip(words, costs):
            if word not in length2wordCost[len(word)]:
                length2wordCost[len(word)][word] = cost
            else:
                length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)

        lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]

        n = len(target)

        dp = [inf] * (n+1)
        dp[0] = 0

        for i in range(n):
            for length in lengths:
                if i+length > n: break
                
                word = target[i:i+length]
                if word in length2wordCost[length]:
                    cost = length2wordCost[length][word]
                    if dp[i+length] > dp[i] + cost:
                        dp[i+length] = dp[i] + cost
          
        return dp[n] if dp[n] < inf else -1
```