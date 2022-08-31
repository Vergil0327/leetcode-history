package main

import (
	"testing"
)

func Test_isPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "aba"},
			want: true,
		},
		{
			name: "test2",
			args: args{s: "abcba"},
			want: true,
		},
		{
			name: "test3",
			args: args{s: "abcca"},
			want: false,
		},
		{
			name: "test4",
			args: args{s: "A man, a plan, a canal: Panama"},
			want: true,
		},
		{
			name: "test5",
			args: args{s: "race a car"},
			want: false,
		},
		{
			name: "test5",
			args: args{s: "0P"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.s); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPalindromeBetter(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "aba"},
			want: true,
		},
		{
			name: "test2",
			args: args{s: "abcba"},
			want: true,
		},
		{
			name: "test3",
			args: args{s: "abcca"},
			want: false,
		},
		{
			name: "test4",
			args: args{s: "A man, a plan, a canal: Panama"},
			want: true,
		},
		{
			name: "test5",
			args: args{s: "race a car"},
			want: false,
		},
		{
			name: "test5",
			args: args{s: "0P"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindromeBetter(tt.args.s); got != tt.want {
				t.Errorf("isPalindromeBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
