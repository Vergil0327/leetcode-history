class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # find label's row
        row = 1
        while ((2**row)-1) < label:
            row += 1

        # from label to root
        path = []
        while row:
            path.append(label)
            if row%2 == 0:
                leftmost = (2**row)-1
                idx = leftmost - label
                parentIdx = idx//2
                label = 2**(row-2) + parentIdx
            else:
                leftmost = 2**(row-1)
                idx = label-leftmost
                parentIdx = idx//2
                label = leftmost-1 - parentIdx
            row -= 1
        return reversed(path)