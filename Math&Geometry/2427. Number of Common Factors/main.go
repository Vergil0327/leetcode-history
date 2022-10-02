package main

func commonFactors(a int, b int) int {
	count := 0
	for i := 1; i <= min(a, b); i++ {
		if a%i == 0 && b%i == 0 {
			count += 1
		}
	}

	return count
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
