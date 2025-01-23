# Intuition

The core idea is to calculate the sum of maximum and minimum elements for all subarrays with at most k elements using a monotonic stack approach.

考察每個nums[i]分別作為**max element**以及**min element**能貢獻多少合法subarray

- 作為max element: XXXX numx[i] XXXXX, 如果能知道prevSmaller跟nextSmaller的位置, 那就能知道能組出多少合法subarray是nums[i]作為max element的
- 作為min element: XXXX nums[i] XXXXX, 如果能知道prevLarger跟nextLarger的位置, 那就能知道能組出多少合法subarray是nums[i]作為min element的

但這題還有個限制是**至多為k-size**, 所以我們要計算的是當前window size在size為{1,2,3,...,k}時的貢獻

The solution has two main functions:

sum_of_min_subarrays_at_most_k(): calculates sum of minimum elements
sum_of_max_subarrays_at_most_k(): calculates sum of maximum elements

It uses monotonic stacks to efficiently find the number of subarrays where the current element is the minimum or maximum.


### Helper function

count_subwindows(L, R, M) is a function that calculates the number of valid subarrays for a given element. Here's how it works:

f(x) is a helper function that calculates the sum of first x+1 natural numbers: (x+1)*x/2
count_subwindows(L, R, M) calculates the number of valid subarrays where:

L is the number of elements smaller than the current element to the left
R is the number of elements smaller than the current element to the right
M is the maximum subarray size (k in this case)


The formula f(M) - f(M-(L+1)) - f(M-(R+1)) + f(M-(L+1)-(R+1)) does the following:

- f(M): total number of subarrays of size up to M
- f(M-(L+1)): subtract subarrays that include elements to the left
- f(M-(R+1)): subtract subarrays that include elements to the right
- f(M-(L+1)-(R+1)): add back subarrays that were double-subtracted

ex. nums=[15,-3,-11], k=3

nums[i] as min element:

i=0
L=0, R=0, M=3

[_, 15, _]: (_,15,_), (_,15), (15,_), (_), (15), (_)

total possible subarrays: f(M)=6
invalid: f(M-(L+1))=3: (_,15), (_), (15)
invalid: f(M-(R+1))=3: (15,_), (15), (_)
double-subtracted: f(M-(L+1)-(R+1))=1 (nums[i] (15) itself)
