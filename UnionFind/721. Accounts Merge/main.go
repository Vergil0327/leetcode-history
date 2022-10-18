package main

import "sort"

// my solution: https://leetcode.com/problems/accounts-merge/discuss/2718581/Golang-Union-Find-Solution
func accountsMerge(accounts [][]string) [][]string {
	parent := make([]int, len(accounts))
	rank := make([]int, len(accounts))
	for i := range rank {
		parent[i] = i
		rank[i] = 1
	}

	// use index as account
	var find = func(account int) int {
		p := parent[account]

		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	var union = func(account1, account2 int) bool {
		p1, p2 := find(account1), find(account2)
		if p1 == p2 {
			return false
		}

		if rank[p1] >= rank[p2] {
			parent[p2] = p1
			rank[p1] += rank[p2]
		} else {
			parent[p1] = p2
			rank[p2] += rank[p1]
		}

		return true
	}

	emails := map[string]int{}
	for i, account := range accounts {
		for j := 1; j < len(account); j++ {
			email := account[j]

			if _, ok := emails[email]; !ok {
				emails[email] = i
			} else {
				union(i, emails[email])
			}
		}
	}

	mergedAccounts := map[int][]string{} // name: [email]
	for email, account := range emails {
		p := find(account)
		if _, ok := mergedAccounts[p]; !ok {
			mergedAccounts[p] = []string{accounts[p][0]}
		}
		mergedAccounts[p] = append(mergedAccounts[p], email)
	}

	res := [][]string{}
	for _, account := range mergedAccounts {
		sort.Slice(account[1:], func(i, j int) bool {
			return account[1:][i] < account[1:][j]
		})
		res = append(res, account)
	}

	return res
}
