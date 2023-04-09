# 當時weekly contest, Acceptance Rate < 2%

from sortedcontainers import SortedList

# 根據奇偶數, 能判斷下一個合法抵達的index為多少
# 仔細觀察下面例子可發現, 能跟p互換的i都是兩步兩步移動，所以根據當前index與k的奇偶數可判斷出哪些是有可能抵達的index
# 所以我們才對index分成兩個group, 這樣後續可以透過binary search找出上下界然後遍歷可能index

# sls = [SortedList(), SortedList()]
# for i in range(n):
#     if i not in banned:
#         sls[i % 2].add(i)

# 
# k = 5
# [i X X X p] X
# X [X i X p  X]
# X X [X X p  X X]
# X X X [X p  X i X]
# X X X X [p  X X X i]

# k = 4
# [i X X p] X
# X [X i p  X]
# X X [X p  i X]
# X X X [p  X X i]

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned = set(banned + [p])
        sls = [SortedList(), SortedList()]
        
        for i in range(n):
            if i not in banned:
                sls[i % 2].add(i)
        
        res = [-1] * n
        queue = deque([p])
        res[p] = 0
        x = 1 - (k % 2)
        
        while queue:
            i = queue.popleft()
            parity = (i % 2) ^ x
            sl = sls[parity]
            
            # leftmost index to swap = i - k + 1
            # rightmost index to swap = i + k - 1
            
            # if i = 2, k = 4 -> leftmost = 2-4+1 = -1
            # [-1, 0, 1, 2] 4 -> 1 is minimum valid index as startIndex of valid subarray
            # X X [-1   0     {1        2] X X} X X X
            #    i-k+1    abs(i-k+1)   i
            l = abs(i - k + 1)

            # if i = 0, k = 5 -> rightmost = 0+5-1 = 4
            # [X X X X X] {X X X X X X}
            #  i       r  i+k
            #    k size     n-(i+k) size
            r = n - 1 - abs(n - (i + k))
            
            while (j := sl.bisect_left(l)) < len(sl):
                idx = sl[j]
                if idx > r:
                    break
                
                res[idx] = res[i] + 1
                sl.remove(idx)
                queue.append(idx)
        
        return res

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        res = [-1] * n
        ban = set(banned)
        
        queue = deque([[p, 0]])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                curr, op = queue.popleft()
                if curr in visited: continue
                visited.add(curr)

                res[curr] = op

                l, r = curr-k+1, curr+k-1
                if k%2 == 0:
                    i = curr+1
                    while i < n and i <= r:
                        if i not in ban:
                            queue.append((i, op+1))
                        i += 2
                    i = curr-1
                    while i >= 0 and i >= l:
                        if i not in ban:
                            queue.append((i, op+1))
                        i -= 2
                else:
                    i = curr
                    while i+2 < n and i+2 <= r:
                        if i+2 not in ban:
                            queue.append((i+2, op+1))
                        i += 2
                    i = curr
                    while i-2 >= 0 and i-2 >= l:
                        if i-2 not in ban:
                            queue.append((i-2, op+1))
                        i -= 2

        return res