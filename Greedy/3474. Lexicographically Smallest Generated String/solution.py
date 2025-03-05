class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        """
        Greedy
        """
        n, m = len(str1), len(str2)
        word = [""] * (n + m - 1)
        T = [False] * (n + m - 1)

        # 1. fill all the `T`s
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if word[i + j] and word[i + j] != str2[j]:
                        return ""
                    word[i + j] = str2[j]
                    T[i + j] = True

        # 2. fill all the `F`s with 'a' first
        for i in range(n + m - 1):
            if not word[i]:
                word[i] = "a"

        for i in range(n):
            if str1[i] == "F":
                # 3. check if aleady different
                diff = False
                for j in range(m):
                    if word[i + j] != str2[j]:
                        diff = True
                        break
                if diff:
                    continue

                # 4. find a char to change from the end to the begin
                change = False
                for j in range(m - 1, -1, -1):
                    # if cur is `T`, it cannot be changed, continue
                    if T[i + j]: continue
                    
                    if word[i+j] == "a":
                        word[i + j] = "b"

                    change = True
                    break

                # once we can't change and still not satisfy `F` condition, directly return 
                if not change: return ""

        return "".join(word)
