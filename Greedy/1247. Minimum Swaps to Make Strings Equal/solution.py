class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2): return -1
        
        count = defaultdict(int)
        stack = []
        for i in range(len(s1)):
            count[s1[i]] += 1
            count[s2[i]] += 1
            if s1[i] != s2[i]:
                stack.append(s1[i])
        if count["x"]%2 != 0 or count["y"]%2 != 0: return -1
        
        stack.sort()

        swap = 0
        i = 0
        while i < len(stack):
            if "".join(stack[i:i+2]) == "xx" or "".join(stack[i:i+2]) == "yy":
                swap += 1
            elif "".join(stack[i:i+2]) == "xy" or "".join(stack[i:i+2]) == "yx":
                swap += 2
            i += 2

        return swap