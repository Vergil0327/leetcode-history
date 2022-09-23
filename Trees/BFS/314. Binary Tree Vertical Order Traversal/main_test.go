package main

import (
	"reflect"
	"testing"
)

func Test_verticalOrder(t *testing.T) {
	type args struct {
		root *TreeNode
	}

	// [3,9,20,null,null,15,7]
	root := &TreeNode{Val: 3}
	nodeL := &TreeNode{Val: 9}
	nodeR := &TreeNode{Val: 20}
	root.Left = nodeL
	root.Right = nodeR
	nodeRL := &TreeNode{Val: 15}
	nodeRR := &TreeNode{Val: 7}
	nodeR.Left = nodeRL
	nodeR.Right = nodeRR

	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "test1",
			args: args{root: root},
			want: [][]int{
				{9},
				{3, 15},
				{20},
				{7},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := verticalOrder(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("verticalOrder() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_verticalOrderDFS(t *testing.T) {
	type args struct {
		root *TreeNode
	}

	// [3,9,20,null,null,15,7]
	root := &TreeNode{Val: 3}
	nodeL := &TreeNode{Val: 9}
	nodeR := &TreeNode{Val: 20}
	root.Left = nodeL
	root.Right = nodeR
	nodeRL := &TreeNode{Val: 15}
	nodeRR := &TreeNode{Val: 7}
	nodeR.Left = nodeRL
	nodeR.Right = nodeRR

	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "test1",
			args: args{root: root},
			want: [][]int{
				{9},
				{3, 15},
				{20},
				{7},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := verticalOrderDFS(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("verticalOrderDFS() = %v, want %v", got, tt.want)
			}
		})
	}
}
