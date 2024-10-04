class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def sliding_window_at_most(word, k):
            if k < 0: return 0

            index = {}
            vowel = valid = res = 0
            
            l = 0
            for r in range(len(word)):
                if word[r] in {'a', 'e', 'i', 'o', 'u'}:
                    vowel += 1

                    # if word[r] in index:
                    #     if index[word[r]] < l:
                    #         valid += 1
                    #     index[word[r]] = r
                    # else:
                    #     index[word[r]] = r
                    #     valid += 1
                    if word[r] not in index or index[word[r]] < l: # 第一個合法vowel
                        valid += 1
                    index[word[r]] = r

                while r-l+1 - vowel > k:
                    if word[l] in {'a', 'e', 'i', 'o', 'u'}:
                        if index[word[l]] == l:
                            valid -= 1
                        vowel -= 1
                    l += 1

                if valid == 5:
                    rr = min(index['a'], index['e'], index['i'], index['o'], index['u'])
                    res += rr-l+1
            return res
        return sliding_window_at_most(word, k) - sliding_window_at_most(word, k-1)

# One Pass
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        consecutiveVowel = [0] * (n+2)
        for i in range(n-1, -1, -1):
            if word[i] in "aeiou":
                consecutiveVowel[i] = consecutiveVowel[i+1] + 1

        valid = numConsonant = r = res = 0
        vowels = Counter()
        for l in range(n):
            while r < n and (valid < 5 or numConsonant < k):
                if word[r] in "aeiou":
                    vowels[word[r]] += 1
                    if vowels[word[r]] == 1:
                        valid += 1
                else:
                    numConsonant += 1
                r += 1

            if valid == 5 and numConsonant == k:
                res += 1 + consecutiveVowel[r]

            if word[l] in "aeiou":
                vowels[word[l]] -= 1
                if vowels[word[l]] == 0:
                    valid -= 1
            else:
                numConsonant -= 1
        return res