package main

import (
	"testing"
)

func Test_largestBSTSubtreeBruteForce(t *testing.T) {
	input1 := []int{10, 5, 15, 1, 8, -1, 7}
	root1 := &TreeNode{Val: input1[0]}
	root1.Left = &TreeNode{Val: input1[1]}
	root1.Right = &TreeNode{Val: input1[2]}
	root1.Left.Left = &TreeNode{Val: input1[3]}
	root1.Left.Right = &TreeNode{Val: input1[4]}
	root1.Right.Left = nil
	root1.Right.Right = &TreeNode{Val: input1[6]}

	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{root: root1},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestBSTSubtreeBruteForce(tt.args.root); got != tt.want {
				t.Errorf("largestBSTSubtreeBruteForce() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_largestBSTSubtree(t *testing.T) {
	input1 := []int{10, 5, 15, 1, 8, -1, 7}
	root1 := &TreeNode{Val: input1[0]}
	root1.Left = &TreeNode{Val: input1[1]}
	root1.Right = &TreeNode{Val: input1[2]}
	root1.Left.Left = &TreeNode{Val: input1[3]}
	root1.Left.Right = &TreeNode{Val: input1[4]}
	root1.Right.Left = nil
	root1.Right.Right = &TreeNode{Val: input1[6]}

	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{root: root1},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestBSTSubtree(tt.args.root); got != tt.want {
				t.Errorf("largestBSTSubtree() = %v, want %v", got, tt.want)
			}
		})
	}
}
