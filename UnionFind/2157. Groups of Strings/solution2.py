# words[i]可以透過三種操作跟這些可能字詞連接在一起
# set(words[i]) replace words[i][j] with a-z
# set(words[i]) add a-z to j-th position
# set(words[i]) delete any j-th character

# 透過union-find能知道有多少個group以及最大group size
# 重點還是如何高效判斷words[i], words[j]是connect在一起的

# 那麼每個words[i]就相當於是個節點, 透過三種操作找出可能words[j]
# 然後union(words[i], words[j])
# 最終找出connected componenet的個數以及最大size即可

# > 根據constraint: No letter occurs more than once in words[i].
# 由於每個字母只會出現一次, 比起直接compare(words[i], words[j])
# 我們可以將words[i]轉為bitmask, 用長度26的二進制編碼紀錄哪些位置

# 然後透過三種操作找出words[j]
# 然後compare(encode(words[i]), encode(words[j]))

# 首先是`replace`操作
# 對於當前的index=i, words[i] = bit來說

# 我們可以找出我們有哪些字符, 把他替換成我們沒有的字符: O(26*26)
# ```py
# for b in range(26):
#     if (bit>>b)&1: # replace existed one with character we don't have
#         for k in range(26):
#             if (bit>>k)&1: continue

#             new_bit = bit
#             new_bit ^= (1<<b)
#             new_bit ^= (1<<k)
#             if new_bit in index:
#                 union(i, index[new_bit])
# ```

# 由於我們也可以將當前的字母換成一樣的字母, 也就是words[i]不變
# 也就是關於duplicate words[i]的部分, 他們肯定也是都是connected的
# 所以這部分我們也要union一下, 我們可以在求index的時候順帶處理

# 由於我們需要union-find, 我們用index作為每個words[i]的key
# 因此我們得找一下每個words[i]的index是多少, 方便我們之後進行union

# ```py
# index = {}
# for i, bit in enumerate(arr):
#     if bit in index:
#         union(i, index[bit])
#         index[bit] = find(i)
#     else:
#         index[bit] = i
# ```

# 再來是`add`跟`delete`操作:
# 但words[j] +1 character 後如果變成words[j]
# 代表words[j] -1 character 後會變成words[i]
# 這兩個步驟其實是一樣意思, 所以我們就擇一即可
# 這部很簡單, 我們挑選`delete`, 把字母刪掉即可, time:O(26)
# ```py
# for j in range(26):
#     if (bit>>j)&1:
#         new_bit = bit^(1<<j)
#         if new_bit in index:
#             union(i, index[new_bit])
# ```


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        
        def encode(s):
            bit = 0
            for ch in s:
                bit |= (1<<(ord(ch)-ord("a")))
            return bit

        arr = []
        for word in words:
            arr.append(encode(word))

        # union-find
        parent = list(range(n))
        rank = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        index = {}
        for i, bit in enumerate(arr):
            if bit in index:
                union(i, index[bit])
                index[bit] = find(i)
            else:
                index[bit] = i

        # replace
        MAP = {}
        for i, bit in enumerate(arr):
            for j in range(26):
                if (bit>>j)&1 == 0: continue
                # replace existed one
                x = bit^(1<<j)
                if x in MAP:
                    union(i, MAP[x])
                MAP[x] = i
            

        # delete
        for i, bit in enumerate(arr):
            for j in range(26):
                if (bit>>j)&1:
                    new_bit = bit^(1<<j)
                    if new_bit in index:
                        union(i, index[new_bit])

        groups = set()
        for i in parent:
            p = find(i)
            groups.add(p)

        return [len(groups), max(rank)]