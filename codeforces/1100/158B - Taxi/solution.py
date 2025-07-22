from collections import Counter
 
n = int(input())
arr = list(map(int, input().split()))
 
count = Counter(arr)
 
res = count[4] + count[3] + count[2]//2
count[1] -= count[3]
 
if count[2]%2:
    res += 1
    count[1] -= 2
 
if count[1] > 0:
    res += (count[1]+3)//4
print(res)