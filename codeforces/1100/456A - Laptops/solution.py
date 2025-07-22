# - a.price
# - a.price < b.price && a.quality > b.quality
# - all ai, bi are distinct
n = int(input())
 
arr = []
for i in range(n):
    [price, quality] = input().split()
    arr.append([int(price), int(quality)])
 
    
flag = 0
arr.sort(key=lambda x:(x[0], -x[1]))
for i in range(n-1):
    if arr[i][0] < arr[i+1][0] and arr[i][1] > arr[i+1][1]:
        flag = 1
        break
if flag:
    print("Happy Alex")
else:
    print("Poor Alex")