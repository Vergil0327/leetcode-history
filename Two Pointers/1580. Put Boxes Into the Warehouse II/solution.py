class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse = True)

        l, r = 0, len(warehouse)-1

        cnt = 0
        for hei in boxes:
            if l > r: break
            if hei > max(warehouse[l], warehouse[r]): continue
            if warehouse[r] < hei or (warehouse[l] >= hei and warehouse[l] < warehouse[r]):
                l += 1
            else:
                r += 1
            cnt += 1
        return cnt