package lcp

import "testing"

func Test_longestCommonPrefix(t *testing.T) {
	type args struct {
		strs []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "test-1",
			args: args{strs: []string{"flower", "flow", "flight"}},
			want: "fl",
		},
		{
			name: "test-2",
			args: args{strs: []string{"dog", "racecar", "car"}},
			want: "",
		},
		{
			name: "test-3",
			args: args{strs: []string{"", "racecar", "car"}},
			want: "",
		},
		{
			name: "test-4",
			args: args{strs: []string{"a"}},
			want: "a",
		},
		{
			name: "test-5",
			args: args{strs: []string{"cir", "car"}},
			want: "c",
		},
		{
			name: "test-6",
			args: args{strs: []string{"reflower", "flow", "flight"}},
			want: "",
		},
		{
			name: "test-7",
			args: args{strs: []string{"abab", "aba", ""}},
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonPrefix(tt.args.strs); got != tt.want {
				t.Errorf("longestCommonPrefix() = %v, want %v", got, tt.want)
			}
		})
	}
}
