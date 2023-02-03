# Intuition
we can see zig-zag as a sequence of many samll `V-shape` parition, each step is `(numRows-2)*2+2`.

rest of work just math, process each `V-shape` partition row by row and be careful of out-of-index error
- middle rows are pair value
- handle first row and last row independently since it's starting and turning point. only one value


# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Code
```py
# Daily Challenge - Feb., Day 3, 2023
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        n = len(s)
        res = [""]*numRows
        step = (numRows-2)*2+2
        i = 0
        while i < n:
            for j in range(numRows):
                if j == 0: # first row
                    res[j] += s[i+j]
                    continue
                if j == numRows-1 and i+j < n: # end row
                    res[-1] += s[i+j]
                    continue
                
                # middle rows
                if i+j < n:
                    res[j] += s[i+j]
                if i+step-j < n:
                    res[j] += s[i+step-j] 
            i += step
        return "".join(res)
```