# sort positions first
# check each lantern's minimum required distance between its neighbor or road end

[n, length] = list(map(int, input().split()))
positions = list(map(int, input().split()))
positions.sort()
 
gap = 0
for i in range(1, len(positions)):
    gap = max(gap, (positions[i]-positions[i-1]) / 2)
 
gap = max(gap, positions[0])
gap = max(gap, length - positions[-1])
print(f"{gap:.10f}")