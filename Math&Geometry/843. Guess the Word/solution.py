# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def compare(s, t):
            cnt = 0
            for i in range(6):
                if s[i] == t[i]:
                    cnt += 1
            return cnt
        
        pool = set(words)
        while len(pool) > 0:
            guess = random.choice(list(pool))

            match = master.guess(guess)
            if match == 6: return

            tmp = pool.copy()
            for s in pool:
                if compare(s, guess) != match:
                    tmp.remove(s)
            
            pool = tmp
