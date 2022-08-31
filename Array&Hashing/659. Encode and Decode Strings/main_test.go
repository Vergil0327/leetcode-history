package main

import (
	"reflect"
	"testing"
)

func Test_encode(t *testing.T) {
	type args struct {
		list []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "test1",
			args: args{list: []string{"leet", "code", "is", "hard"}},
			want: "4#leet4#code2#is4#hard",
		},
		{
			name: "test2",
			args: args{list: []string{"leet", "co#e", "is", "hard"}},
			want: "4#leet4#co#e2#is4#hard",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := encode(tt.args.list); got != tt.want {
				t.Errorf("encode() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_decode(t *testing.T) {
	type args struct {
		list string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{
			name: "test1",
			args: args{"4#leet4#code2#is4#hard"},
			want: []string{"leet", "code", "is", "hard"},
		},
		{
			name: "test2",
			args: args{"4#leet4#co#e2#is4#hard"},
			want: []string{"leet", "co#e", "is", "hard"},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := decode(tt.args.list); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("decode() = %v, want %v", got, tt.want)
			}
		})
	}
}
