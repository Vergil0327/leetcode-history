package main

import "testing"

func Test_wordPatternMatch(t *testing.T) {
	type args struct {
		pattern string
		str     string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test1",
			args: args{pattern: "abab", str: "redblueredblue"},
			want: true,
		},
		{
			name: "test2",
			args: args{pattern: "aaaa", str: "asdasdasdasd"},
			want: true,
		},
		{
			name: "test3",
			args: args{pattern: "aabb", str: "xyzabcxzyabc"},
			want: false,
		},
		{
			name: "test4",
			args: args{pattern: "aabaacb", str: "asdasdxyzasdasdzzzxyz"},
			want: true,
		},
		{
			name: "test5",
			args: args{pattern: "zaabacacb", str: "zxyzasdasdxyzasdzzzasdzzzxyz"},
			want: true,
		},
		{
			name: "test6",
			args: args{pattern: "aaaa", str: "asdasdasd"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := wordPatternMatch(tt.args.pattern, tt.args.str); got != tt.want {
				t.Errorf("wordPatternMatch() = %v, want %v", got, tt.want)
			}
		})
	}
}
