package main

import (
	"reflect"
	"testing"
)

func Test_expand(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{
			name: "test1",
			args: args{
				s: "{a,b}c{d,e}f",
			},
			want: []string{"acdf", "acef", "bcdf", "bcef"},
		},
		{
			name: "test2",
			args: args{
				s: "abcd",
			},
			want: []string{"abcd"},
		},
		{
			name: "test3",
			args: args{
				s: "a",
			},
			want: []string{"a"},
		},
		{
			name: "test4",
			args: args{
				s: "",
			},
			want: nil,
		},
		{
			name: "test5",
			args: args{
				s: "{a,b}c{d,e}f{a,b}",
			},
			want: []string{
				"acdfa",
				"acdfb",
				"acefa",
				"acefb",
				"bcdfa",
				"bcdfb",
				"bcefa",
				"bcefb",
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := expand(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("expand() = %v, want %v", got, tt.want)
			}
		})
	}
}
