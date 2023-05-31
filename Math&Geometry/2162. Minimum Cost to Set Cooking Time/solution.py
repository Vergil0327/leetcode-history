class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minute, sec = targetSeconds//60, targetSeconds%60
        
        option1 = ""
        if minute < 100:
            option1 = (str(minute) if minute > 0 else "")
            if option1:
                option1 += str(sec) if sec >= 10 else "0"+str(sec) # if we have minute to push, we need to fill "0" if sec < 10
            else:
                option1 = str(sec) # no need for prepending zeros

        option2 = ""
        if minute > 0 and sec <= 39:
            minute -= 1
            sec += 60
            option2 = (str(minute) if minute > 0 else "")
            if option2:
                option2 += str(sec) if sec >= 10 else "0"+str(sec) # if we have minute to push, we need to fill "0" if sec < 10
            else:
                option2 = str(sec) # no need for prepending zeros

        def cost(option):
            curr = str(startAt)
            cost = 0
            for i in range(len(option)):
                if option[i] == curr:
                    cost += pushCost  # push
                else:
                    curr = option[i]
                    cost += moveCost + pushCost # push
            return cost

        res = inf
        if option1:
            res = min(res, cost(option1))
        if option2:
            res = min(res, cost(option2))
        return res