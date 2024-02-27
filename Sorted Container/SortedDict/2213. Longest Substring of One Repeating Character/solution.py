from sortedcontainers import SortedList, SortedDict
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n, k = len(s), len(queryCharacters)

        interval = SortedDict() # {start_index: length}
        curIdx = -1
        for i in range(n):
            if i == 0 or s[i] != s[i-1]:
                interval[i] = 1
                curIdx = interval.index(i)
            else:
                k, v = interval.peekitem(curIdx)
                interval[k] += 1

        length = SortedList()
        for l in interval.values():
            length.add(l)
   
        arr = list(s)
        res = []
        for i, ch in zip(queryIndices, queryCharacters):
            if ch != arr[i]:
                arr[i] = ch
                idx = interval.bisect_right(i)-1
                
                # break interval
                j, size = interval.peekitem(idx)
                # j______i
                # i j_____
                # j__ i j_
                if size > 1:
                    del interval[j]
                    length.remove(size)

                    if i == j:
                        interval[i] = 1
                        length.add(1)

                        interval[j+1] = size-1
                        length.add(size-1)
                        
                    elif i == j+size-1:
                        interval[i] = 1
                        length.add(1)

                        interval[j] = size-1
                        length.add(size-1)
                    else:
                        interval[i] = 1
                        length.add(1)
                        
                        interval[j] = i-j
                        length.add(interval[j])

                        interval[i+1] = size - (i-j+1)
                        length.add(interval[i+1])

                # merge interval
                ## check merge right
                if i+1<n and ch == arr[i+1]:
                    idx = interval.bisect_right(i)
                    j, size = interval.peekitem(idx)
                    length.remove(size)
                    length.remove(interval[i])
                    del interval[j]

                    interval[i] = interval[i]+size
                    length.add(interval[i])
                
                ## check merge left
                if i-1 >= 0 and ch == arr[i-1]:
                    l = interval.bisect_left(i)-1
                    j, size = interval.peekitem(l)
                    length.remove(interval[i])
                    length.remove(size)
                    interval[j] = size+interval[i]
                    length.add(interval[j])
                    del interval[i]
            res.append(length[-1])
        return res
