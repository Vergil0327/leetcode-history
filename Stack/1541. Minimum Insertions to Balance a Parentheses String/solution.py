class Solution:
    def minInsertions(self, s: str) -> int:
        left = []
        right = []
        cnt = 0
        for c in s:
            if c == "(":
                if right:
                    right.pop()
                    cnt += 1
                    if left:
                        left.pop()
                    else:
                        cnt += 1
                left.append(c)
            else:
                if right:
                    right.pop()
                    if left:
                        left.pop()
                    else:
                        cnt += 1
                else:
                    right.append(c)

        if right:
            right.pop()
            cnt += 1
            if left:
                left.pop()
            else:
                cnt += 1

        while left:
            left.pop()
            cnt += 2
        return cnt