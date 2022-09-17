package main

import (
	"testing"
)

func Test_missingElement(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{
				nums: []int{4, 7, 9, 10},
				k:    1,
			},
			want: 5,
		},
		{
			name: "test2",
			args: args{
				nums: []int{4, 7, 9, 10},
				k:    3,
			},
			want: 8,
		},
		{
			name: "test3",
			args: args{
				nums: []int{1, 2, 4},
				k:    3,
			},
			want: 6,
		},
		{
			name: "test3",
			args: args{
				nums: []int{1, 2, 4},
				k:    5,
			},
			want: 8,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := missingElement(tt.args.nums, tt.args.k); got != tt.want {
				t.Errorf("missingElement() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_missingElementByIndex(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{
				nums: []int{4, 7, 9, 10},
				k:    1,
			},
			want: 5,
		},
		{
			name: "test2",
			args: args{
				nums: []int{4, 7, 9, 10},
				k:    3,
			},
			want: 8,
		},
		{
			name: "test3",
			args: args{
				nums: []int{1, 2, 4},
				k:    3,
			},
			want: 6,
		},
		{
			name: "test3",
			args: args{
				nums: []int{1, 2, 4},
				k:    5,
			},
			want: 8,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := missingElementByIndex(tt.args.nums, tt.args.k); got != tt.want {
				t.Errorf("missingElementByIndex() = %v, want %v", got, tt.want)
			}
		})
	}
}
