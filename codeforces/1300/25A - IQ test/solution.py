"""
找出唯一一個奇偶性跟其他不同的數即可
"""

n = int(input())
nums = list(map(int, input().split()))
 
evenness = [[], []]
ans = -1
for i, num in enumerate(nums, start=1):
    if (len(evenness[num%2])) > 1: continue
    evenness[num%2].append(i)
 
if len(evenness[num%2]) > 1:
    print(evenness[1 - (num%2)][0])
else:
    print(evenness[num%2][0])