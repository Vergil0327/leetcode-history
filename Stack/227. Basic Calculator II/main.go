// https://leetcode.com/problems/basic-calculator-ii/
package main

import (
	"bytes"
	"regexp"
	"strconv"
)

func calculateConcise(s string) int {
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

	var operation byte = '+'
	stack := []int{}
	num := 0
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			num = 10*num + int(s[i]-'0')
		}

		if i == len(s)-1 || !(s[i] >= '0' && s[i] <= '9') {
			switch operation {
			case '*':
				stack[len(stack)-1] *= num
			case '/':
				stack[len(stack)-1] /= num
			case '-':
				stack = append(stack, -num)
			default:
				stack = append(stack, num)
			}
			operation = s[i]
			num = 0
		}

	}

	sum := 0
	for _, v := range stack {
		sum += v
	}

	return sum
}

// T:O(n)
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

	// caluculate * & / and push positive or negative value into `values` array
	values := []int{}
	numericRegex := regexp.MustCompile(`[0-9]`)
	opRegex := regexp.MustCompile(`[\+\-\*\/]`)
	numStr := bytes.NewBufferString("")
	op := bytes.NewBufferString("")
	i := 0
	for i < len(s) {
		if numMatched := numericRegex.MatchString(string(s[i])); numMatched {
			numStr.WriteByte(s[i])
			i += 1
		} else if matchedOps := opRegex.MatchString(string(s[i])); matchedOps {
			switch s[i] {
			case '+':
				fallthrough
			case '-':
				if numStr.String() == "" {
					op.Reset()
					op.WriteByte(s[i])
					i += 1
					continue
				}

				num, _ := strconv.Atoi(numStr.String())
				numStr.Reset()

				if op.String() == "-" {
					values = append(values, -num)
				} else {
					values = append(values, num)
				}
				op.Reset()
				op.WriteByte(s[i])
				i += 1
			case '*':
				var l int
				if numStr.String() != "" {
					l, _ = strconv.Atoi(numStr.String())
					numStr.Reset()
				} else {
					l = values[len(values)-1]
					values = values[:len(values)-1]
				}

				i += 1
				for i < len(s) && numericRegex.MatchString(string(s[i])) {
					numStr.WriteByte(s[i])
					i += 1
				}
				r, _ := strconv.Atoi(numStr.String())
				numStr.Reset()

				if op.String() == "-" {
					values = append(values, -l*r)
				} else {
					values = append(values, l*r)
				}
				op.Reset()
			case '/':
				var l int
				if numStr.String() != "" {
					l, _ = strconv.Atoi(numStr.String())
					numStr.Reset()
				} else {
					l = values[len(values)-1]
					values = values[:len(values)-1]
				}

				i += 1
				for i < len(s) && numericRegex.MatchString(string(s[i])) {
					numStr.WriteByte(s[i])
					i += 1
				}
				r, _ := strconv.Atoi(numStr.String())
				numStr.Reset()

				if op.String() == "-" {
					values = append(values, -l/r)
				} else {
					values = append(values, l/r)
				}
				op.Reset()
			}
		}
	}
	if numStr.String() != "" {
		num, _ := strconv.Atoi(numStr.String())
		numStr.Reset()
		if op.String() == "-" {
			values = append(values, -num)
		} else {
			values = append(values, num)
		}
		op.Reset()
	}

	sum := 0
	for _, v := range values {
		sum += v
	}

	return sum
}
