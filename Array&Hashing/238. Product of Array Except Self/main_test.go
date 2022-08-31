package main

import (
	"reflect"
	"testing"
)

func Test_productExceptSelfBetter(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Test1",
			args: args{[]int{1, 2, 3, 4}},
			want: []int{24, 12, 8, 6},
		},
		{
			name: "Test2",
			args: args{[]int{-1, 1, 0, -3, 3}},
			want: []int{0, 0, 9, 0, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := productExceptSelfBetter(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("productExceptSelf() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_productExceptSelfBrutal(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Test1",
			args: args{[]int{1, 2, 3, 4}},
			want: []int{24, 12, 8, 6},
		},
		{
			name: "Test2",
			args: args{[]int{-1, 1, 0, -3, 3}},
			want: []int{0, 0, 9, 0, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := productExceptSelfBrutal(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("productExceptSelfBrutal() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_productExceptSelfBest(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Test1",
			args: args{[]int{1, 2, 3, 4}},
			want: []int{24, 12, 8, 6},
		},
		{
			name: "Test2",
			args: args{[]int{-1, 1, 0, -3, 3}},
			want: []int{0, 0, 9, 0, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := productExceptSelfBest(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("productExceptSelfBest() = %v, want %v", got, tt.want)
			}
		})
	}
}
