class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        num, res = 0, []
        for i in range(len(word)):
            num = num*10+int(word[i])
            num %= m
            if num == 0:
                res.append(1)
            else:
                res.append(0)
        return res
