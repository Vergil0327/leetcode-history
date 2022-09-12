// https://leetcode.com/problems/asteroid-collision/

package main

// explanation: https://www.youtube.com/watch?v=LN7KjRszjk4&ab_channel=NeetCode
func asteroidCollisionNeetcode(asteroids []int) []int {
	stack := []int{}

	for _, ast := range asteroids {
		for len(stack) > 0 && ast < 0 && stack[len(stack)-1] > 0 {
			diff := ast + stack[len(stack)-1]
			if diff < 0 {
				stack = stack[:len(stack)-1]
			} else if diff > 0 {
				ast = 0
			} else {
				stack = stack[:len(stack)-1]
				ast = 0
			}
		}

		if ast != 0 {
			stack = append(stack, ast)
		}
	}

	return stack
}

func asteroidCollisionRefactor(asteroids []int) []int {
	stack := []int{}
	for _, ast := range asteroids {
		if ast < 0 {
			for len(stack) > 0 && stack[len(stack)-1] > 0 && stack[len(stack)-1]+ast < 0 {
				stack = stack[:len(stack)-1]
			}

			if len(stack) == 0 {
				stack = append(stack, ast)
				continue
			}

			if top := stack[len(stack)-1]; top+ast == 0 {
				stack = stack[:len(stack)-1]
			} else if top < 0 {
				stack = append(stack, ast)
			}
		} else {
			stack = append(stack, ast)
		}
	}

	return stack
}

func asteroidCollision(asteroids []int) []int {
	stack := []int{}
	for _, ast := range asteroids {
		if len(stack) > 0 && ast < 0 {
			for len(stack) > 0 && stack[len(stack)-1] > 0 && stack[len(stack)-1]+ast < 0 {
				stack = stack[:len(stack)-1]
			}

			if len(stack) > 0 {
				top := stack[len(stack)-1]
				if top+ast == 0 {
					stack = stack[:len(stack)-1]
				} else if top < 0 {
					stack = append(stack, ast)
				}
			} else {
				stack = append(stack, ast)
			}
		} else {
			stack = append(stack, ast)
		}
	}

	return stack
}
