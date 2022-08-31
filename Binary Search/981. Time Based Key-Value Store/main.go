// https://leetcode.com/problems/time-based-key-value-store/
package main

/*
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
*/

type Item struct {
	Timestamp int
	Value     string
}

type TimeMap struct {
	m map[string][]Item
}

func Constructor() TimeMap {
	return TimeMap{
		m: make(map[string][]Item),
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.m[key] = append(this.m[key], Item{Value: value, Timestamp: timestamp})

	// ! we don't need to sort it. it's timestamp! already sorted (see constraint)
	// sort.Slice(this.m[key], func(i, j int) bool {
	// 	return this.m[key][i].Timestamp < this.m[key][j].Timestamp
	// })
}

func (this *TimeMap) Get(key string, timestamp int) string {
	timeSlice := this.m[key]
	if len(timeSlice) < 1 {
		return ""
	}

	l, r := 0, len(timeSlice)-1
	for l < r {
		mid := r - (r-l)/2
		if timeSlice[mid].Timestamp == timestamp {
			return timeSlice[mid].Value
		}

		if timestamp > timeSlice[mid].Timestamp {
			l = mid
		} else {
			r = mid - 1
		}
	}

	if timestamp >= this.m[key][l].Timestamp {
		return this.m[key][l].Value
	} else {
		return ""
	}
}

// Solution: https://www.youtube.com/watch?v=fu2cD_6E8Hw
func (this *TimeMap) GetBetter(key string, timestamp int) string {
	result := "" // return "" if not found
	store := this.m[key]

	l, r := 0, len(store)-1

	for l <= r {
		mid := (l + r) / 2

		if store[mid].Timestamp <= timestamp /* valid case */ {
			result = store[mid].Value
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return result
}

// first try

type TimeMap1 struct {
	m map[int]string
	t map[string][]int
}

func Constructor1() TimeMap1 {
	return TimeMap1{
		m: make(map[int]string),
		t: make(map[string][]int),
	}
}

// T:O(nLogN)
func (this *TimeMap1) Set1(key string, value string, timestamp int) {
	this.m[timestamp] = value
	this.t[key] = append(this.t[key], timestamp)

	// ! we don't need to sort it. it's timestamp! already sorted (see constraint)
	// sort.Slice(this.t[key], func(i, j int) bool {
	// 	return this.t[key][i] < this.t[key][j]
	// })
}

// T:O(n)
func (this *TimeMap1) Get1(key string, timestamp int) string {
	index := 0
	for i := len(this.t[key]) - 1; i >= 0; i-- {
		if this.t[key][i] <= timestamp {
			index = this.t[key][i]
			break
		}
	}

	return this.m[index]
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
