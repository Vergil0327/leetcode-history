# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def myAtoi(self, s: str) -> int:
		    # remove leading zero
        queue = deque(s)
        while queue and queue[0] == " ":
            queue.popleft()
        if not queue: return 0
        
		    # store sign if exists
        sign = "+"
        if queue[0] == "+" or queue[0] == "-":
            sign = queue[0]
            queue.popleft()

		    # retrieve valid ascii letters. (0-9)
        asci = ""
        while queue:
            ch = queue.popleft()
            if ch not in set("1234567890"):
                break
            asci += ch
        if asci == "": return 0

		    # ascii to integer
        num = 0
        power = 0
        for i in range(len(asci)-1, -1, -1):
            num += (ord(asci[i])-ord("0")) * (10 ** power)
            power += 1
			
		    # clamp integer to [-2**31, 2**31-1]
        return max(-num, -2**31) if sign == "-" else min(num, 2**31-1)

# We can further optimize memory usage by using two pointers to store our valid ascii string
# time complexity: O(n)
# space complexity: O(1)
class SolutionOptimized:
    def myAtoi(self, s: str) -> int:
        if s == "": return 0

		    # remove leading zero
        idx = 0        
        while idx < len(s) and s[idx] == " ":
            idx += 1
        if idx >= len(s): return 0
        
		    # store sign if exists
        sign = "+"
        if s[idx] == "+" or s[idx] == "-":
            sign = s[idx]
            idx += 1
        if idx >= len(s): return 0

		    # retrieve valid numeric string. (0-9)
        end = idx
        while end < len(s):
            ch = s[end]
            if ch not in set("1234567890"):
                break
            end += 1
        if idx == end: return 0
        
		    # ascii to integer
        num = 0
        power = 0
        for i in range(end-1, idx-1, -1):
            num += (ord(s[i])-ord("0")) * (10 ** power)
            power += 1

		    # clamp integer to [-2**31, 2**31-1]
        return max(-num, -2**31) if sign == "-" else min(num, 2**31-1)