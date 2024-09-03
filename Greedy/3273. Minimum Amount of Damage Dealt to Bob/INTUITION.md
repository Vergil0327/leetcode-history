# Intuition

這題首先想到的是計算每個enemy需要多少回合(rounds)才能消滅
這樣我們就能計算消滅每個enemy[i]的CP值 = damage[i]/rounds where rounds=ceil(health[i]/power)

我們由大到小排序, 然後greedily的消滅CP值最高的角色, 也就是計算下來單回合能消滅最多damage的enemy
同時消滅的過程中所承受的傷害可以用suffix sum來預先處理

所以整體框架為:

```py
n = len(damage)
enemy = []
for i in range(n):
    rounds = ceil(health[i]/power)
    enemy.append([damage[i], rounds])

enemy.sort(key=lambda x:-x[0]/x[1]) # 以消滅的CP值排序: CP = -damage[i]/ceil(health[i]/power)

sufsum = [0] * (n+1) # sufsum[i]: the total damage from enemy[i:]
for i in range(n-1, -1, -1):
    sufsum[i] = sufsum[i+1] + enemy[i][0]
    
res = 0
for i in range(n):
    _, rounds = enemy[i]
    res += sufsum[i] * rounds
return res
```