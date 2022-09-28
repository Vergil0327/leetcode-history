// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/alien-dictionary/
package main

import (
	"reflect"
	"testing"
)

func Test_alienOrder(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "ex1",
			args: args{words: []string{"wrt", "wrf", "er", "ett", "rftt"}},
			want: "wertf",
		},
		{
			name: "ex2",
			args: args{words: []string{"z", "x"}},
			want: "zx",
		},
		{
			name: "ex3",
			args: args{words: []string{"z", "x", "z"}},
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := AlienOrderBFS(tt.args.words); got != tt.want {
				t.Errorf("alienOrder() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlienOrderBFS(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "ex1",
			args: args{words: []string{"wrt", "wrf", "er", "ett", "rftt"}},
			want: "wertf",
		},
		{
			name: "ex2",
			args: args{words: []string{"z", "x"}},
			want: "zx",
		},
		{
			name: "ex3",
			args: args{words: []string{"z", "x", "z"}},
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := AlienOrderBFS(tt.args.words); got != tt.want {
				t.Errorf("AlienOrderBFS() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlienOrderDFS(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := AlienOrderDFS(tt.args.words); got != tt.want {
				t.Errorf("AlienOrderDFS() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_buildGraph(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want map[string][]string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := buildGraph(tt.args.words); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("buildGraph() = %v, want %v", got, tt.want)
			}
		})
	}
}
