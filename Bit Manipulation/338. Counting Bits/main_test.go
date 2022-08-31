package main

import (
	"reflect"
	"testing"
)

func Test_countBits(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name    string
		args    args
		wantAns []int
	}{
		{
			name:    "test1",
			args:    args{n: 2},
			wantAns: []int{0, 1, 1},
		},
		{
			name:    "test2",
			args:    args{n: 5},
			wantAns: []int{0, 1, 1, 2, 1, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotAns := countBits(tt.args.n); !reflect.DeepEqual(gotAns, tt.wantAns) {
				t.Errorf("countBits() = %v, want %v", gotAns, tt.wantAns)
			}
		})
	}
}

func Test_countOne(t *testing.T) {
	type args struct {
		num int
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
			if got := countOne(tt.args.num); got != tt.want {
				t.Errorf("countOne() = %v, want %v", got, tt.want)
			}
		})
	}
}
