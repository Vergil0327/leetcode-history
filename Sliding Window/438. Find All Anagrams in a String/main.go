package main

func findAnagrams(s string, p string) []int {
	if len(p) > len(s) {
		return nil
	}

	window, need := map[byte]int{}, map[byte]int{}
	for i := range p {
		need[p[i]] += 1
	}

	valid := 0
	res := []int{}

	l, r := 0, 0
	for r < len(s) {
		ch := s[r]
		r += 1

		if _, ok := need[ch]; ok {
			window[ch] += 1
			if window[ch] == need[ch] {
				valid += 1
			}
		}

		// [l, r), keeps window valid
		for r-l >= len(p) {
			if valid == len(need) {
				res = append(res, l)
			}

			c := s[l]
			l += 1
			if _, ok := need[c]; ok {
				if window[c] == need[c] {
					valid -= 1
				}
				window[c] -= 1
			}
		}
	}
	return res
}
