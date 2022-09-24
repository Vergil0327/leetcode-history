package main

import (
	"reflect"
	"testing"
)

func Test_numIslands(t *testing.T) {
	type args struct {
		m         int
		n         int
		positions [][]int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "test1",
			args: args{
				m:         3,
				n:         3,
				positions: [][]int{{0, 0}, {0, 1}, {1, 2}, {2, 1}},
			},
			want: []int{1, 1, 2, 3},
		},
		{
			name: "test2",
			args: args{
				m:         3,
				n:         3,
				positions: [][]int{{0, 0}, {0, 1}, {1, 2}, {2, 1}, {1, 1}},
			},
			want: []int{1, 1, 2, 3, 1},
		},
		{
			name: "test3",
			args: args{
				m:         3,
				n:         3,
				positions: [][]int{{0, 0}, {0, 1}, {1, 2}, {2, 1}, {2, 0}},
			},
			want: []int{1, 1, 2, 3, 3},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numIslands(tt.args.m, tt.args.n, tt.args.positions); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("numIslands() = %v, want %v", got, tt.want)
			}
		})
	}
}
