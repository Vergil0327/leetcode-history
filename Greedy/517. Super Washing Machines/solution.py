class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n != 0: return -1

        target = total//n
        # for each machines[i]:
        # if machines[i] > target: it can pass to left left[i] and pass to right right[i]
        # if machines[i] < target, it need left[i] from left and need right[i] from right
        # thus, left[i] + right[i] = machines[i] - target

        # since machines[i] only can pass to its neighbor
        # left[i] = -right[i-1]

        # for edge case machines[0] and machines[n-1]
        # they only can pass to one direction
        # therefore,
        # left[0] = 0 and right[0] = machines[0]-target
        # left[n-1] = machines[n-1]-target and right[n-1] = 0

        left, right = [0] * n, [0] * n
        left[0] = 0
        right[0] = machines[0] - target

        right[n-1] = 0
        left[n-1] = machines[n-1] - target

        for i in range(1, n-1):
            left[i] = -right[i-1]

            # left[i] + right[i] = machines[i] - target
            # => left[i] = machines[i] - target - right[i]
            right[i] = machines[i] - target - left[i]

        ops = 0
        for i in range(n):
            netPass = 0
            if left[i] >= 0: netPass += left[i]
            if right[i] >= 0: netPass += right[i]
            ops = max(ops, netPass)
        return ops
