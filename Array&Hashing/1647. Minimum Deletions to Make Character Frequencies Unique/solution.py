# O(nlogn), sorting + two pointers + hashing
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)

        seen = set()
        stack = []
        i = 1 # unused frequency
        res = 0
        for f in sorted(counter.values()):
            if f not in seen:
                seen.add(f)
                while i < f:
                    stack.append(i)
                    i += 1

                # update i to f+1, next unused freqency
                i = f+1
            else:
                res += f - (stack.pop() if stack else 0)
        return res


