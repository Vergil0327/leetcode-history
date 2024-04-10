class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)

        def calTime(car1, car2):
            pos1, spd1 = car1
            pos2, spd2 = car2
            return (pos2-pos1)/(spd1-spd2)

        res = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            pos, spd = cars[i]
            while stack and (cars[stack[-1]][1] >= spd or 
                            (res[stack[-1]] > 0 and calTime(cars[i], cars[stack[-1]]) >= res[stack[-1]])):
                stack.pop()

            if stack:
                res[i] = calTime(cars[i], cars[stack[-1]])

            stack.append(i)
        return res
