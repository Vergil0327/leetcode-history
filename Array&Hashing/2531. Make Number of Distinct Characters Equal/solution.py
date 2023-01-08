class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        m, n = len(counter1), len(counter2)
        for c1 in set(word1):
            for c2 in set(word2):
                i, j, k , l = counter1[c1], counter1[c2], counter2[c1], counter2[c2]
                a, b = m, n
                counter1[c1] -= 1
                counter1[c2] += 1
                counter2[c1] += 1
                counter2[c2] -= 1
                
                if counter1[c1] == 0:
                    a -= 1
                if counter1[c2] == 1:
                    a += 1
                if counter2[c2] == 0:
                    b -= 1
                if counter2[c1] == 1:
                    b += 1
                
                if a == b: return True
                
                counter1[c1], counter1[c2], counter2[c1], counter2[c2] = i, j, k, l
        return False
