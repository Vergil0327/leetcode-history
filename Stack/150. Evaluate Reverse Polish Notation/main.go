// https://leetcode.com/problems/evaluate-reverse-polish-notation/
package main

import (
	"strconv"
)

// Evaluate the value of an arithmetic expression in Reverse Polish Notation.

// Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

// Note that division between two integers should truncate toward zero.

// It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

// Example 1:
// Input: tokens = ["2","1","+","3","*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9

// Example 2:
// Input: tokens = ["4","13","5","/","+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6

// Example 3:
// Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
// Output: 22
// Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
// = ((10 * (6 / (12 * -11))) + 17) + 5
// = ((10 * (6 / -132)) + 17) + 5
// = ((10 * 0) + 17) + 5
// = (0 + 17) + 5
// = 17 + 5
// = 22

func popStackItem(stack *[]int) int {
	endIdx := len(*stack) - 1
	item := (*stack)[endIdx]
	*stack = (*stack)[:endIdx]
	return item
}

// T:O(n)
func evalRPN(tokens []string) int {
	// !!! Edge Case
	if len(tokens) == 1 {
		num, _ := strconv.ParseInt(tokens[0], 10, 64)
		return int(num)
	}

	answer := 0
	stack := []int{}

	for _, token := range tokens {
		if token != "+" && token != "-" && token != "*" && token != "/" {
			num, _ := strconv.ParseInt(token, 10, 32)
			stack = append(stack, int(num))
			continue
		}

		switch token {
		case "+":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			result := l + r
			answer = result
			stack = append(stack, result)
		case "-":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			result := l - r
			answer = result
			stack = append(stack, result)
		case "*":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			result := l * r
			answer = result
			stack = append(stack, result)
		case "/":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			result := l / r
			answer = result
			stack = append(stack, result)
		}
	}
	return answer
}

func evalRPNBetter(tokens []string) int {
	// answer := 0 // ! redundant variable
	stack := []int{}

	for _, token := range tokens {
		if token != "+" && token != "-" && token != "*" && token != "/" {
			num, _ := strconv.ParseInt(token, 10, 32)
			stack = append(stack, int(num))
			continue
		}

		switch token {
		case "+":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			// answer = result
			stack = append(stack, l+r)
		case "-":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			// answer = result
			stack = append(stack, l-r)
		case "*":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			// answer = result
			stack = append(stack, l*r)
		case "/":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			// answer = result
			stack = append(stack, l/r)
		}
	}
	return stack[0]
}

func evalRPNEvenBetter(tokens []string) int {
	stack := []int{}

	for _, token := range tokens {
		switch token {
		case "+":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			stack = append(stack, l+r)
		case "-":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			stack = append(stack, l-r)
		case "*":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			stack = append(stack, l*r)
		case "/":
			r := popStackItem(&stack)
			l := popStackItem(&stack)
			stack = append(stack, l/r)
		default:
			num, _ := strconv.ParseInt(token, 10, 32)
			stack = append(stack, int(num))
		}
	}
	return stack[0]
}
