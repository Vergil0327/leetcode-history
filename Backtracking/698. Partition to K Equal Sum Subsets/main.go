package main

import (
	"math"
	"sort"
)

func canPartitionKSubsets(nums []int, k int) bool {
	if k == 1 {
		return true
	}
	sum := 0
	max := 0
	for _, v := range nums {
		sum += v
		if v > max {
			max = v
		}
	}

	// !important
	// if we got num which is greater than sum/k, we'll never get valid subset
	if sum%k != 0 || max > sum/k {
		return false
	}

	// be greedy, take largest num first
	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })

	// visited := map[int]bool{}
	visited := make([]bool, len(nums)) // it's more efficient to use array rather than hashmap

	var dfs func(nums []int, visited []bool, start, sum, k, target int) bool
	dfs = func(nums []int, visited []bool, start, sum, k, target int) bool {
		if k == 1 {
			return true
		}

		if sum == target {
			return dfs(nums, visited, 0, 0, k-1, target)
		}

		for i := start; i < len(nums); i++ {
			if visited[i] || sum+nums[i] > target {
				continue
			}

			visited[i] = true
			// since we've already sort the nums, num before i+1 should be invalid (it'll make next round of nums[i]+sum > target)
			if dfs(nums, visited, i+1, nums[i]+sum, k, target) {
				return true
			}
			visited[i] = false
		}
		return false
	}
	return dfs(nums, visited, 0, 0, k, sum/k)
}

// brute force
func canPartitionKSubsetsTLE(nums []int, k int) bool {
	total := 0
	max := math.MinInt
	for _, num := range nums {
		total += num
		if num > max {
			max = num
		}
	}
	target := total / k

	// ! if we got number which is greater than target, we'll never partition correctly
	if total%k != 0 || max > target {
		return false
	}

	// be greedy, take largest num first
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	visited := map[int]bool{}
	return dfs(nums, 0, 0, k, visited, target)
}

func dfs(nums []int, state int, i int, k int, visited map[int]bool, target int) bool {
	if k == 1 {
		return true
	}

	if state == target {
		return dfs(nums, 0, 0, k-1, visited, target)
	}

	for j := i; j < len(nums); j++ {
		if visited[j] {
			continue
		}
		if state+nums[j] > target {
			continue
		}

		visited[j] = true
		if dfs(nums, state+nums[j], i+1, k, visited, target) {
			return true
		}
		visited[j] = false
	}

	return false
}
