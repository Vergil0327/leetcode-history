package main

import (
	"reflect"
	"sort"
	"testing"
)

func Test_groupAnagrams(t *testing.T) {
	type args struct {
		strs []string
	}
	tests := []struct {
		name string
		args args
		want [][]string
	}{
		{
			name: "test1",
			args: args{strs: []string{"eat", "tea", "tan", "ate", "nat", "bat"}},
			want: [][]string{{"bat"}, {"tan", "nat"}, {"eat", "tea", "ate"}},
		},
		{
			name: "test2",
			args: args{strs: []string{"dddddg", "gggggd"}},
			want: [][]string{{"dddddg"}, {"gggggd"}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := groupAnagrams(tt.args.strs)
			sort.Slice(got, func(i, j int) bool {
				return len(got[i]) < len(got[j])
			})
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("groupAnagrams() = %v, want %v", got, tt.want)
			}
		})
	}
}
