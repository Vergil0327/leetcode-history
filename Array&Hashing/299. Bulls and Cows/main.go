// https://leetcode.com/problems/bulls-and-cows/
package main

import "fmt"

/*
The idea is to iterate over the numbers in secret and in guess and count all bulls right away.
For cows maintain an array that stores count of the number appearances in secret and in guess. Increment cows when either number from secret was already seen in guest or vice versa.
*/
func getHintOnePass(secret string, guess string) string {
	bull, cow := 0, 0
	numbers := [10]int{} // 0-9

	for i := 0; i < len(secret); i++ {
		if secret[i] == guess[i] {
			bull += 1
		} else {
			s := secret[i] - '0'
			g := guess[i] - '0'

			// secret[i] encounter past guess[i]
			if numbers[s] < 0 {
				cow += 1
			}

			// guess[i] encounter past secret[i]
			if numbers[g] > 0 {
				cow += 1
			}

			numbers[s] += 1
			numbers[g] -= 1
		}
	}

	return fmt.Sprintf("%dA%dB", bull, cow)
}

func getHint(secret string, guess string) string {
	bull, cow := 0, 0

	s := []byte(secret)
	g := []byte(guess)

	m := map[byte]int{}
	for i := 0; i < len(secret); i++ {
		m[s[i]] += 1
	}

	// calculate bull
	for i := 0; i < len(secret); i++ {
		if s[i] == g[i] {
			bull += 1
			m[s[i]] -= 1
			if val, ok := m[s[i]]; ok && val == 0 {
				delete(m, s[i])
			}
		}
	}

	// calculate cow
	for i := 0; i < len(secret); i++ {
		if s[i] != g[i] && m[g[i]] > 0 {
			cow += 1
			m[g[i]] -= 1
			if val, ok := m[g[i]]; ok && val == 0 {
				delete(m, g[i])
			}
		}
	}

	return fmt.Sprintf("%dA%dB", bull, cow)
}
