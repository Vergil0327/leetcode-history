# Intuition

- All strings in words will altogether be composed of no more than 16 unique lowercase letters.
- All strings in words are unique.

意思是最終可能的SCS, 每個字母的出現次數,只會在0到2次之間
All strings in words will altogether be composed of no more than 16 unique lowercase letters.
16個unique lowercase letters => 代表長度最多只有16, 2^16=65536, 這數字規模允許我們遍歷所有可能subset
所以如果我們可以高效檢查當前subset合不合法的話, 我們就可以用這個方法解決問題

核心概念:
遍歷所有可能SCS(O(2^16)), 再對每個SCS檢查合不合法
並且最後我們只看SCS裡的每個字符出現的frequency, 所以遍歷時也只需要在意每個字母的使用次數

而組成的方式:
1. 假如用"ab", "ba"來看, 可以接成"aba"跟"bab", 代表末位字符如果跟首位字符相同可以併組在一起
2. 那如果用"aa", "bb"來看, 就只能相連成"aabb"跟"bbaa"

從這兩種規則來看

"ab": a -> b
"ba": b -> a
"aa": a -> a
"bb": b -> b

每個words[i]其實表示兩個字符間有著edge, ex. words[i] = "ab", 代表節點"a" 有一個指向節點"b"的邊 ("a" -> "b")
整個可以看成graph problem

所以現在有個大致概念是, 我們的主要目的變成要找出如何遍歷所有能subset以及如何檢查該subset是合法subset, 也就是可以透過words來組成


那再回過頭討論SCS, 首先我們有這些字符(節點)可運用

```py
nodes = {x for word in words for x in word}
```

那每個節點可能出現**1次**或**2次**
那這邊我們目的是先遍歷所有可能為**出現2次**的字符及其可能組合

這代表我們當前subset裡,  `doubles`裡出現的字符都出現兩次
出現兩次可能是相連或是個別由兩個words[i]組成, 例如`"...aa..."`, 或是`"ax ... ya"`
那不管是哪種情況, 當遍歷到另外一個`doubles`裡出現的字符時, 都是合法組合

> ex. doubles = ("a", "b")
> 那代表SCS可能是"aabb"或"abba"或..., 不管如何, 都是可能的合法組合

那在知道所有出現兩次的字符後, 我們將與其相關字符的edges扣除掉後, 剩下的edge如果依舊能組成不含有cycle的graph的話
代表剩下的edge都沒出現double並且該組成也能透過扣除掉doubles相關的edges後組成合法graph, 亦即能組成合法字詞
因此這時就找到了合法Common Supersequence

由於我們length由小到大遍歷, 因此一但找到Common Supersequence, 長度必定最短, 必定是SCS
因此就可以不用再繼續往下遍歷possible subset了

```py
for length in range(len(nodes) + 1):
    valid_doubles = []
    for doubles in combinations(nodes, length):
        # ex. ("a", "b")
        graph = defaultdict(list)
        for word in words:
            u, v = word[0], word[1]
            if u not in doubles and v not in doubles:
                graph[u].append(v)
        if not has_cycle(graph):
            valid_doubles.append(doubles)
    if valid_doubles: break

NEW, VISITING, DONE = 0, 1, 2
def has_cycle(graph):
    color = defaultdict(int)
    def dfs(node):
        if color[node] != NEW:
            return color[node] == VISITING
        color[node] = VISITING
        if any(dfs(nei) for nei in graph[node]):
            return True
        color[node] = DONE
        return False

    return any(dfs(u) for u in graph)
```

那麼最終答案我們只需要將我們的SCS的frequency建構出來即可

```py
res = []
for doubles in valid_doubles:
    row = [0] * 26
    for x in nodes:
        row[ord(x)-ord("a")] = 1

    for y in doubles:
        row[ord(y)-ord("a")] = 2
    res.append(row)
return res
```