package main

import (
	"testing"
)

func Test_maxDepthRecursion(t *testing.T) {
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
			args: args{root: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDepthRecursion(tt.args.root); got != tt.want {
				t.Errorf("maxDepthRecursion() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxDepthBFS(t *testing.T) {
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
			args: args{root: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDepthBFS(tt.args.root); got != tt.want {
				t.Errorf("maxDepthQueue() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxDepthDFS(t *testing.T) {
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
			args: args{root: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDepthDFS(tt.args.root); got != tt.want {
				t.Errorf("maxDepthDFS() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxDepthDFSBetter(t *testing.T) {
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
			args: args{root: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDepthDFSBetter(tt.args.root); got != tt.want {
				t.Errorf("maxDepthDFSBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
