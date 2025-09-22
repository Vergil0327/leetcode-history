class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def split_merge(arr):
            perms = []
            for i in range(n):
                for j in range(i, n):
                    pre = arr[:i]
                    mid = arr[i:j+1]
                    suf = arr[j+1:]
                    cur = pre + suf
                    for k in range(len(cur)-1):
                        perms.append(cur[:k+1] + mid + cur[k+1:])
                    perms.append(pre+suf+mid)
                    perms.append(mid+pre+suf)
            return perms
    
        queue = deque([nums1])
        visited = set()
        res = 0
        while queue:
            for _ in range(len(queue)):
                arr = queue.popleft()
                if arr == nums2: return res
                key = ",".join(map(str, arr))
                if key in visited: continue
                visited.add(key)

                for nxt in split_merge(arr):
                    queue.append(nxt)
            res += 1
        return res