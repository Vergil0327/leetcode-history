package main

import "testing"

func Test_sequenceReconstruction(t *testing.T) {
	type args struct {
		org  []int
		seqs [][]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				seqs: [][]int{{1, 2}, {1, 3}},
				org:  []int{1, 2, 3},
			},
			want: false,
		},
		{
			name: "test2",
			args: args{
				seqs: [][]int{{1, 2}},
				org:  []int{1, 2, 3},
			},
			want: false,
		},
		{
			name: "test3",
			args: args{
				seqs: [][]int{{1, 2}, {1, 3}, {2, 3}},
				org:  []int{1, 2, 3},
			},
			want: true,
		},
		{
			name: "test4",
			args: args{
				seqs: [][]int{{5, 2, 6, 3}, {4, 1, 5, 2}},
				org:  []int{4, 1, 5, 2, 6, 3},
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sequenceReconstruction(tt.args.org, tt.args.seqs); got != tt.want {
				t.Errorf("sequenceReconstruction() = %v, want %v", got, tt.want)
			}
		})
	}
}
