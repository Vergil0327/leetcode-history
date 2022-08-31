// https://leetcode.com/problems/house-robber/
package main

import "testing"

func Test_rob(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "testcase1",
			args: args{nums: []int{1, 2, 3, 1}},
			want: 4,
		},

		{
			name: "testcase2",
			args: args{nums: []int{2, 7, 9, 3, 1}},
			want: 12,
		},

		{
			name: "testcase3",
			args: args{nums: []int{0}},
			want: 0,
		},

		{
			name: "testcase4",
			args: args{nums: []int{1, 1}},
			want: 1,
		},

		{
			name: "testcase5",
			args: args{nums: []int{1, 3, 1}},
			want: 3,
		},

		{
			name: "testcase6",
			args: args{nums: []int{2, 1, 1, 2}},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rob(tt.args.nums); got != tt.want {
				t.Errorf("rob() = %v, want %v", got, tt.want)
			}
		})
	}
}
