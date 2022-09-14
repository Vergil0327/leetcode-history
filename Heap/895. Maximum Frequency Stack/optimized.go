package main

// explanation: https://www.youtube.com/watch?v=Z6idIicFDOE
type FreqStackBetter struct {
	maxFreq int
	stacks  map[int][]int // { freq: [val1, val2, ...] }
	freq    map[int]int   // { val: freq }
}

func BetterConstructor() FreqStackBetter {
	return FreqStackBetter{stacks: make(map[int][]int), freq: make(map[int]int)}
}

// T:O(1)
func (this *FreqStackBetter) Push(val int) {
	// update freq
	this.freq[val] += 1

	// check maxFreq
	if this.freq[val] > this.maxFreq {
		this.maxFreq = this.freq[val]
		this.stacks[this.freq[val]] = make([]int, 0)
	}

	// push to stacks
	this.stacks[this.freq[val]] = append(this.stacks[this.freq[val]], val)
}

// T:O(1)
func (this *FreqStackBetter) Pop() int {
	// pop max freq value
	val := this.stacks[this.maxFreq][len(this.stacks[this.maxFreq])-1]
	this.stacks[this.maxFreq] = this.stacks[this.maxFreq][:len(this.stacks[this.maxFreq])-1]

	// update freq
	this.freq[val] -= 1

	// check maxFreq
	if len(this.stacks[this.maxFreq]) == 0 {
		this.maxFreq -= 1
	}

	return val
}
