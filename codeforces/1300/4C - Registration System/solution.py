# 單純紀錄每個名字出現的次數即可

n = int(input())
 
from collections import Counter
count = Counter()
for _ in range(n):
    name = input()
    if name not in count:
        print("OK")
    else:
        print(f"{name}{count[name]}")
    count[name] += 1