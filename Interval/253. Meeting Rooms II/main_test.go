// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/meeting-rooms-ii/
package main

import (
	"testing"
)

func TestMeetingRoom2(t *testing.T) {
	type args struct {
		intervals [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{intervals: [][]int{{0, 30}, {5, 10}, {15, 20}}},
			want: 2,
		},
		{
			name: "case2",
			args: args{intervals: [][]int{{7, 10}, {2, 4}}},
			want: 1,
		},
		{
			name: "case3",
			args: args{intervals: [][]int{{7, 10}, {2, 4}, {5, 30}, {17, 25}, {30, 40}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MeetingRoom2(tt.args.intervals); got != tt.want {
				t.Errorf("MeetingRoom2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMeetingRoom2Solution(t *testing.T) {
	type args struct {
		intervals [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{intervals: [][]int{{0, 30}, {5, 10}, {15, 20}}},
			want: 2,
		},
		{
			name: "case2",
			args: args{intervals: [][]int{{7, 10}, {2, 4}}},
			want: 1,
		},
		{
			name: "case3",
			args: args{intervals: [][]int{{7, 10}, {2, 4}, {5, 30}, {17, 25}, {30, 40}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MeetingRoom2Solution(tt.args.intervals); got != tt.want {
				t.Errorf("MeetingRoom2Solution() = %v, want %v", got, tt.want)
			}
		})
	}
}
