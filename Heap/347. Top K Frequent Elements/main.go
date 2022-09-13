// https://leetcode.com/problems/top-k-frequent-elements/

package main

import "container/heap"

/*
Bucket Sort T:O(n)
Idea is simple. Build a array of list to be buckets with length 1 to sort.

public List<Integer> topKFrequent(int[] nums, int k) {

	List<Integer>[] bucket = new List[nums.length + 1];
	Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();

	for (int n : nums) {
		frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
	}

	for (int key : frequencyMap.keySet()) {
		int frequency = frequencyMap.get(key);
		if (bucket[frequency] == null) {
			bucket[frequency] = new ArrayList<>();
		}
		bucket[frequency].add(key);
	}

	List<Integer> res = new ArrayList<>();

	for (int pos = bucket.length - 1; pos >= 0 && res.size() < k; pos--) {
		if (bucket[pos] != null) {
			res.addAll(bucket[pos]);
		}
	}
	return res;
}
Thanks for sharing, only one nitpick:

Think about the case when K=2,
and you have 1 number that has max frequency, say 10 times.
and you have 10 numbers that has 2nd max frequency, say 9 times.
With your algo, the returned list will contain 11 numbers instead of 2.

Any easy fix:
return res.subList(0,k);

max frequency is length of nums
we use frequency as idx of bucket, so bucket length will be `len(nums)+1`
*/
func topKFrequentBucket(nums []int, k int) []int {
	bucket := make([][]int, len(nums)+1)

	freq := map[int]int{}
	for _, num := range nums {
		freq[num] += 1
	}

	for k, v := range freq {
		if bucket[v] == nil {
			bucket[v] = make([]int, 0)
		}
		bucket[v] = append(bucket[v], k)
	}

	topK := []int{}
	for i := len(bucket) - 1; i >= 0 && len(topK) < k; i-- {
		if len(bucket[i]) > 0 {
			topK = append(topK, bucket[i]...)
		}
	}

	return topK[:k]
}

// T:O(n) average, worst in n^2
func topKFrequentQuickSelect(nums []int, k int) []int {
	// T:O(n)
	freq := map[int]int{}
	for _, num := range nums {
		freq[num] += 1
	}

	// T:O(n)
	values := []int{}
	for num := range freq {
		values = append(values, num)
	}

	target := len(values) - k

	var quickselect func(l, r int) []int
	quickselect = func(l, r int) []int {
		pivot := values[r]
		p := l
		for i := l; i < r; i++ {
			if freq[values[i]] < freq[pivot] {
				values[i], values[p] = values[p], values[i]
				p += 1
			}
		}
		values[r], values[p] = values[p], values[r]

		if p == target {
			return values[p:]
		} else if p < target {
			return quickselect(p+1, r)
		} else {
			return quickselect(l, p-1)
		}
	}

	return quickselect(0, len(values)-1)
}

func topKFrequent(nums []int, k int) []int {
	// T:O(n)
	freq := map[int]int{}
	for _, num := range nums {
		freq[num] += 1
	}

	// T:O(n)
	values := [][]int{} // [val, freq]
	for num, f := range freq {
		values = append(values, []int{num, f})
	}

	// T:O(n)
	h := MaxHeap(values)
	heap.Init(&h)

	// T:O(klogn)
	res := []int{}
	for k > 0 {
		res = append(res, heap.Pop(&h).([]int)[0])
		k -= 1
	}

	return res
}

type MaxHeap [][]int // [val, freq]

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	return h[i][1] > h[j][1]
}
func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MaxHeap) Push(item interface{}) {
	*h = append(*h, item.([]int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

/*
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

`Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.`
*/
