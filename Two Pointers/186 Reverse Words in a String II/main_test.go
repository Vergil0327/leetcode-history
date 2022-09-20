// https://leetcode.com/problems/reverse-words-in-a-string-ii/
package main

import (
	"reflect"
	"testing"
)

func Test_reverseWordsWithSpace(t *testing.T) {
	type args struct {
		s []string
	}
	tests := []struct {
		name string
		args args
	}{
		{
			name: "test",
			args: args{s: []string{"t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			want := []string{"b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"}
			if got := reverseWordsWithSpace(tt.args.s); !reflect.DeepEqual(got, want) {
				t.Errorf("reverseWordsWithSpace want %v, got %v", want, got)
			}
		})
	}
}

func Test_reverseWordsOptimized(t *testing.T) {
	type args struct {
		s []string
	}
	tests := []struct {
		name string
		args args
	}{
		{
			name: "test",
			args: args{s: []string{"t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			reverseWordsOptimized(tt.args.s)
			t.Error("check fmt.Println answer")
		})
	}
}
