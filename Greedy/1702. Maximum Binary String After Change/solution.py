class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        s = list(binary)
        n = len(binary)
        zeros = binary.count("0")

        i = 0
        while i < n and s[i] == "1":
            i += 1

        while i < n and s[i] == "0" and zeros > 1:
            s[i] = "1"
            s[i+1] = "0"
            zeros -= 1
            i += 1
        
        i += 1
        while i < n:
            s[i] = "1"
            i += 1
        return "".join(s)