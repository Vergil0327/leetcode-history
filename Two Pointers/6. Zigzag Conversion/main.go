// https://leetcode.com/problems/zigzag-conversion/
package main

import (
	"bytes"
	"strings"
)

// explanation: https://www.youtube.com/watch?v=Q2Tw6gcVEwc
// T:O(n) M:O(n)
func convertMathApporach(s string, numRows int) string {
	// ! base case
	if numRows == 1 {
		return s
	}

	/*
		Input: s = "PAYPALISHIRING", numRows = 4
		Output: "PINALSIGYAHRPI"
		Explanation:
		P     I    N
		A   L S  I G
		Y A   H R
		P     I
	*/
	str := bytes.NewBufferString("")
	increment := 2 * (numRows - 1)
	for r := 0; r < numRows; r++ {
		for i := r; i < len(s); i += increment {
			// first and last row
			str.WriteByte(s[i])

			// handle middle row
			inMiddleRow := r > 0 && r < numRows-1
			if idx := i + increment - 2*r; inMiddleRow && idx < len(s) {
				str.WriteByte(s[idx])
			}
		}
	}

	return str.String()
}

// T:O(n) M:O(n)
func convert(s string, numRows int) string {
	// !!! base case
	if numRows == 1 {
		return s
	}

	zigzag := make([][]string, numRows)
	for i := range zigzag {
		zigzag[i] = make([]string, 0)
	}

	i := 0
	j := 0
	for j < len(s) && i < numRows {
		zigzag[i] = append(zigzag[i], string(s[j]))
		i += 1
		j += 1

		if i == numRows {
			i = numRows - 1
			for j < len(s) && i > 0 {
				i -= 1
				zigzag[i] = append(zigzag[i], string(s[j]))
				j += 1
			}
			i = 1
		}
	}

	str := ""
	for _, strs := range zigzag {
		str += strings.Join(strs, "")
	}
	return str
}
