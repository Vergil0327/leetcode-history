package main

import "testing"

func Test_areSentencesSimilarTwo(t *testing.T) {
	type args struct {
		words1 []string
		words2 []string
		pairs  [][2]string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{
				words1: []string{"great", "acting", "skills"},
				words2: []string{"fine", "drama", "talent"},
				pairs:  [][2]string{{"great", "good"}, {"fine", "good"}, {"acting", "drama"}, {"skills", "talent"}},
			},
			want: true,
		},
		{
			name: "test2",
			args: args{
				words1: []string{"great"},
				words2: []string{"great"},
				pairs:  [][2]string{},
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := areSentencesSimilarTwo(tt.args.words1, tt.args.words2, tt.args.pairs); got != tt.want {
				t.Errorf("areSentencesSimilarTwo() = %v, want %v", got, tt.want)
			}
		})
	}
}
