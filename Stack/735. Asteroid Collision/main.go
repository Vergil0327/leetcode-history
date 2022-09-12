// https://leetcode.com/problems/asteroid-collision/

package main

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
