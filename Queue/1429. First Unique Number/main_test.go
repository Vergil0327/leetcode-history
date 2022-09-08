// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/first-unique-number/
package main

import (
	"fmt"
	"testing"
)

func TestFirstUnique_ShowFirstUnique(t *testing.T) {
	type fields struct {
		exist map[int]int
		queue []int
	}
	tests := []struct {
		name   string
		fields fields
		want   []int
	}{
		{
			name:   "test1",
			fields: fields{exist: make(map[int]int), queue: make([]int, 0)},
			want:   []int{2, 3, -1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			uniq := New([]int{2, 3, 5})
			fmt.Println(uniq)
			if got := uniq.ShowFirstUnique(); got != tt.want[0] {
				t.Errorf("FirstUnique.ShowFirstUnique() = %v, want %v", got, tt.want[0])
			}
			uniq.Add(5)
			fmt.Println(uniq)
			if got := uniq.ShowFirstUnique(); got != tt.want[0] {
				t.Errorf("FirstUnique.ShowFirstUnique() = %v, want %v", got, tt.want[0])
			}
			uniq.Add(2)
			fmt.Println(uniq)
			if got := uniq.ShowFirstUnique(); got != tt.want[1] {
				t.Errorf("FirstUnique.ShowFirstUnique() = %v, want %v", got, tt.want[1])
			}
			// uniq.Add(3)
			// if got := uniq.ShowFirstUnique(); got != tt.want[2] {
			// 	t.Errorf("FirstUnique.ShowFirstUnique() = %v, want %v", got, tt.want[2])
			// }

		})
	}
}
