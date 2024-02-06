class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        # Manacher
        maxRight = maxCenter = -1
        P = [0] * n
        for i in range(n):
            if i <= maxRight:
                j = maxCenter*2-i
                r = min(P[j], maxRight-i)
            else:
                r = 0

            while i-r>=0 and i+r<n and s[i-r] == s[i+r]:
                r += 1

            P[i] = r-1

            if i+P[i] > maxRight:
                maxRight = i+P[i]
                maxCenter = i

        left = [0]*n
        left[0] = 1
        j = 0
        for i in range(1, n):
            while j < n and j+P[j] < i:
                j += 1

            left[i] = max(left[i-1], (i-j)*2+1)

        right = [0]*n
        right[n-1] = 1
        j = n-1

        for i in range(n-2, -1, -1):
            while j >= 0 and j-P[j] > i:
                j -= 1

            right[i] = max(right[i+1], (j-i)*2+1)

        return max(left[i]*right[i+1] for i in range(0, n-1))