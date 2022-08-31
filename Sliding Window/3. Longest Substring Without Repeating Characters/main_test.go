// https://leetcode.com/problems/longest-substring-without-repeating-characters/
package main

import "testing"

func Test_lengthOfLongestSubstring(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "ex.1",
			args: args{s: "abcabcbb"}, // abc
			want: 3,
		},
		{
			name: "ex.2",
			args: args{s: "bbbbb"}, // b
			want: 1,
		},
		{
			name: "ex.3",
			args: args{s: "pwwkew"}, // wke
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := lengthOfLongestSubstring(tt.args.s); got != tt.want {
				t.Errorf("lengthOfLongestSubstring() = %v, want %v", got, tt.want)
			}
		})
	}
}
