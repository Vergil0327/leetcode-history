class Solution:
    def dfs(self, state, num, currVal, prevVal, target):
        if not num:
            if currVal == target:
                self.res.append(state)
            return
        
        for i in range(len(num)):
            prefix, suffix = num[:i+1], num[i+1:]
            if i == 0 or i>0 and num[0] != "0": # no leading zeros
                # +
                self.dfs(state + "+" + prefix, suffix, currVal + int(prefix), int(prefix), target)
                
                # -
                self.dfs(state + "-" + prefix, suffix, currVal - int(prefix), -int(prefix), target)
                
                # *
                # "23+52-36" * 646 = currVal - prevVal + prevVal * int(suffix)
                # restore previous result and calculate current reuslt with `*`
                self.dfs(state + "*" + prefix, suffix, currVal - prevVal + prevVal * int(prefix), prevVal * int(prefix) ,target)

    def addOperators(self, num: str, target: int) -> List[str]:
        dfs = self.dfs
        self.res = []

        for i in range(len(num)):
            if i == 0 or i > 0 and num[0] != "0": # no leading zeros
                dfs(num[:i+1], num[i+1:], int(num[:i+1]), int(num[:i+1]), target)
        return self.res