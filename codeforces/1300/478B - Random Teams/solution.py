# Intuition: 計算pair of friends: comb(group_size, 2)
# 所以根據combination的公式, group size增加, 會是乘法(倍數)增長, 所以:
# min pair of friends: equally split into m groups
# max pair of friends: one giant group, + one-man-group + one-man-group + ...
 
n, m = list(map(int, input().split()))
 
from math import comb
 
mink = 0
 
# calculate min pair of friends, 將n平均分配到m個groups上
group_size = n//m
remaining = n - (n//m) * m
x = comb(n//m + 1, 2)
for i in range(remaining): # 無法整除的部分，平均分配到前remaining groups
    mink += x
y = comb(n//m, 2)
for i in range(m - remaining):
    mink += y
 
maxk = comb(n-m+1, 2) # 一個大group, 其餘size都1
print(mink, maxk)