# Hashset + Priority Queue
class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = False
        self.point = 0

class Solution:
    def topStudents(self, positive: List[str], negative: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        posSet, negSet = set(), set()
        for word in positive:
            posSet.add(word)

        for word in negative:
            negSet.add(word)
        
        ranks = []
        for i, s in enumerate(report):
            point = [0, student_id[i]]

            for word in s.split():
                if word in posSet:
                    point[0] += 3
                if word in negSet:
                    point[0] -= 1
            
            point[0] = -point[0]
            heapq.heappush(ranks, point)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(ranks)[1])
        return res

# Trie + Priority Queue
class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = False
        self.point = 0

class Solution:
    def topStudents(self, positive: List[str], negative: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        root = TrieNode()
        
        for word in positive:
            curr = root
            for ch in word:
                if ch not in curr.next:
                    curr.next[ch] = TrieNode()
                curr = curr.next[ch]
            curr.end = True
            curr.point = 3

        for word in negative:
            curr = root
            for ch in word:
                if ch not in curr.next:
                    curr.next[ch] = TrieNode()
                curr = curr.next[ch]
            curr.end = True
            curr.point = -1
        
        ranks = []
        for i, s in enumerate(report):
            point = [0, student_id[i]]

            for word in s.split():
                curr = root
                isBreak = False
                for ch in word:
                    if ch not in curr.next:
                        break
                    curr = curr.next[ch]

                # 必須透過 isBreak 確認是目前這個word才計算分數
                # 因為有可能break後剛好curr.end為True，這樣會計算分數錯誤
                # ex. words = ["b", "dcbe"] report=["dcbx"]
                if curr.end and not isBreak:
                    point[0] += curr.point
            
            point[0] = -point[0]
            heapq.heappush(ranks, point)

        res = []
        for _ in range(k):
            pop = heapq.heappop(ranks)
            res.append(pop[1])
        return res
