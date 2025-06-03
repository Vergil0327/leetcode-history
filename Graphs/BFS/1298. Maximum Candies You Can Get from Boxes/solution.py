class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)

        res = 0
        while queue:
            renew = False
            for _ in range(len(queue)):
                box_id = queue.popleft()
                if status[box_id]:
                    renew = True
                    res += candies[box_id]
                    for key in keys[box_id]:
                        status[key] = 1

                    for new_box in containedBoxes[box_id]:
                        queue.append(new_box)
                else:
                    queue.append(box_id)
            if not renew:
                break
        return res