// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

package main

import (
	"fmt"
	"math"
)

/*
Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

Example 3:
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
*/

// triplets: [[4,5,2],[4,2,7],[5,8,6],[3,6,6],[4,5,2]]
// target: [4,5,7]
// Expected: true

// explanation: https://www.youtube.com/watch?v=kShkQLQZ9K4
// we can only consider possible triplets
func mergeTripletsWithSet(triplets [][]int, target []int) bool {
	check := map[string]interface{}{}

	for _, triplet := range triplets {
		if triplet[0] > target[0] || triplet[1] > target[1] || triplet[2] > target[2] {
			continue
		}

		// 根本不需要MaxInt, 因為target就是最大值
		// 所以只要看最後湊不湊得出target即可
		for i, v := range triplet {
			if v == target[i] {
				// ! be careful of duplicate value in triplets
				// example: [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]
				// if we directly use v as key, we'll get map{5} in the end instead of map{5, 5, 5} (hashmap will remove duplicate key)
				// or maybe we use array & append value instead
				key := fmt.Sprintf("%d,%d", v, i)
				check[key] = struct{}{}
			}
		}
	}

	return len(check) == 3
}

// triplets任一數值超過target即不符合
// T:O(n)
func mergeTriplets(triplets [][]int, target []int) bool {
	ti, tj, tk := target[0], target[1], target[2]
	check := make([]int, len(triplets[0]))

	for _, triplet := range triplets {
		if check[0] == ti && check[1] == tj && check[2] == tk {
			return true
		}

		i, j, k := triplet[0], triplet[1], triplet[2]

		if i == ti {
			if check[0] != i && j <= tj && k <= tk {
				check[0] = MaxInt(check[0], i)
				check[1] = MaxInt(check[1], j)
				check[2] = MaxInt(check[2], k)
			}
		}
		if j == tj {
			if check[1] != j && i <= ti && k <= tk {
				check[0] = MaxInt(check[0], i)
				check[1] = MaxInt(check[1], j)
				check[2] = MaxInt(check[2], k)
			}
		}
		if k == tk {
			if check[2] != k && i <= ti && j <= tj {
				check[0] = MaxInt(check[0], i)
				check[1] = MaxInt(check[1], j)
				check[2] = MaxInt(check[2], k)
			}
		}
	}

	if check[0] == ti && check[1] == tj && check[2] == tk {
		return true
	}
	return false
}

func MaxInt(i, j int) int {
	return int(math.Max(float64(i), float64(j)))
}
