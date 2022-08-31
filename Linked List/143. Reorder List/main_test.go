// https://leetcode.com/problems/reorder-list/
package main

import (
	"reflect"
	"testing"
)

func Test_reorderList(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		// {
		// 	name: "test1",
		// 	args: args{head: genLinkedList([]int{1, 2, 3, 4})},
		// 	want: genLinkedList([]int{1, 4, 2, 3}),
		// },
		{
			name: "test2",
			args: args{head: genLinkedList([]int{1, 2, 3, 4, 5})},
			want: genLinkedList([]int{1, 5, 2, 4, 3}),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			reorderList(tt.args.head)

			t.Errorf("test")
		})
	}
}

func Test_genLinkedList(t *testing.T) {
	type args struct {
		list []int
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := genLinkedList(tt.args.list); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("genLinkedList() = %v, want %v", got, tt.want)
			}
		})
	}
}
