# Intuition

startValue -> *= 2 -> target
           -> -= 1

from start to target, can think startValue as root
each time we have two operation to reach target, and we can keep branching to reach target

if we think above as a tree and think reversely, there is only one way from target back to root (startValue)
1. if target%2 == 0, target //= 2, where target > startValue
2. if target%2 != 0, target = (target+1)//2 , where target > startValue

if target < startValue, there is only one way to reach startValue, i.e. keep increment 1
=> step += startValue-target if target < value