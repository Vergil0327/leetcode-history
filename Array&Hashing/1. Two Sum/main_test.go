package main

import (
	"reflect"
	"testing"
)

func Test_twoSum(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// {
		// 	name: "test1",
		// 	args: args{nums: []int{3, 3}, target: 6},
		// 	want: []int{0, 1},
		// },
		// {
		// 	name: "test2",
		// 	args: args{nums: []int{1, 2, 3}, target: 5},
		// 	want: []int{1, 2},
		// },
		// {
		// 	name: "test3",
		// 	args: args{nums: []int{3, 2, 4}, target: 6},
		// 	want: []int{1, 2},
		// },
		{
			name: "test4",
			args: args{nums: []int{3, 2, 3}, target: 6},
			want: []int{0, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoSum(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
