class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x, y)

        if x == y: # no cycle
            res = [0]*n
            for k in range(1, n):
                res[k-1] += n-k
            
            return [pair*2 for pair in res]


        def func1(size):
            count = [0]*n
            for t in range(1, n+1):
                idx = t-1
                l, r = 1, size-t
                count[idx] += max(0, r-l+1) # 用max(0, value)來避免加總到無意義的負數(r<l)
            return count
        def func2(left, right):
            count = [0]*n
            for t in range(1, n+1):
                l, r = max(1, left+3-t), min(left, left+2+right-t)
                count[t-1] += max(0, r-l+1)
            return count
        def func3(size, middle_left, middle_right):
            count = [0]*n

            # (i, middle_left exclude x)
            for t in range(1, n+1):
                l = max(1, size+2-t)
                r = min(size, size+1+middle_left-t)
                
                count[t-1] += max(0, r-l+1)

            # (i, middle_right exclude x)
            for t in range(1, n+1):
                l = max(1, size+2-t)
                r = min(size, size+1+middle_right-t)
                
                count[t-1] += max(0, r-l+1)

            # (i, x) where i in size
            for t in range(1, n+1):
                if t <= size:
                    count[t-1] += 1
            return count

        def func4(size):
            count = [0]*n
            alreadyMultiply2 = [0]*n
            for t in range(1, n+1):
                clockwise = t
                counterclockwise = size-t
                if clockwise < counterclockwise: # clockwise的(i, i+t)是最短路徑, 這時(i,j)是合法pair
                    count[t-1] += size
                elif clockwise == counterclockwise:
                    alreadyMultiply2[t-1] += size
            return count, alreadyMultiply2

        left = x-1
        right = n-y

        arr1 = func1(left)
        arr2 = func1(right)
        arr3 = func2(left, right)

        middle_left_size = (y-x)//2
        middle_right_size = (y-x+1)//2
        arr4 = func3(left, middle_left_size, middle_right_size)
        arr5 = func3(right, middle_right_size, middle_left_size)

        middle = y-x+1
        arr6, alreadyX2 = func4(middle)
        
        tmp = [sum(arrs)*2 for arrs in zip(arr1, arr2, arr3, arr4, arr5, arr6)]
        return [x+y for x, y in zip(tmp, alreadyX2)]


# solution by @lee215
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/solutions/4601078/java-c-python-burning-points/
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x, y)

        if x == y: # no cycle
            res = [0]*n
            for k in range(1, n):
                res[k-1] += n-k
            
            return [pair*2 for pair in res]

        
        res = [0] * n
        for i in range(1, n+1):
            res[0] += 2 # go left and go right
            
            # 往左抵達n=1時停止, [1 <- i, 1 <- x <- y <- i]
            # 根據i在[1,x]或[y,n]位置的不同, 走的路也不同
            res[min(i-1, abs(i-y)+x)] -= 1

            # 往右抵達n時停止, [i -> n, i -> x -> y -> n]
            res[min(abs(n-i), abs(i-x)+1+n-y)] -= 1

            ## 每當抵達x或y, 我們都有兩種路徑可選
            # 抵達x然後分兩條路, 哪條路更近選哪條
            res[min(abs(i-x), abs(y-i)+1)] += 1
            # 抵達y後分兩條路
            res[min(abs(i-x)+1, abs(y-i))] += 1

            # 中間cycle部分, 從x, y兩端出發, 會在cycle中間停止
            # 根據奇數或偶數長度, 兩個走法會分別停在mid, 或停在mid-1及mid+1
            r = max(x-i, 0) + max(i-y, 0)
            res[r + (y-x+0)//2] -= 1
            res[r + (y-x+1)//2] -= 1

        # 得到所有點所貢獻的edges
        return list(accumulate(res))