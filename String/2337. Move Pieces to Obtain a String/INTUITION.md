# Intuition

1. first of all, if count of "L", "R" and "_" doesn't match, directly return False

2. try to find substring _*x+L / _*x+R in start to match every substring _*y + L / _*y + R in target
   - for _*x + L in start and _*y + L in target, if x >= y, we can match by moving L to the left
   - for _*x + R in start and _*y + L in target, if x <= y, we can match by moving R to the right
   - otherwise, we can't match through moving character in start