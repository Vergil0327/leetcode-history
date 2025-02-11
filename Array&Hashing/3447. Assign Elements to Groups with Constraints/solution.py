class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        multiple2idx = {}
        for i, el in enumerate(elements):
            multiple = el
            if el not in multiple2idx:
                while multiple <= mx:
                    if multiple not in multiple2idx:
                        multiple2idx[multiple] = i
                    multiple += el

        res = [-1] * len(groups)
        for i, group in enumerate(groups):
            if group in multiple2idx:
                res[i] = multiple2idx[group]
        return res