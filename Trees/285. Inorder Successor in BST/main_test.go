package main

import (
	"reflect"
	"testing"
)

func Test_inorderSuccessor(t *testing.T) {
	// [2,1,3], p = 1
	root1 := &TreeNode{Val: 2, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 3}}

	// [5,3,6,2,4,null,null,1], p = 6
	root2 := &TreeNode{Val: 5}
	root2.Left = &TreeNode{Val: 3}
	root2.Right = &TreeNode{Val: 6}
	root2.Left.Left = &TreeNode{Val: 2}
	root2.Left.Right = &TreeNode{Val: 4}
	root2.Left.Left.Left = &TreeNode{Val: 1}

	type args struct {
		root *TreeNode
		p    *TreeNode
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		{
			name: "test1",
			args: args{
				root: root1,
				p:    root1.Left,
			},
			want: root1,
		},
		{
			name: "test2",
			args: args{
				root: root2,
				p:    root2.Right,
			},
			want: nil,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := inorderSuccessor(tt.args.root, tt.args.p); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("inorderSuccessor() = %v, want %v", got, tt.want)
			}
		})
	}
}
