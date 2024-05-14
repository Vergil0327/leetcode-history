class Solution:
    @cache
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        if target < x:
            # x=5, target=2 => 5/5 + 5/5
            # x=5, target=4 => 5-5/5
            return min(target + target-1, x-target + x-target)
        y = log(target, x)
        l, r = floor(y), ceil(y)
        next_target1 = target-pow(x, l)
        next_target2 = pow(x, r)-target

        return min(self.leastOpsExpressTarget(x, next_target1) + (l-1)+1  if next_target1 < target else inf,
                   self.leastOpsExpressTarget(x, next_target2) + (r-1)+1  if next_target2 < target else inf)