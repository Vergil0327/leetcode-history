package main

import (
	"testing"
)

func Test_isValidPalindrome(t *testing.T) {
	type args struct {
		s string
		k int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				s: "abcdeca",
				k: 2,
			},
			want: true,
		},
		{
			name: "test2",
			args: args{
				s: "abcdeca",
				k: 1,
			},
			want: false,
		},
		{
			name: "test3",
			args: args{
				s: "aaaaaaaaaaaaaaaaaaaaabcdecaaaaaaaaaaaaaaaaaaaaa",
				k: 2,
			},
			want: true,
		},
		{
			name: "test4",
			args: args{
				s: "bbbbbbbbbbbbbbbbbbbbcaaaaaaaaaaaaaaaaaaaaabcdecaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb",
				k: 3,
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValidPalindrome(tt.args.s, tt.args.k); got != tt.want {
				t.Errorf("isValidPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isValidPalindromeBottomUp(t *testing.T) {
	type args struct {
		s string
		k int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				s: "abcdeca",
				k: 2,
			},
			want: true,
		},
		{
			name: "test2",
			args: args{
				s: "abcdeca",
				k: 1,
			},
			want: false,
		},
		{
			name: "test3",
			args: args{
				s: "aaaaaaaaaaaaaaaaaaaaabcdecaaaaaaaaaaaaaaaaaaaaa",
				k: 2,
			},
			want: true,
		},
		{
			name: "test4",
			args: args{
				s: "bbbbbbbbbbbbbbbbbbbbcaaaaaaaaaaaaaaaaaaaaabcdecaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb",
				k: 3,
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValidPalindromeBottomUp(tt.args.s, tt.args.k); got != tt.want {
				t.Errorf("isValidPalindromeBottomUp() = %v, want %v", got, tt.want)
			}
		})
	}
}
