// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
package main

import "math"

/*
01	001	0001
1		2			3

011	0111
2		3

0011 0101 1010 1100
3
00111 01011 10101 11010 11100
4
00011 00101 01010 10100 11000
4

101 1101 1011 10111
1    1    2    3

				100111110001000001
zeros   01223456666777777[10]

0後面有1, 一個零多一秒
每多一個1, 多一秒
0加在後面只要沒1就沒增加秒數
但只要有1, 所有的0都要移動 都得算進去
*/
// explanation: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/discuss/2454262/DP-vs.-Brute-Force
func secondsToRemoveOccurrences(s string) int {
	seconds := 0
	count0 := 0
	for _, ch := range s {
		if ch == '0' {
			count0 += 1
		}
		if ch == '1' && count0 > 0 {
			seconds = int(math.Max(float64(count0), float64(seconds+1)))
		}
	}

	return seconds
}
