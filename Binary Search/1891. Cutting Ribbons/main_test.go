package main

import "testing"

func Test_maxLength(t *testing.T) {
	type args struct {
		ribbons []int
		k       int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{
				ribbons: []int{9, 7, 5},
				k:       3,
			},
			want: 5,
		},
		{
			name: "test2",
			args: args{
				ribbons: []int{7, 5, 9},
				k:       4,
			},
			want: 5,
		},
		{
			name: "test3",
			args: args{
				ribbons: []int{5, 7, 9},
				k:       22,
			},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxLength(tt.args.ribbons, tt.args.k); got != tt.want {
				t.Errorf("maxLength() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_check(t *testing.T) {
	type args struct {
		ribbons []int
		length  int
		k       int
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
			if got := check(tt.args.ribbons, tt.args.length, tt.args.k); got != tt.want {
				t.Errorf("check() = %v, want %v", got, tt.want)
			}
		})
	}
}
