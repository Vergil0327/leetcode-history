package main

// it's easy to missing edge case if we store every frequency and calculation
// instead, we can try brute force for removing one character at each iteration
// time complexity will be O(length(word)*(length(word)-1)) = O(n^2)

func equalFrequency(word string) bool {
	for i := range word {
		str := word[:i] + word[i+1:]

		freq := map[byte]int{}
		for j := 0; j < len(str); j++ {
			freq[str[j]] += 1
		}

		set := map[int]bool{}
		for _, f := range freq {
			set[f] = true
		}

		if len(set) == 1 {
			return true
		}
	}

	return false
}
