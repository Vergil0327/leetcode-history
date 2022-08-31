package main

import (
	"testing"
)

func TestSolutionsWithSorting(t *testing.T) {
	type args struct {
		intervals [][2]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{intervals: [][2]int{
				{0, 30}, {5, 10}, {15, 20},
			}},
			want: false,
		},
		{
			name: "test2",
			args: args{intervals: [][2]int{
				{7, 10}, {2, 4},
			}},
			want: true,
		},
		{
			name: "test3",
			args: args{intervals: [][2]int{
				{7, 10}, {10, 15}, {25, 40},
			}},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SolutionsWithSorting(tt.args.intervals); got != tt.want {
				t.Errorf("SolutionsWithSorting() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSolutionsWithWithoutSorting(t *testing.T) {
	type args struct {
		intervals [][2]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{intervals: [][2]int{
				{0, 30}, {5, 10}, {15, 20},
			}},
			want: false,
		},
		{
			name: "test2",
			args: args{intervals: [][2]int{
				{7, 10}, {2, 4},
			}},
			want: true,
		},
		{
			name: "test3",
			args: args{intervals: [][2]int{
				{7, 10}, {10, 15}, {25, 40},
			}},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SolutionsWithWithoutSorting(tt.args.intervals); got != tt.want {
				t.Errorf("SolutionsWithWithoutSorting() = %v, want %v", got, tt.want)
			}
		})
	}
}
