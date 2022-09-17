package main

import (
	"testing"
)

func Test_longestRepeatedSubstringBruteForce(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{s: "abcd"},
			want: 0,
		},
		{
			name: "test2",
			args: args{s: "abbaba"},
			want: 2,
		},
		{
			name: "test3",
			args: args{s: "aabcaabdaab"},
			want: 3,
		},
		{
			name: "test4",
			args: args{s: "aaaaa"},
			want: 4,
		},
		{
			name: "test5",
			args: args{s: "aabcaabdaabaabaab"}, // aabaab
			want: 6,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestRepeatedSubstringBruteForce(tt.args.s); got != tt.want {
				t.Errorf("longestRepeatedSubstring() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_longestRepeatedSubstring(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{s: "abcd"},
			want: 0,
		},
		{
			name: "test2",
			args: args{s: "abbaba"},
			want: 2,
		},
		{
			name: "test3",
			args: args{s: "aabcaabdaab"},
			want: 3,
		},
		{
			name: "test4",
			args: args{s: "aaaaa"},
			want: 4,
		},
		{
			name: "test5",
			args: args{s: "aabcaabdaabaabaab"}, // aabaab
			want: 6,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestRepeatedSubstring(tt.args.s); got != tt.want {
				t.Errorf("longestRepeatedSubstring() = %v, want %v", got, tt.want)
			}
		})
	}
}
