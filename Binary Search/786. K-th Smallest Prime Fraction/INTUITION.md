# Intuition

`arr[i]/arr[j] = mid => arr[j] = arr[i] / mid`

use **binary search** to guess value `mid` and check count by arr[j] = arr[i]/mid
keep trial-and-error to search fraction `mid` between [0,1]

**how to check k-th smallest ?**

since arr is sorted, we can use binary search for arr[j] where arr[j] = arr[i]/mid
if idx = bisect.bisect(arr, arr[i]/mid), then:
indices within [idx, n-1] are the valid arr[j] to make arr[i]/arr[j] <= mid
then we count how many valid pairs are smaller than `mid`.

when count == k, return pair with largest fraction