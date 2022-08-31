// https://leetcode.com/problems/generate-parentheses/
package main

import (
	"reflect"
	"testing"
)

func Test_generateParenthesis(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{
			name: "test1",
			args: args{n: 1},
			want: []string{"()"},
		},
		{
			name: "test2",
			args: args{n: 2},
			want: []string{"(())", "()()"},
		},
		{
			name: "test3",
			args: args{n: 3},
			want: []string{"((()))", "(()())", "(())()", "()(())", "()()()"},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := generateParenthesis(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("generateParenthesis() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_generateParenthesis2(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{
			name: "test1",
			args: args{n: 1},
			want: []string{"()"},
		},
		{
			name: "test2",
			args: args{n: 2},
			want: []string{"(())", "()()"},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := generateParenthesis2(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("generateParenthesis2() = %v, want %v", got, tt.want)
			}
		})
	}
}
