class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
   
        @cache             
        def isPrime(num):
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0: return False
            return True

        count = Counter()
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    row, col = i+dx, j+dy
                    num = mat[i][j]
                    while 0 <= row < m and 0 <= col < n:
                        num = num*10 + mat[row][col]
                        if isPrime(num) and num > 10:
                            count[num] += 1
                        row, col = row+dx, col+dy
        
        res = -1
        mxFreq = 0
        for prime, freq in count.items():
            if freq > mxFreq:
                mxFreq = freq
                res = prime
            elif freq == mxFreq:
                res = max(res, prime)
        return res

        