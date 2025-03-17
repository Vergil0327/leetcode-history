# Intuition

把每個nums[i]加入到hashmap裡並紀錄index
那這樣就能快速知道跟nums[queries[i]]相同的數分別在哪些index
再透過binary search找出**右方最靠近位置(bisect_right)**以及**左方最靠近位置(bisect_left-1)**後

計算距離並考慮circular即可:

- r = bisect_right(indice[nums[i]], i)%m
  - right closest index, take modular to find circular position if out of bounds
- l = (bisect_left(indice[nums[i]], i)-1+m)%m
  - left closest index, take modular to find circular position if out of bounds