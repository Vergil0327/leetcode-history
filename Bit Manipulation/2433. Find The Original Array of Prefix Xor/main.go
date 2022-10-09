package main

// XOR:
// num ^ 0 = num
// 0 ^ num = num
// num ^ num = 0

// pref[0] = arr[0]
// pref[1] = arr[0] ^ arr[1] = pref[0] ^ arr[1]
// ==> pref[1] ^ pref[0] = pref[0] ^ pref[0] ^ arr[1] = 0 ^ arr[1]
// pref[2] = arr[0] ^ arr[1] ^ arr[2] = pref[1] ^ arr[2]
// ==> pref[2] ^ pref[1] = pref[1] ^ pref[1] ^ arr[2] = 0 ^ arr[2]

// pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
func findArray(pref []int) []int {
	res := make([]int, len(pref))

	for i := range pref {
		if i == 0 {
			res[i] = pref[i]
			continue
		}
		res[i] = pref[i] ^ pref[i-1]
	}

	return res
}
