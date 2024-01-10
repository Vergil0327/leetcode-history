class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)//2
        k = len(balls)

        @cache
        def C(m, n):
            if m == n: return 1
            if n == 1: return m
            return C(m-1, n-1) + C(m-1, n)

        self.total = self.same = 0
        box1, box2 = defaultdict(int), defaultdict(int)
        def dfs(i, box1, box2):
            if i == k:
                numBall1 = sum(box1.values())
                numBall2 = sum(box2.values())
                if numBall1 != numBall2: return

                distinct1 = distinct2 = 0
                perm = 1
                for typ, cnt in box1.items():
                    if cnt == 0: continue
                    distinct1 += 1
                    perm *= C(balls[typ], cnt)

                for cnt in box2.values():
                    if cnt > 0:
                        distinct2 += 1

                self.total += perm
                self.same += perm * int(distinct1 == distinct2)

                return
            for c in range(balls[i]+1):
                box1[i] += c
                box2[i] += balls[i]-c
                dfs(i+1, box1, box2)
                box1[i] -= c
                box2[i] -= balls[i]-c

        dfs(0,box1, box2)
        
        return self.same / self.total

# no more calculation of sum(box.values())
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)//2
        k = len(balls)

        @cache
        def C(m, n):
            if m == n: return 1
            if n == 1: return m
            return C(m-1, n-1) + C(m-1, n)

        self.total = self.same = 0
        box1, box2 = defaultdict(int), defaultdict(int)
        def dfs(i, box1, box2, numBall1, numBall2):
            if i == k:
                if numBall1 != numBall2: return

                distinct1 = distinct2 = 0
                perm = 1
                for typ, cnt in box1.items():
                    if cnt == 0: continue
                    distinct1 += 1
                    perm *= C(balls[typ], cnt)

                for cnt in box2.values():
                    if cnt > 0:
                        distinct2 += 1

                self.total += perm
                self.same += perm * int(distinct1 == distinct2)

                return
            for c in range(balls[i]+1):
                box1[i] += c
                box2[i] += balls[i]-c
                dfs(i+1, box1, box2, numBall1+c, numBall2+balls[i]-c)
                box1[i] -= c
                box2[i] -= balls[i]-c

        dfs(0,box1, box2, 0, 0)
        
        return self.same / self.total