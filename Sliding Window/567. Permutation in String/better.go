package main

// T:O(n)
func checkInclusionBetter(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	fingerPrintS1, fingerPrintWindow := [26]int{}, [26]int{}
	for i := 0; i < len(s1); i++ {
		fingerPrintS1[s1[i]-'a'] += 1
		fingerPrintWindow[s2[i]-'a'] += 1
	}

	matches := 0
	for i, v := range fingerPrintS1 {
		if fingerPrintWindow[i] == v {
			matches += 1
		}
	}

	l := 0
	for r := len(s1); r < len(s2); r++ {
		// check first window
		if matches == 26 {
			return true
		}

		index := s2[r] - 'a'
		fingerPrintWindow[index] += 1
		if fingerPrintS1[index] == fingerPrintWindow[index] {
			matches += 1
		} else if fingerPrintS1[index]+1 == fingerPrintWindow[index] {
			matches -= 1
		}

		index = s2[l] - 'a'
		fingerPrintWindow[index] -= 1
		if fingerPrintS1[index] == fingerPrintWindow[index] {
			matches += 1
		} else if fingerPrintS1[index]-1 == fingerPrintWindow[index] {
			matches -= 1
		}

		l += 1
	}

	// !!! Caution: remember to check result from last loop
	return matches == 26
}

// Great Python Solution
// For each window representing a substring of s2 of length len(s1), we want to check if the count of the window is equal to the count of s1. Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]
// We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). After, we only need to check if it is equal to the target. Working with list values of [0, 1,..., 25] instead of 'a'-'z' makes it easier to count later.

// def checkInclusion(self, s1, s2):
//     A = [ord(x) - ord('a') for x in s1]
//     B = [ord(x) - ord('a') for x in s2]

//     target = [0] * 26
//     for x in A:
//         target[x] += 1

//     window = [0] * 26
//     for i, x in enumerate(B):
//         window[x] += 1
//         if i >= len(A):
//             window[B[i - len(A)]] -= 1
//         if window == target:
//             return True
//     return False
