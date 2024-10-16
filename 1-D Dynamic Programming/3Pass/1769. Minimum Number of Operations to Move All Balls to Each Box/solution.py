class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        # number of steps for boxes from left
        left_moves = [0] * n
        num_boxes = 0
        for i in range(n):
            left_moves[i] = (left_moves[i-1] if i-1>=0 else 0) + num_boxes
            num_boxes += int(boxes[i] == '1')

        # number of steps for boxes from right
        right_moves = [0] * (n+1)
        num_boxes = 0
        for i in range(n-1,-1,-1):
            right_moves[i] = right_moves[i+1]+num_boxes
            num_boxes += int(boxes[i] == '1')

        return [left_moves[i] + right_moves[i] for i in range(n)]