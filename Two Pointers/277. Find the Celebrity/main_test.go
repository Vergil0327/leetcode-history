package main

import "testing"

func Test_findCelebrity(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{n: 3},
			want: 1,
			// want: -1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findCelebrity(tt.args.n); got != tt.want {
				t.Errorf("findCelebrity() = %v, want %v", got, tt.want)
			}
		})
	}
}
