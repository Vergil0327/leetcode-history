class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        
        leftmost = []
        j = 0
        for i in range(M):
            if j < N and s[i] == t[j]:
                j += 1
            leftmost.append(j)

        score = N-j # score is number of deletion

        # leftmost[i] means t[:leftmost[i]] is subseq, need to delete t[leftmost[i]:]
        # leftmost is first deletion from left to make t[:leftmost[i]] valid subseq

        # rightmost means t[rightmost+1:] is subseq, need to delete t[:rightmost+1]
        # rightmost is first deletion from the right to make t[rightmost:] a valid subseq

        rightmost = N-1
        for i in range(M-1, -1, -1):
            # rightmost index must >= leftmost index
            # deletion can't be negative
            score = min(score, max(rightmost-leftmost[i]+1, 0))

            if rightmost >= 0 and s[i] == t[rightmost]:
                rightmost -= 1

        return min(score, rightmost-0+1)