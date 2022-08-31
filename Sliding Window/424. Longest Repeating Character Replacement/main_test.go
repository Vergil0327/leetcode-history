// https://leetcode.com/problems/longest-repeating-character-replacement/
package main

import (
	"testing"
)

func Test_characterReplacement(t *testing.T) {
	type args struct {
		s string
		k int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{s: "ABAB", k: 2},
			want: 4,
		},
		{
			name: "test2",
			args: args{s: "AABABBA", k: 1},
			want: 4,
		},
		{
			name: "test3",
			args: args{s: "AABCDEEE", k: 2},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := characterReplacement(tt.args.s, tt.args.k); got != tt.want {
				t.Errorf("characterReplacement() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getMaxCount(t *testing.T) {
	type args struct {
		contain map[byte]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getMaxCount(tt.args.contain); got != tt.want {
				t.Errorf("getMaxCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_characterReplacementBetter(t *testing.T) {
	type args struct {
		s string
		k int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{s: "ABAB", k: 2},
			want: 4,
		},
		{
			name: "test2",
			args: args{s: "AABABBA", k: 1},
			want: 4,
		},
		{
			name: "test3",
			args: args{s: "AABCDEEE", k: 2},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := characterReplacementBetter(tt.args.s, tt.args.k); got != tt.want {
				t.Errorf("characterReplacementBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
