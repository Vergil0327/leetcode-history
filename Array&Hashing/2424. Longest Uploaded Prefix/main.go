package main

type LUPrefix struct {
	maxIdx int
	list   []int
}

func Constructor(n int) LUPrefix {
	return LUPrefix{list: make([]int, n)}
}

func (this *LUPrefix) Upload(video int) {
	this.list[video-1] = 1
	for i := this.maxIdx; i < len(this.list); i++ {
		if this.list[i] == 1 {
			this.maxIdx = i
		} else {
			break
		}
	}
}

func (this *LUPrefix) Longest() int {
	if this.list[0] == 1 {
		return this.maxIdx + 1
	} else {
		return 0
	}
}

/**
* Your LUPrefix object will be instantiated and called as such:
* obj := Constructor(n);
* obj.Upload(video);
* param_2 := obj.Longest();
 */
