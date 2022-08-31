// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
// Subscribe to UNLOCK
package main

import (
	"testing"
)

func Test_solution(t *testing.T) {
	type args struct {
		edges [][]int
		n     int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{edges: [][]int{{0, 1}, {1, 2}, {3, 4}}, n: 5},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solution(tt.args.edges, tt.args.n); got != tt.want {
				t.Errorf("solution() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_numberOfConnectedComponentUnionFind(t *testing.T) {
	type args struct {
		edges [][]int
		n     int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{edges: [][]int{{0, 1}, {1, 2}, {3, 4}}, n: 5},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberOfConnectedComponentUnionFind(tt.args.edges, tt.args.n); got != tt.want {
				t.Errorf("numberOfConnectedComponentUnionFind() = %v, want %v", got, tt.want)
			}
		})
	}
}
