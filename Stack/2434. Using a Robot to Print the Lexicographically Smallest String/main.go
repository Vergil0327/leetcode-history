package main

import "strings"

// T:O(n)
// store min character after i-th position
// we can use this information to determine if we should continue append to t or write to papper
func robotWithString2(s string) string {
	minCh := byte('z')
	minCharacterAfter := make([]byte, len(s))
	for i := len(s) - 1; i >= 0; i-- {
		minCh = min(minCh, s[i])
		minCharacterAfter[i] = minCh
	}

	res := strings.Builder{}
	res.Grow(len(s))
	t := []byte{}

	i := 0
	for i < len(s) || len(t) > 0 {
		if i == len(s) {
			break
		}

		if len(t) == 0 || t[len(t)-1] > minCharacterAfter[i] {
			t = append(t, s[i])
			i += 1
			continue
		}

		res.WriteByte(t[len(t)-1])
		t = t[:len(t)-1]
	}

	for len(t) > 0 {
		res.WriteByte(t[len(t)-1])
		t = t[:len(t)-1]
	}

	return res.String()
}

func min(a, b byte) byte {
	if a < b {
		return a
	}

	return b
}

// Simulate Robot
// T:O(26 * n)
func robotWithString(s string) string {
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a'] += 1
	}

	res := strings.Builder{}
	t := ""
	low := 0
	for _, ch := range s {
		t = string(ch)
		count[ch-'a'] -= 1

		for low < 26 && count[low] == 0 {
			low += 1
		}

		for len(t) > 0 && int(t[len(t)-1]-'a') <= low {
			res.WriteByte(t[len(t)-1])
			t = t[:len(t)-1]
		}
	}

	return res.String()
}

// brute force
// T:O(26 * n), got TLE in golang
// ! unfortunately, it seems that type conversion is slow
// got pass when using strings.Builder instead
func robotWithStringTLE(s string) string {
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a'] += 1
	}

	res := ""
	t := ""
	low := 0
	for _, ch := range s {
		t += string(ch) // ! slow
		count[ch-'a'] -= 1

		for low < 26 && count[low] == 0 {
			low += 1
		}

		for len(t) > 0 && int(t[len(t)-1]-'a') <= low {
			res += string(t[len(t)-1]) // ! slow
			t = t[:len(t)-1]
		}
	}

	return res
}
