package leetcode

import (
	"reflect"
	"testing"
)

func Test_insertionSort(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "test_insertion_sort",
			args: args{nums: []int{4, 3, 2, 1}},
			want: []int{1, 2, 3, 4},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := insertionSort(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("insertionSort() = %v, want %v", got, tt.want)
			}
		})
	}
}
