class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        arr = list(num)

        for i in range(n):
            if change[int(arr[i])] > int(arr[i]):
                for j in range(i, n):
                    vv = int(arr[j])

                    if change[vv] >= vv:
                        arr[j] = str(change[vv])
                    else:
                        break
                return "".join(arr)
        return num
