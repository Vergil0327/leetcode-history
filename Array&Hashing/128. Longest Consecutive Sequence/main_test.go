package main

import (
	"testing"
)

func Test_longestConsecutive(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{nums: []int{100, 4, 200, 1, 3, 2}},
			want: 4, // Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
		},
		{
			name: "test2",
			args: args{nums: []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}},
			want: 9,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestConsecutive(tt.args.nums); got != tt.want {
				t.Errorf("longestConsecutive() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_longestConsecutiveBetter(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{nums: []int{100, 4, 200, 1, 3, 2}},
			want: 4, // Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
		},
		{
			name: "test2",
			args: args{nums: []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}},
			want: 9,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestConsecutiveBetter(tt.args.nums); got != tt.want {
				t.Errorf("longestConsecutiveBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
