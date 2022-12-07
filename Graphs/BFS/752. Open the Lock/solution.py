# BFS
class Solution:
    def wheelLock(self, lock: str):
        res = []
        charArr = list(lock)
        for i in range(len(charArr)):
            ch = charArr[i]
            if ch == '9':
                charArr[i] = '0'
            else:
                charArr[i] = chr(ord(ch)+1 )
            res.append("".join(charArr))
            
            if ch == '0':
                charArr[i] = '9'
            else:
                charArr[i] = chr(ord(ch)-1 )
            res.append("".join(charArr))
            
            charArr[i] = ch

        return res
    
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for dead in deadends:
            visited.add(dead)
        
        # edge case: "0000" in deadend
        if "0000" in visited:
            return -1
        
        queue = deque(["0000"])
        visited.add("0000")

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()

                if curr == target:
                    return step
                
                for nxt in self.wheelLock(curr):
                    if nxt not in visited:
                        queue.append(nxt)
                        visited.add(nxt)
            step += 1
            
        return -1


# Optimized, bidirection BFS
# explanation: https://labuladong.github.io/algo/4/31/110/
class Solution:
    def wheelLock(self, lock: str):
        res = []
        charArr = list(lock)
        for i in range(len(charArr)):
            ch = charArr[i]
            if ch == '9':
                charArr[i] = '0'
            else:
                charArr[i] = chr(ord(ch)+1 )
            res.append("".join(charArr))
            
            if ch == '0':
                charArr[i] = '9'
            else:
                charArr[i] = chr(ord(ch)-1 )
            res.append("".join(charArr))
            
            charArr[i] = ch

        return res
    
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for dead in deadends:
            visited.add(dead)
        
        # edge case: "0000" in deadend
        if "0000" in visited:
            return -1

        q1, q2 = set(), set()
        q1.add("0000")
        q2.add(target)
        step = 0
        while q1 and q2:
            tmp = set()
            for node in q1:
                if node in visited: continue
                if node in q2: return step

                visited.add(node)
                for nxt in self.wheelLock(node):
                    if nxt not in visited:
                        tmp.add(nxt)
            step += 1
            q1 = q2
            q2 = tmp
        return -1
