from collections import Counter
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        words = "".join(chunks).split(' ')
        count = Counter()
        for word in words:
            word = word.strip().rstrip('-').lstrip('-')
            
            i = j = 0
            while j < len(word):
                if word[j].isalpha():
                    j += 1
                else:
                    k = j
                    while k < len(word) and word[k] == '-':
                        k += 1
                    if k-j == 1:
                        j = k
                    else:
                        count[word[i:j]] += 1
                        i = j = k
            count[word[i:j]] += 1

        return [count[t] for t in queries]

