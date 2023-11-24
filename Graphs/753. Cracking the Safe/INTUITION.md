# Intuition

用n位數, k進制表示目前的密碼state
=> password = X X X X (1 <= n <= 4)
=> 共 pow(k, n) 種密碼

new_str = prev_str + str(d) for d in range(k)
pwd = new_str[len(new_str)-n:]

1. 最短能滿足所有密碼的string肯定是盡可能讓pwd不重複來構造出該string
2. 而這可以想成一個graph, 每一組密碼是個節點, 所以我們要找的就是從訪問過所有節點的路徑中, 找出最終str為最短的一個. 也就是每次前往的下個節點, 盡可能不重複
所以我們用dfs遍歷所有可能找出最佳

最佳解肯定是每次字串的n-size suffix string皆為不重複的password. The existence of such a password is proved by [De Bruijn sequence](https://en.wikipedia.org/wiki/De_Bruijn_sequence#Uses)

因此照這個想法去進行DFS找出第一個合法解即可