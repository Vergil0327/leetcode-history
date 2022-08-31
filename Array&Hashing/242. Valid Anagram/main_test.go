package main

import "testing"

func Test_isAnagramMap(t *testing.T) {
	type args struct {
		s string
		t string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "anagram", t: "nagaram"},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isAnagramMap(tt.args.s, tt.args.t); got != tt.want {
				t.Errorf("isAnagramMap() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sortString(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "test1",
			args: args{str: "anagram"},
			want: "aaagmnr",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sortString(tt.args.str); got != tt.want {
				t.Errorf("sortString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isAnagramSort(t *testing.T) {
	type args struct {
		s string
		t string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "anagram", t: "nagaram"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isAnagramSort(tt.args.s, tt.args.t); got != tt.want {
				t.Errorf("isAnagramSort() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isAnagramBest(t *testing.T) {
	type args struct {
		s string
		t string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{s: "anagram", t: "nagaram"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isAnagramBest(tt.args.s, tt.args.t); got != tt.want {
				t.Errorf("isAnagramBest() = %v, want %v", got, tt.want)
			}
		})
	}
}
