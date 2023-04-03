# Intuition

we can use two pointers (sliding window) to maintain a window with `k` flips at most.

X X X X X X X X X X X X X X X X X X X X X X X
l ->    r ->


keep moving `r` pointer and count how many 1's in window[l:r] with `k` flips at most
if we flips more than `k`, move `l` pointer until flips <= `k`
