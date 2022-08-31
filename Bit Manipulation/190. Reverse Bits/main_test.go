package main

import (
	"testing"
)

func Test_reverseBits(t *testing.T) {
	type args struct {
		num uint32
	}
	tests := []struct {
		name string
		args args
		want uint32
	}{
		{
			name: "test1",
			args: args{num: 43261596},
			want: 964176192,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverseBits(tt.args.num); got != tt.want {
				t.Errorf("reverseBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_reverseBitsBetter(t *testing.T) {
	type args struct {
		num uint32
	}
	tests := []struct {
		name string
		args args
		want uint32
	}{
		{
			name: "test1",
			args: args{num: 43261596},
			want: 964176192,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverseBitsBetter(tt.args.num); got != tt.want {
				t.Errorf("reverseBitsBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_reverseBitsBest(t *testing.T) {
	type args struct {
		num uint32
	}
	tests := []struct {
		name string
		args args
		want uint32
	}{
		{
			name: "test1",
			args: args{num: 43261596},
			want: 964176192,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverseBitsBest(tt.args.num); got != tt.want {
				t.Errorf("reverseBitsBest() = %v, want %v", got, tt.want)
			}
		})
	}
}
