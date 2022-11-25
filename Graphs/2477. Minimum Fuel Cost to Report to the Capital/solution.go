package main

// https://space.bilibili.com/206214
func minimumFuelCost(roads [][]int, seats int) int64 {
	ans := 0
	n := len(roads) + 1
	g := make([][]int, n)
	for _, edge := range roads {
		u, v := edge[0], edge[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	var dfs func(u, parent int) int
	dfs = func(u, parent int) int {
		sz := 1
		for _, v := range g[u] {
			if v != parent {
				sz += dfs(v, u)
			}
		}
		if parent != -1 {
			ans += (sz-1)/seats + 1
		}
		return sz
	}
	dfs(0, -1)

	return int64(ans)
}
