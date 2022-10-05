package main

func wordPatternMatch(pattern, str string) bool {
	letterToStr := map[byte]string{}
	strToLetter := map[string]byte{}

	var dfs func(s string, p string) bool
	dfs = func(s string, p string) bool {
		if p == "" && s == "" {
			return true
		}

		if s == "" || p == "" {
			return false
		}

		if substr, ok := letterToStr[p[0]]; ok {
			if len(substr) > len(s) || substr != s[:len(substr)] {
				return false
			}

			if dfs(s[len(substr):], p[1:]) {
				return true
			}
		}

		ptn := p[0]
		for i := 1; i <= len(s); i++ {
			substr := s[:i]
			if p, ok := strToLetter[substr]; ok && ptn != p {
				continue
			}

			strToLetter[substr] = ptn
			letterToStr[ptn] = substr
			if dfs(s[len(substr):], p[1:]) {
				return true
			}

			// backtracking
			delete(strToLetter, substr)
			delete(letterToStr, ptn)
		}

		return false
	}
	return dfs(str, pattern)
}
