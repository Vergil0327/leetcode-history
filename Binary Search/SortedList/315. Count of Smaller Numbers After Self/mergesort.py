# explanation: https://labuladong.github.io/algo/2/21/41/
class SolutionMergeSort:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = [[num, idx] for idx, num in enumerate(nums)] # [value, index]
        tmp = [0]*len(arr)
        count = [0] * len(arr)
        
        # [left, right]
        def merge(arr, left, mid, right):            
            tmp[left:right+1] = arr[left:right+1].copy()
            
            l, r = left, mid+1
            for i in range(left, right+1):
                if l == mid+1:
                    arr[i] = tmp[r]
                    r += 1
                elif r == right+1:
                    arr[i] = tmp[l]
                    l += 1
                    count[arr[i][1]] += r-(mid+1)
                elif tmp[l][0] > tmp[r][0]:
                    arr[i] = tmp[r]
                    r += 1
                else:
                    arr[i] = tmp[l]
                    l += 1
                    # tmp[l] <= tmp[r] => num in [mid+1, r) is smaller than tmp[l]
                    # tmp[l] mid+1, ..., tmp[r]
                    count[arr[i][1]] += r-(mid+1)
        
        def mergesort(arr, left, right):
            if left >= right: return [left]
            
            mid = left + (right-left)//2
            mergesort(arr, left, mid)
            mergesort(arr, mid+1, right)
            return merge(arr, left, mid, right)
        
        
        mergesort(arr, 0, len(nums)-1)

        return count