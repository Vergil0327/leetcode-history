package main

import (
	"reflect"
	"testing"
)

// func Test_array2tree(t *testing.T) {
// 	root1 := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
// 	type args struct {
// 		nums []int
// 	}
// 	tests := []struct {
// 		name string
// 		args args
// 		want *TreeNode
// 	}{
// 		{
// 			name: "test",
// 			args: args{nums: []int{1, 2, 3}},
// 			want: root1,
// 		},
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			if got := array2tree(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
// 				t.Errorf("array2tree() = %v, want %v", got, tt.want)
// 			}
// 		})
// 	}
// }

func Test_copyRandomBinaryTree(t *testing.T) {
	target := &TreeNode{Val: 1, Random: nil, Left: nil}
	l := &TreeNode{Val: 7, Random: target}
	target.Right = &TreeNode{Val: 4, Random: l, Left: l}

	want := &TreeNode{Val: 1, Random: nil, Left: nil}
	wantL := &TreeNode{Val: 7, Random: want}
	want.Right = &TreeNode{Val: 4, Random: wantL, Left: wantL}

	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		{
			name: "test1",
			args: args{root: target},
			want: want,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := copyRandomBinaryTree(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("copyRandomBinaryTree() = %v, want %v", got, tt.want)
			}
		})
	}
}
