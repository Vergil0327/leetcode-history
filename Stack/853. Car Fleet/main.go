// https://leetcode.com/problems/car-fleet/
package main

import (
	"sort"
)

/* There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination. */

// Example 1:

// Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
// Output: 3
// Explanation:
// The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
// The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
// The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
// Note that no other cars meet these fleets before the destination, so the answer is 3.

// Example 2:
// Input: target = 10, position = [3], speed = [3]
// Output: 1
// Explanation: There is only one car, hence there is only one fleet.

// Example 3:
// Input: target = 100, position = [0,2,4], speed = [4,2,1]
// Output: 1
// Explanation:
// The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
// Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

// Constraints:

// n == position.length == speed.length
// 1 <= n <= 105
// 0 < target <= 106
// 0 <= position[i] < target
// All the values of position are unique.
// 0 < speed[i] <= 106

type Car struct {
	Pos, Speed int
}

func carFleet(target int, position []int, speed []int) int {
	cars := []Car{}
	for i, pos := range position {
		cars = append(cars, Car{Pos: pos, Speed: speed[i]})
	}

	// sort in position
	sort.Slice(cars, func(i, j int) bool {
		return cars[i].Pos < cars[j].Pos
	})

	requiredTime := []float32{}
	for i := len(cars) - 1; i >= 0; i-- {
		// !!! use float32 because time can be decimal value
		t := float32(target-cars[i].Pos) / float32(cars[i].Speed)
		if len(requiredTime) == 0 ||
			(len(requiredTime) > 0 && t > requiredTime[len(requiredTime)-1]) {
			requiredTime = append(requiredTime, t)
		}
	}

	return len(requiredTime)
}

// https://www.youtube.com/watch?v=Pr6T-3yB9RM
// T:O(nLonN) because of sorting M:O(n)
func carFleetBetter(target int, position []int, speed []int) int {
	cars := []Car{}
	for i, pos := range position {
		cars = append(cars, Car{Pos: pos, Speed: speed[i]})
	}

	// sort by position in Descending order
	// we check if car collides into car fleet from the farthest car
	sort.Slice(cars, func(i, j int) bool {
		return cars[i].Pos > cars[j].Pos
	})

	stack := []float32{}
	for _, car := range cars {
		t := float32(target-car.Pos) / float32(car.Speed)
		stack = append(stack, t)
		if len(stack) >= 2 && stack[len(stack)-1] <= stack[len(stack)-2] /* means car collision */ {
			stack = stack[:len(stack)-1] // pop from stack
		}
	}

	return len(stack)
}

// Disscussion
// Sort the vehicles by the (pos, vel) pair.
// Since the first vehicle will always lead a fleet, starting from the second vehicle, compare each vehicle's ideal arrival time with the arrival time of the fleet in front of it, i.e., stack[-1]. If its ideal arrival time is earlier, it will join the fleet in front of it. Otherwise, it will lead a new fleet and we append its arrival time into stack.
// Finally, stack contains the arrival times of the fleets and the length of stack will be the number of distinct arrival times, i.e., the number of fleets.
// class Solution:
//     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
//         stack = []
//         for pos, vel in sorted(zip(position, speed))[::-1]:
//             dist = target - pos
//             if not stack:
//                 stack.append(dist / vel)
//             elif dist / vel > stack[-1]:
//                 stack.append(dist / vel)
//         return len(stack)
