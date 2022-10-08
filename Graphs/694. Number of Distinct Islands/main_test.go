package main

import "testing"

func Test_numDistinctIslands(t *testing.T) {
	type args struct {
		grid [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{grid: [][]int{
				{1, 1, 0, 0, 0},
				{1, 1, 0, 0, 0},
				{0, 0, 0, 1, 1},
				{0, 0, 0, 1, 1},
			}},
			want: 1,
		},
		{
			name: "test2",
			args: args{grid: [][]int{
				{1, 1, 0, 1, 1},
				{1, 0, 0, 0, 0},
				{0, 0, 0, 0, 1},
				{1, 1, 0, 1, 1},
			}},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numDistinctIslands(tt.args.grid); got != tt.want {
				t.Errorf("numDistinctIslands() = %v, want %v", got, tt.want)
			}
		})
	}
}
