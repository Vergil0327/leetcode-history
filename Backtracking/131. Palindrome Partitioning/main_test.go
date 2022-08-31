// https://leetcode.com/problems/palindrome-partitioning/
package main

import (
	"testing"
)

func Test_checkPalindrome(t *testing.T) {
	type args struct {
		s string
		l int
		r int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "aba", l: 0, r: 2},
			want: true,
		},
		{
			name: "test2",
			args: args{s: "aaa", l: 0, r: 2},
			want: true,
		},
		{
			name: "test1",
			args: args{s: "baa", l: 0, r: 2},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := checkPalindrome(tt.args.s, tt.args.l, tt.args.r); got != tt.want {
				t.Errorf("checkPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
