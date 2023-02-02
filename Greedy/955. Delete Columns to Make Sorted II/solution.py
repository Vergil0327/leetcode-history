class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        COLS = len(strs[0])

        deletion = 0
        relation = [-1] * n # 1 means str[i][:j] < str[i+1][:j]; 0 means str[i][:j] == str[i+1][:j]
        for i in range(COLS):
            tmp = relation.copy()
            shouldDel = False
            for j in range(n-1):
                if tmp[j] != 1 and strs[j][i] > strs[j+1][i]:
                    deletion += 1
                    shouldDel = True
                    break
                if (tmp[j] != 1) and strs[j][i] == strs[j+1][i]:
                    tmp[j] = 0
                if strs[j][i] < strs[j+1][i]:
                    tmp[j] = 1

            if not shouldDel:
                relation = tmp
        return deletion
