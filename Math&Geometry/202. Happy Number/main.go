package main

import (
	"fmt"
	"math"
	"strconv"
)

func isHappy(n int) bool {
	seen := map[int]any{}
	return check(n, seen)
}

func check(n int, seen map[int]any) bool {
	// check if x belongs to a multiple of 10
	if x := math.Log10(float64(n)); x == math.Trunc(x) {
		return true
	}
	if _, isCycle := seen[n]; isCycle {
		return false
	}
	seen[n] = struct{}{}

	str := fmt.Sprint(n)
	var sum float64
	for _, r := range str {
		num, _ := strconv.ParseFloat(string(r), 64)
		sum += math.Pow(num, 2)
	}
	return check(int(sum), seen)
}

// Better

func isHappyBetter(n int) bool {
	seen := map[int]any{}
	return check(n, seen)
}

func checkBetter(n int, seen map[int]any) bool {
	if n == 1 {
		return true
	}
	if _, isCycle := seen[n]; isCycle {
		return false
	}
	seen[n] = struct{}{}

	str := fmt.Sprint(n)
	var sum float64
	for _, r := range str {
		num, _ := strconv.ParseFloat(string(r), 64)
		sum += math.Pow(num, 2)
	}
	return checkBetter(int(sum), seen)
}

// Other Solution

func isHappyBest(n int) bool {
	seen := make(map[int]bool)
	for n != 1 {
		n = getNext(n)
		if seen[n] {
			break
		}
		seen[n] = true
	}
	return n == 1
}

func getNext(n int) int {
	sum := 0
	for n > 0 {
		digit := n % 10
		n = n / 10
		sum += digit * digit
	}
	return sum
}
