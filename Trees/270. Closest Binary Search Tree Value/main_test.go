package main

import "testing"

func Test_closestValue(t *testing.T) {
	root1 := &TreeNode{
		Val:   4,
		Left:  &TreeNode{Val: 2, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 3}},
		Right: &TreeNode{Val: 5},
	}

	type args struct {
		root   *TreeNode
		target float64
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test1",
			args: args{
				root:   root1,
				target: 3.714286,
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := closestValue(tt.args.root, tt.args.target); got != tt.want {
				t.Errorf("closestValue() = %v, want %v", got, tt.want)
			}
		})
	}
}
