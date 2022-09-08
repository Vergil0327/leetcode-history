// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/zigzag-iterator/

package main

import (
	"reflect"
	"testing"
)

// func TestZigzagIterator(t *testing.T) {
// 	type args struct {
// 		list1 []int
// 		list2 []int
// 	}
// 	tests := []struct {
// 		name string
// 		args args
// 		want []int
// 	}{
// 		{
// 			name: "test1",
// 			args: args{
// 				list1: []int{1, 2},
// 				list2: []int{3, 4, 5, 6},
// 			},
// 			want: []int{1, 3, 2, 4, 5, 6},
// 		},
// 		{
// 			name: "test2",
// 			args: args{
// 				list1: []int{1, 1, 1, 1},
// 				list2: []int{3, 4, 5, 6},
// 			},
// 			want: []int{1, 3, 1, 4, 1, 5, 1, 6},
// 		},
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			if got := ZigzagIterator(tt.args.list1, tt.args.list2); !reflect.DeepEqual(got, tt.want) {
// 				t.Errorf("ZigzagIterator() = %v, want %v", got, tt.want)
// 			}
// 		})
// 	}
// }

func TestZigzagIterator_HasNext(t *testing.T) {
	type fields struct {
		q *[][]int
	}
	tests := []struct {
		name   string
		fields fields
		want   bool
	}{
		{
			name:   "test1",
			fields: fields{q: &[][]int{{1}}},
			want:   true,
		},
		{
			name:   "test2",
			fields: fields{q: &[][]int{{1}, {2}}},
			want:   true,
		},
		{
			name:   "test1",
			fields: fields{q: &[][]int{}},
			want:   false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			iter := ZigzagIterator{
				q: tt.fields.q,
			}
			if got := iter.HasNext(); got != tt.want {
				t.Errorf("ZigzagIterator.HasNext() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestZigzagIterator_Next(t *testing.T) {
	type fields struct {
		q *[][]int
	}

	tests := []struct {
		name   string
		fields fields
		want   []int
	}{
		{
			name:   "test1",
			fields: fields{q: &[][]int{{1, 2, 3, 4}, {5, 6, 7, 8}}},
			want:   []int{1, 5, 2, 6, 3, 7, 4, 8},
		},
		{
			name:   "test2",
			fields: fields{q: &[][]int{{1, 1, 1, 1}, {5, 6, 7, 8}}},
			want:   []int{1, 5, 1, 6, 1, 7, 1, 8},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			iter := ZigzagIterator{
				q: tt.fields.q,
			}
			got := []int{}
			for iter.HasNext() {
				got = append(got, iter.Next())
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ZigzagIterator.HasNext() = %v, want %v", got, tt.want)
			}
		})
	}

}
