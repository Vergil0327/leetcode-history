# Intuition

由於要求合法的assigned maximum height,
首先能想到的想法是先對`maximumHeight`由大到小排序, 然後greedily assign這些maximum height
並持續記錄當前合法的maximum height, `validHeight`

如果當前maximumHeight[i] = h:

- 如果maximumHeight[i] <= validHeight: 那就直接`res += maximumHeight[i]`並更新`validHeight = validHeight[i]-1`
- 如果maximum[i] > validHeight: 那代表這時候我們能assign的最高高度為validHeight, 並更新`validHeight = validHeight-1`
- 如果要assign的時候, validHeight已經等於0了, 那代表我們沒有合法的positive height可分配了, 直接返回`-1`即可


time: O(nlogn)
space: O(1)