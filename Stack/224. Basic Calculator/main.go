// https://leetcode.com/problems/basic-calculator/
package main

import (
	"bytes"
)

// turn +(1+2) to +1+2, -(1+2) to -1-2
func calculateConcise(s string) int {
	sign := []int{1}
	res := 0
	operation := 1
	for i := 0; i < len(s); {
		switch s[i] {
		case ' ':
			i++
		case '+':
			operation = sign[len(sign)-1]
			i++
		case '-':
			operation = -sign[len(sign)-1]
			i++
		case '(':
			sign = append(sign, operation)
			i++
		case ')':
			sign = sign[:len(sign)-1]
			i++
		default:
			num := 0
			for i < len(s) && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			res += operation * num
		}
	}
	return res
}

func calculate(s string) int {
	// remove space
	str := bytes.NewBufferString("")
	for _, c := range s {
		if c == ' ' {
			continue
		}
		str.WriteRune(c)
	}

	s = str.String()
	if s == "" {
		return 0
	}

	opStack := []byte{}
	stack := []int{}
	num := 0
	sum := 0
	var operation byte = '+'
	for i := 0; i < len(s); i++ {
		if i == len(s)-1 && s[i] >= '0' && s[i] <= '9' {
			num = num*10 + int(s[i]-'0')
			if operation == '-' {
				sum -= num
			} else {
				sum += num
			}
			continue
		}

		if s[i] >= '0' && s[i] <= '9' {
			num = num*10 + int(s[i]-'0')
		} else {
			switch s[i] {
			case '-':
				if operation == '-' {
					sum -= num
				} else {
					sum += num
				}
				operation = '-'
			case '(':
				stack = append(stack, sum)
				opStack = append(opStack, operation)
				sum = 0
				operation = '+'
			case ')':
				if operation == '-' {
					sum -= num
				} else {
					sum += num
				}

				operation := opStack[len(opStack)-1]
				opStack = opStack[:len(opStack)-1]
				if operation == '-' {
					sum = stack[len(stack)-1] - sum
					stack = stack[:len(stack)-1]
				} else {
					sum = stack[len(stack)-1] + sum
					stack = stack[:len(stack)-1]
				}
			default /* cover 5 & +5 */ :
				if operation == '-' {
					sum -= num
				} else {
					sum += num
				}
				operation = '+'
			}
			num = 0
		}
	}

	return sum
}
