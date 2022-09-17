// https://leetcode.com/problems/count-days-spent-together/
package main

import (
	"strconv"
	"strings"
)

// https://leetcode.com/problems/count-days-spent-together/discuss/2587939/Stupid-Problem
// intuition by @Sagar_05: just convert every date to days and subtract the maximum of arrival from minimum leaving time.
// transform to 365 day instead of month with date
func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	aliceStart := strings.Split(arriveAlice, "-")
	aliceLeave := strings.Split(leaveAlice, "-")
	arriveMonthA, _ := strconv.ParseInt(aliceStart[0], 10, 64)
	arriveDateA, _ := strconv.ParseInt(aliceStart[1], 10, 64)
	leaveMonthA, _ := strconv.ParseInt(aliceLeave[0], 10, 64)
	leaveDateA, _ := strconv.ParseInt(aliceLeave[1], 10, 64)

	arriveDaysA := getDays(int(arriveMonthA), int(arriveDateA))
	leaveDaysA := getDays(int(leaveMonthA), int(leaveDateA))

	bobStart := strings.Split(arriveBob, "-")
	bobLeave := strings.Split(leaveBob, "-")
	arriveMonthB, _ := strconv.ParseInt(bobStart[0], 10, 64)
	arriveDateB, _ := strconv.ParseInt(bobStart[1], 10, 64)
	leaveMonthB, _ := strconv.ParseInt(bobLeave[0], 10, 64)
	leaveDateB, _ := strconv.ParseInt(bobLeave[1], 10, 64)

	arriveDaysB := getDays(int(arriveMonthB), int(arriveDateB))
	leaveDaysB := getDays(int(leaveMonthB), int(leaveDateB))

	// check no overlapping
	if min(leaveDaysA, leaveDaysB) < max(arriveDaysA, arriveDaysB) {
		return 0
	}

	// return overlapping + 1
	return min(leaveDaysA, leaveDaysB) - max(arriveDaysA, arriveDaysB) + 1
}

func getDays(month, date int) int {
	mDays := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

	days := 0
	for i := 0; i < month-1; i++ {
		days += mDays[i]
	}
	days += date
	return days
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
