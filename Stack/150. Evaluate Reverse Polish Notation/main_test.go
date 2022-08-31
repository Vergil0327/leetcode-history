// https://leetcode.com/problems/evaluate-reverse-polish-notation/
package main

import "testing"

func Test_evalRPN(t *testing.T) {
	type args struct {
		tokens []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{tokens: []string{"2", "1", "+", "3", "*"}},
			want: 9,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := evalRPN(tt.args.tokens); got != tt.want {
				t.Errorf("evalRPN() = %v, want %v", got, tt.want)
			}
		})
	}
}
