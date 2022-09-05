// https://leetcode.com/problems/sum-of-two-integers/

package main

/*
a: 3, b: 5
011 101 -> 1000
 a = (a & b) << 1 = 001 << 1 = 010
 b = a ^ b = 110

XOR can get value that don't generate carry
AND can know where the carry from

looks like we need recursive bitwise ops

let's continue above example
	a = (010 & 110) << 1 = 010 << 1 = 100
	b = 010 ^ 110 = 100

	a = (100 & 100) << 1 = 1000
	b = 100 ^ 100 = 000

Bitwise AND :
	0011 & 0101	0001
Bitwise OR :
	0011 | 0101	0111
Bitwise XOR :
	0011 ^ 0101	0110
Bitwise NOT (same as 1111 ^ 0101) :
	^0101	1010
Bitclear (AND NOT):
	0011 &^ 0101	0010
Left shift:
	00110101<<2	11010100
No upper limit on shift count:
	00110101<<100	00000000
Right shift:
	00110101>>2	00001101
*/

func getSum(a int, b int) int {
	if a == 0 {
		return b
	}

	if b == 0 {
		return a
	}

	a, b = (a&b)<<1, a^b
	if b == 0 {
		return a
	}

	return getSum(a, b)
}
