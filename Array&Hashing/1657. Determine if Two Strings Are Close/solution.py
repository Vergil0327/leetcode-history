# op1. -> any combination, don't need to care position of characters
# op2. -> freq1 = [...], freq2 = [...], only need to check if freq array is the same or not

# O(nlogn)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        keys1 = set(counter1.keys())
        values1 = sorted(counter1.values())
        keys2 = set(counter2.keys())
        values2 = sorted(counter2.values())

        return  keys1|keys2 == keys1&keys2 and all(a == b for a, b in zip(values1, values2))

# O(n)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        if set(word1) != set(word2): return False
        
        # or just
        # return Counter(Counter(word1).values()) == Counter(Counter(word2).values())

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        freq1 = defaultdict(int)
        for v in counter1.values():
            freq1[v] += 1
        
        freq2 = defaultdict(int)
        for v in counter2.values():
            freq2[v] += 1
            
        for k, freq in freq1.items():
            if freq != freq2[k]: return False

        return True