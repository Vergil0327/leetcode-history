// https://leetcode.com/problems/find-in-mountain-array/
package main

/**
 * This is the MountainArray's API interface.
 * You should not implement it, or speculate about its implementation
 */
type MountainArray struct {
}

func (this *MountainArray) get(index int) int { return 0 }
func (this *MountainArray) length() int       { return 0 }

func findInMountainArray(target int, mountainArr *MountainArray) int {
	length := mountainArr.length()
	peak := findMountainPeak(mountainArr, length, 0, length-1)

	l, r := 0, peak
	for l <= r {
		mid := l + (r-l)/2
		current := mountainArr.get(mid)
		if target > current {
			l = mid + 1
		} else if target < current {
			r = mid - 1
		} else {
			return mid
		}
	}

	l, r = peak, length-1
	for l <= r {
		mid := l + (r-l)/2
		current := mountainArr.get(mid)
		if target < current {
			l = mid + 1
		} else if target > current {
			r = mid - 1
		} else {
			return mid
		}
	}

	return -1
}

func findMountainPeak(mountainArr *MountainArray, mountainLen int, l, r int) (peak int) {
	for l < r {
		mid := l + (r-l)/2
		midL := mid - 1
		if midL < 0 {
			midL = mid
		}
		midR := mid + 1
		if midR >= mountainLen {
			midR = mid
		}

		vl, vm, vr := mountainArr.get(midL), mountainArr.get(mid), mountainArr.get(midR)
		if vl < vm && vm < vr {
			l = mid
		} else if vl > vm && vm > vr {
			r = mid
		} else {
			peak = mid
			break
		}
	}

	return
}
