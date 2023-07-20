# Intuition

因為只有兩個方向, 我們可以用stack存所有向右走的asteroids
一旦出現向左, 就查看stack, 相撞贏的話就持續pop掉stack
最後只會剩兩種情況:
1. 直到最後剩下空stack或是同樣向左的asteroids就加入asteroids
2. stack[-1]是一個絕對值相同的asteroid, 這時兩個會一起消滅, 所以就單純pop掉stack[-1]即可