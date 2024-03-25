# Intuition

maximum XOR => 首先想到的是跟Trie做連結
類似題目: 1707. Maximum XOR With an Element From Array, 2935. Maximum Strong Pair XOR II

對於[node, val] = queries[i]來說, 如果我們有從root到node的Trie的話, 其中Trie紀錄各自節點的XOR value
那這樣對於val來說, 我們就能透過Trie找出當前的maximum XOR

ex. val = 10001110
由於1 XOR 0 = 1, 0 XOR 1 = 1, 想要最大XOR, 就代表要盡可能找互補的bit
所以我們就在trie裡, 一層層的找1-(val>>i)&1, 如果沒有, 再去(val>>i)&1

val <= 2 * 20^5 <= 110000110101000000 (二進制) => Trie 最多就18層

有了這想法後, 再來就是如何在遍歷queries過程中能同時高效利用trie來搜索 maximum XOR value 了
由於有限定路徑, 對於queries[i].val來說, 我們只能從root -> queries[i].node這段路徑所建構的Tries中, 搜索該路徑節點所貢獻的bit並找出最大值

因此, 我們應該要從根節點開始往下遍歷, 並且透過backtracking去建構Trie
然後在遍歷過程中查看該節點有沒有出現在queries[i]裡, 有的話當前的Trie會是root -> node這段路徑所構成
我們能直接透過Tries去找出該quries的maximum XOR

其實這題跟2935. Maximum Strong Pair XOR II相當類似, 就差在是透過DFS去對tries進行建構

整體框架如下

```py
graph = defaultdict(list)
root = -1
for node, p in enumerate(parents):
    if p == -1:
        root = node
        continue
    graph[p].append(node)

max_bit_length = ceil(log2(2 * 10**5)) # 0 <= queries[i].val <= 2 * 10^5
tri = Trie(max_bit_length)

res = [0]*len(queries)

query2idx = defaultdict(set)
for i, (node, val) in enumerate(queries):
    query2idx[node].add(i)

def dfs(node):
    tri.add(node)
    if node in query2idx:
        for idx in query2idx[node]:
            res[idx] = tri.findMaxXOR(queries[idx][1])

    for children in graph[node]:
        dfs(children)

    tri.delete(node)

dfs(root)
return res
```

time complexity: O(n log(18))

### Tries Implementation


```py
class TrieNode:
    def __init__(self):
        self.next = dict()
        self.val = 0

class Trie:
    def __init__(self, n):
        self.n = n
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        for i in range(self.n, -1, -1):
            val = (num>>i)&1
            if val not in node.next:
                node.next[val] = TrieNode()
            
            node = node.next[val]
        node.val = num

    def findMaxXOR(self, val):
        cur = self.root
        for i in range(self.n, -1, -1):
            bit = (val>>i)&1
            cur = cur.next[1-bit] if 1-bit in cur.next else cur.next[bit]
        return val^cur.val
    
    def delete(self, num):
        bits = []
        for i in range(self.n, -1, -1):
            bit = (num>>i)&1
            bits.append(bit)
        return self._delete(num, bits, 0, self.root)
    
    def _delete(self, num, encodes, i, current):
        if i == self.n+1:
            if current.val != num: return False
            current.val = 0
            return len(current.next) == 0
        
        b = encodes[i]
        if b not in current.next: return False

        next_node = current.next[b]

        need_del = self._delete(num, encodes, i+1, next_node)
        if need_del:
            del current.next[b]
            return len(current.next) == 0
        return False
```