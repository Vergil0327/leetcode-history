class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def findMinRect(top, down, left, right):
            l, t, r, bot = inf, inf, -1, -1
            
            for i in range(top, down+1):
                for j in range(left, right+1):
                    if grid[i][j] > 0:
                        l = min(l, j)
                        r = max(r, j)
                        t = min(t, i)
                        bot = max(bot, i)
            return (r-l+1) * (bot-t+1)

        res = m*n
        # horizontal split
        for split1 in range(1, m):
            # horizontal split
            for split2 in range(split1+1, m):
                area1 = findMinRect(0, split1-1, 0, n-1) # top
                area2 = findMinRect(split1, split2-1, 0, n-1) # middle
                area3 = findMinRect(split2, m-1, 0, n-1) # bottom
                res = min(res, area1+area2+area3)

        # horizontal split
        for split1 in range(1, m):
            # upper vertical split
            for split2 in range(1, n):
                area1 = findMinRect(0, split1-1, 0, split2-1) # top-left
                area2 = findMinRect(0, split1-1, split2, n-1) # top-right
                area3 = findMinRect(split1, m-1, 0, n-1)
                res = min(res, area1+area2+area3)

            # lower vertical split
                area1 = findMinRect(0, split1-1, 0, n-1) # top
                area2 = findMinRect(split1, m-1, 0, split2-1) # bottom-left
                area3 = findMinRect(split1, m-1, split2, n-1) # bottom-right
                res = min(res, area1+area2+area3)

        # vertical split
        for split1 in range(1, n):
            # vertical split
            for split2 in range(split1+1, n):
                area1 = findMinRect(0, m-1, 0, split1-1) # left
                area2 = findMinRect(0, m-1, split1, split2-1) # mid
                area3 = findMinRect(0, m-1, split2, n-1) # right
                res = min(res, area1+area2+area3)

        # vertical split
        for split1 in range(1, n):
            # left horizontal split
            for split2 in range(1, m):
                area1 = findMinRect(0, split2-1, 0, split1-1) # left-top
                area2 = findMinRect(split2, m-1, 0, split1-1) # left-bottom
                area3 = findMinRect(0, m-1, split1, n-1)
                res = min(res, area1+area2+area3)

            # right horizontal split
                area1 = findMinRect(0, m-1, 0, split1-1) # left
                area2 = findMinRect(0, split2-1, split1, n-1) # right-top
                area3 = findMinRect(split2, m-1, split1, n-1) # right-bottom
                res = min(res, area1+area2+area3)
        return res
    