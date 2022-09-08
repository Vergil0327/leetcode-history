// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/moving-average-from-data-stream/
package main

import (
	"testing"
)

func TestMovingAverage_Next(t *testing.T) {
	type fields struct {
		sum  int
		q    []int
		size int
	}
	type args struct {
		num int
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   float64
	}{
		{
			name:   "test1",
			fields: fields{sum: 0, q: make([]int, 0), size: 3},
			args:   args{num: 1},
			want:   1,
		},
		{
			name:   "test2",
			fields: fields{sum: 1, q: []int{1}, size: 3},
			args:   args{num: 10},
			want:   5.5,
		},
		{
			name:   "test3",
			fields: fields{sum: 11, q: []int{1, 10}, size: 3},
			args:   args{num: 3},
			want:   float64((1 + 10 + 3)) / 3,
		},
		{
			name:   "test4",
			fields: fields{sum: 14, q: []int{1, 10, 3}, size: 3},
			args:   args{num: 5},
			want:   float64((10 + 3 + 5)) / 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			this := MovingAverage{
				sum:  tt.fields.sum,
				q:    tt.fields.q,
				size: tt.fields.size,
			}
			if got := this.Next(tt.args.num); got != tt.want {
				t.Errorf("MovingAverage.Next() = %v, want %v", got, tt.want)
			}
		})
	}
}
