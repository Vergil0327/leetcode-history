// https://leetcode.com/problems/course-schedule/
package main

import (
	"reflect"
	"testing"
)

func Test_buildGraph(t *testing.T) {
	type args struct {
		prerequisites [][]int
	}
	tests := []struct {
		name      string
		args      args
		wantGraph map[int][]int
	}{
		{
			name: "test1",
			args: args{prerequisites: [][]int{{1, 2}}},
			wantGraph: map[int][]int{
				1: {2},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotGraph := buildGraph(tt.args.prerequisites); !reflect.DeepEqual(gotGraph, tt.wantGraph) {
				t.Errorf("buildGraph() = %v, want %v", gotGraph, tt.wantGraph)
			}
		})
	}
}
