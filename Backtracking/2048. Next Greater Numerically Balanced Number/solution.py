class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def dfs(i, length, curNum, counter):
            if i >= length:
                is_balanced = True
                for d, freq in counter.items():
                    if freq != 0 and d != freq:
                        is_balanced = False
                        break

                if is_balanced:
                    self.candidates.append(curNum)
                return

            for d in range(1, length+1):
                if counter[d] >= d: continue   # Prune if number of occurrences of `d` is greater than `d`
                if counter[d] + (length - i) < d: continue  # Prune if not enough number of occurrences of `d`
                counter[d] += 1
                dfs(i + 1, length, curNum * 10 + d, counter)
                counter[d] -= 1

        for length in range(len(str(n)), len(str(n)) + 2):
            self.candidates = []
            dfs(0, length, 0, Counter())
            for num in self.candidates:
                if num > n:
                    return num