// https://leetcode.com/problems/container-with-most-water/
package main

import (
	"testing"
)

func Test_maxArea(t *testing.T) {
	type args struct {
		height []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{height: []int{1, 8, 6, 2, 5, 4, 8, 3, 7}},
			want: 49,
		},
		{
			name: "test2",
			args: args{height: []int{2, 3, 4, 5, 18, 17, 6}},
			want: 17,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxArea(tt.args.height); got != tt.want {
				t.Errorf("maxArea() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxAreaTwoPointer(t *testing.T) {
	type args struct {
		height []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{height: []int{1, 8, 6, 2, 5, 4, 8, 3, 7}},
			want: 49,
		},
		{
			name: "test2",
			args: args{height: []int{2, 3, 4, 5, 18, 17, 6}},
			want: 17,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxAreaTwoPointer(tt.args.height); got != tt.want {
				t.Errorf("maxAreaTwoPointer() = %v, want %v", got, tt.want)
			}
		})
	}
}
