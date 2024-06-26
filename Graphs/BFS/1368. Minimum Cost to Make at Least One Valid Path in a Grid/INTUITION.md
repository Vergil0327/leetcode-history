# Intuition

想法是先用BFS看看能不能不花cost抵達終點
如果不行, 那就從上一步所有經過的點改成其他方向, 看看能不能只花1 cost抵達終點
如果再不行那就再從上一步改方向, 再花費1cost（共2 cost)看看能不能抵達終點
持續進行BFS直到抵達終點

所以本質是持續透過BFS來搜索

至於如何確認能不能從當前這些點作為起點抵達終點
我們可以用DFS從當前起點出發, 把所有經過的點都記錄下來:
- 如果能抵達終點, 也就是終點包含在經過的點內, 那當前cost就是最小cost
- 如果不能, 那就再從這些經過的點做為起點, 繼續透過外層BFS用1 cost轉換方向看下次能不能抵達終點
