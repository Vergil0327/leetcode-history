
class Solution:
    def score(self, A: List[str], X: str) -> int:
        # note. Each cards[i] is composed of only lowercase English letters between 'a' and 'j'.
        wildcard = 0 # aa bb cc dd ee ff gg hh ii jj
        countL = [0] * 10 # x在左邊
        countR = [0] * 10 # x在右邊
        for x, y in A:
            if x == y == X:
                wildcard += 1
            elif x == X:
                countL[ord(y) - ord("a")] += 1
            elif y == X:
                countR[ord(x) - ord("a")] += 1

        def countPairs(count):
            """
            return (pairs, remaining)
            """
            
            sl = SortedList()
            for num in count:
                if num > 0:
                    sl.add(num)
                
            pairs = 0
            while len(sl) > 1:
                a = sl.pop()
                b = sl.pop(0)
                pairs += 1
                a -= 1
                b -= 1
                if a > 0:
                    sl.add(a)
                if b > 0:
                    sl.add(b)
            return pairs, sum(sl)


        pairs = remain = 0
        for count in [countL, countR]:
            p, r = countPairs(count)
            pairs += p
            remain += r
        
        used = min(wildcard, remain)
        wildcard -= used
        extra = min(pairs, wildcard // 2)
        return pairs + used + extra
