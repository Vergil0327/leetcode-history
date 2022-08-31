package main

import (
	"testing"
)

func Test_hasCycle(t *testing.T) {
	head1 := &ListNode{Val: 1, Next: nil}
	head2 := &ListNode{Val: 2, Next: head1}
	head1.Next = head2

	head4 := &ListNode{Val: 4, Next: nil}
	head5 := &ListNode{Val: 5, Next: nil}
	head6 := &ListNode{Val: 6, Next: nil}
	head4.Next = head5
	head5.Next = head6
	head6.Next = head5

	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test0",
			args: args{head: nil},
			want: false,
		},
		{
			name: "test1",
			args: args{head: head1},
			want: true,
		},
		{
			name: "test2",
			args: args{head: &ListNode{Val: 1, Next: nil}},
			want: false,
		},
		{
			name: "test3",
			args: args{head: head4},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasCycle(tt.args.head); got != tt.want {
				t.Errorf("hasCycle() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_hasCycleBetter(t *testing.T) {
	head1 := &ListNode{Val: 1, Next: nil}
	head2 := &ListNode{Val: 2, Next: head1}
	head1.Next = head2

	head4 := &ListNode{Val: 4, Next: nil}
	head5 := &ListNode{Val: 5, Next: nil}
	head6 := &ListNode{Val: 6, Next: nil}
	head4.Next = head5
	head5.Next = head6
	head6.Next = head5

	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test0",
			args: args{head: nil},
			want: false,
		},
		{
			name: "test1",
			args: args{head: head1},
			want: true,
		},
		{
			name: "test2",
			args: args{head: &ListNode{Val: 1, Next: nil}},
			want: false,
		},
		{
			name: "test3",
			args: args{head: head4},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasCycleBetter(tt.args.head); got != tt.want {
				t.Errorf("hasCycleBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
