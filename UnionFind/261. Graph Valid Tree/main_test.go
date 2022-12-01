// subscribe to UNLOCK
// https://jettlee.gitbooks.io/leetcode/content/261-graph-valid-tree.html
package main

import "testing"

func Test_graphValidTree(t *testing.T) {
	type args struct {
		edges [][]int
		n     int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "case1",
			args: args{n: 5, edges: [][]int{{0, 1}, {0, 2}, {0, 3}, {1, 4}}},
			want: true,
		},
		{
			name: "case2",
			args: args{n: 5, edges: [][]int{{0, 1}, {1, 2}, {2, 3}, {1, 3}, {1, 4}}},
			want: false,
		},
		{
			name: "case3",
			args: args{n: 6, edges: [][]int{{0, 1}, {0, 2}, {0, 3}, {4, 5}}},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := graphValidTree(tt.args.edges, tt.args.n); got != tt.want {
				t.Errorf("graphValidTree() = %v, want %v", got, tt.want)
			}
		})
	}
}
