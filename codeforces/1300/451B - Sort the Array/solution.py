n = int(input())
arr = list(map(int, input().split()))

# 目的:
# arr[:i] + reversed(arr[i:j]) + arr[j:] = sorted(arr)

i, j = 0, n-1
while i+1 < n and arr[i] < arr[i+1]:
    i += 1

while j-1 >= 0 and arr[j] > arr[j-1]:
    j -= 1

if i == n-1 or j == 0:
    print("yes")
    print(1, 1)
else:
    arr2 = arr[:i] + list(reversed(arr[i:j+1])) + arr[j+1:]
    if list(sorted(arr)) == arr2:
        print("yes")
        print(i+1, j+1) # to 1-indexed
    else:
        print("no")
