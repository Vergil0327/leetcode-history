// https://leetcode.com/problems/combination-sum/
package main

import (
	"reflect"
	"testing"
)

func Test_combinationSum(t *testing.T) {
	type args struct {
		candidates []int
		target     int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "test1",
			args: args{candidates: []int{2, 3, 6, 7}, target: 7},
			want: [][]int{{2, 2, 3}, {7}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := combinationSum(tt.args.candidates, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("combinationSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_combinationSum2(t *testing.T) {
	type args struct {
		candidates []int
		target     int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "test1",
			args: args{candidates: []int{2, 3, 6, 7}, target: 7},
			want: [][]int{{2, 2, 3}, {7}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := combinationSum2(tt.args.candidates, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("combinationSum2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_combinationSumSlow(t *testing.T) {
	type args struct {
		candidates []int
		target     int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := combinationSumSlow(tt.args.candidates, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("combinationSumSlow() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_checkIfStateValid(t *testing.T) {
	type args struct {
		state  []int
		target int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := checkIfStateValid(tt.args.state, tt.args.target); got != tt.want {
				t.Errorf("checkIfStateValid() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		state []int
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
			if got := sum(tt.args.state); got != tt.want {
				t.Errorf("sum() = %v, want %v", got, tt.want)
			}
		})
	}
}
