package main

import (
	"reflect"
	"testing"
)

func Test_findLeaves(t *testing.T) {
	root1 := &TreeNode{Val: 1}
	node2 := &TreeNode{Val: 2}
	node3 := &TreeNode{Val: 3}
	node4 := &TreeNode{Val: 4}
	node5 := &TreeNode{Val: 5}
	root1.Left = node2
	root1.Right = node3
	node2.Left = node4
	node2.Right = node5
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "test1",
			args: args{
				root: root1,
			},
			want: [][]int{{4, 5, 3}, {2}, {1}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findLeaves(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findLeaves() = %v, want %v", got, tt.want)
			}
		})
	}
}
