// https://leetcode.com/problems/regular-expression-matching/

package main

import "testing"

func Test_isMatch(t *testing.T) {
	type args struct {
		s string
		p string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "aa a",
			args: args{
				s: "aa",
				p: "a",
			},
			want: false,
		},
		{
			name: "aa a*",
			args: args{
				s: "aa",
				p: "a*",
			},
			want: true,
		},
		{
			name: "aa .*",
			args: args{
				s: "aa",
				p: ".*",
			},
			want: true,
		},
		{
			name: "test1",
			args: args{
				s: "aaa",
				p: "ab*a*c*a",
			},
			want: true,
		},
		{
			name: "test2",
			args: args{
				s: "a",
				p: ".*..a*",
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isMatch(tt.args.s, tt.args.p); got != tt.want {
				t.Errorf("isMatch() = %v, want %v", got, tt.want)
			}
		})
	}
}
