package main

import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	if len(s) > 12 {
		return nil
	}

	res := []string{}
	group := 4
	var dfs func(state []string, s string)
	dfs = func(state []string, s string) {
		if s == "" && group == 0 {
			res = append(res, strings.Join(state, "."))
			return
		}

		if group < 0 {
			return
		}

		// 0-255, three digits at most
		for i := 0; i < min(len(s), 4); i++ {
			ip := s[:i+1]
			if !check(ip) {
				continue
			}

			// ip consists of 4 addrss
			group -= 1
			dfs(append(state, s[:i+1]), s[i+1:])
			group += 1
		}
	}
	dfs([]string{}, s)

	return res
}

// T:O(n), n<=3; 3 digits at most
func check(addr string) bool {
	if len(addr) > 4 {
		return false
	}

	// check no leading zeros
	for i := 0; i < len(addr)-1; i++ {
		if addr[i] == '0' {
			return false
		} else {
			break
		}
	}

	num, err := strconv.ParseInt(addr, 10, 64)
	if err != nil {
		return false
	}

	return num >= 0 && num <= 255
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
