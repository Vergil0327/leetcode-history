package main

import (
	"math"
	"testing"
)

func Test_findMaxAverageSubarray(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want float64
	}{
		{
			name: "test1",
			args: args{
				nums: []int{1, 12, -5, -6, 50, 3},
				k:    4,
			},
			want: 12.75,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMaxAverageSubarray(tt.args.nums, tt.args.k); got != tt.want {
				t.Errorf("findMaxAverageSubarray() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_findMaxAverageSubarrayBinSearch(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want float64
	}{
		{
			name: "test1",
			args: args{
				nums: []int{1, 12, -5, -6, 50, 3},
				k:    4,
			},
			want: 12.75,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMaxAverageSubarrayBinSearch(tt.args.nums, tt.args.k); !(math.Abs(got-tt.want) < math.Pow10(-5)) {
				t.Errorf("findMaxAverageSubarrayBinSearch() = %v, want %v", got, tt.want)
			}
		})
	}
}
