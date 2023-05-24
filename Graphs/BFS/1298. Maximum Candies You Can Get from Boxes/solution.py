class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)

        res = 0
        while queue:
            locked = set()
            for _ in range(len(queue)):
                box = queue.popleft()
                if status[box] == 0:
                    queue.append(box)
                    locked.add(box)
                    continue

                res += candies[box]
                for key in keys[box]:
                    status[key] = 1
                    locked.discard(key)

                for newBox in containedBoxes[box]:
                    queue.append(newBox)
            if len(locked) == len(queue): break

        return res