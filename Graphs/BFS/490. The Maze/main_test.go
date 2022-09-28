// https://www.cnblogs.com/grandyang/p/6381458.html

package main

import "testing"

func Test_maze(t *testing.T) {
	type args struct {
		maze        [][]int
		start       [2]int
		destination [2]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				maze: [][]int{
					{0, 0, 1, 0, 0},
					{0, 0, 0, 0, 0},
					{0, 0, 0, 1, 0},
					{1, 1, 0, 1, 1},
					{0, 0, 0, 0, 0},
				},
				start:       [2]int{0, 4},
				destination: [2]int{4, 4},
			},
			want: true,
		},
		{
			name: "test2",
			args: args{
				maze: [][]int{
					{0, 0, 1, 0, 0},
					{0, 0, 0, 0, 0},
					{0, 0, 0, 1, 0},
					{1, 1, 0, 1, 1},
					{0, 0, 0, 0, 0},
				},
				start:       [2]int{0, 4},
				destination: [2]int{3, 2},
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maze(tt.args.maze, tt.args.start, tt.args.destination); got != tt.want {
				t.Errorf("maze() = %v, want %v", got, tt.want)
			}
		})
	}
}
