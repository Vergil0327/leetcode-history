class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
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