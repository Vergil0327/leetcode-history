package lcp

import (
	"strings"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	prefix := strs[0]
	for _, str := range strs {

		for strings.Index(str, prefix) != 0 {
			prefix = prefix[0 : len(prefix)-1]
			if prefix == "" {
				return ""
			}
		}
	}

	return prefix
}

func longestCommonPrefixVertical(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	var sb strings.Builder
	for i := 0; ; i++ {
		for _, str := range strs {
			if i == len(str) || strs[0][i] != str[i] {
				return sb.String()
			}
		}
		sb.WriteByte(strs[0][i])
	}
}
