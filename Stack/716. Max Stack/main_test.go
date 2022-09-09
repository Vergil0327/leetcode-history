// SUBSCRIBE TO UNLOCK
package main

import (
	"testing"
)

func TestMaxStack(t *testing.T) {
	type fields struct {
		values   []int
		maximums []int
	}
	tests := []struct {
		name   string
		fields fields
		want   []int
	}{
		{
			name:   "test1",
			fields: fields{values: make([]int, 0), maximums: make([]int, 0)},
			want:   []int{5, 5, 1, 5, 1, 5, 10, 10},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			stk := &MaxStack{
				values:   tt.fields.values,
				maximums: tt.fields.maximums,
			}
			stk.Push(5)
			stk.Push(1)
			stk.Push(5)

			if got := stk.Top(); got != tt.want[0] {
				t.Errorf("MaxStack.Top() = %v, want %v", got, tt.want)
			}
			if got := stk.PopMax(); got != tt.want[1] {
				t.Errorf("MaxStack.PopMax() = %v, want %v", got, tt.want)
			}
			if got := stk.Top(); got != tt.want[2] {
				t.Errorf("MaxStack.Top() = %v, want %v", got, tt.want)
			}
			if got := stk.PeekMax(); got != tt.want[3] {
				t.Errorf("MaxStack.PeekMax() = %v, want %v", got, tt.want)
			}
			if got := stk.Pop(); got != tt.want[4] {
				t.Errorf("MaxStack.Pop() = %v, want %v", got, tt.want)
			}
			if got := stk.Top(); got != tt.want[5] {
				t.Errorf("MaxStack.Top() = %v, want %v", got, tt.want)
			}

			stk.Push(10)
			if got := stk.Top(); got != tt.want[6] {
				t.Errorf("MaxStack.Top() = %v, want %v", got, tt.want)
			}
			if got := stk.PeekMax(); got != tt.want[7] {
				t.Errorf("MaxStack.PeekMax() = %v, want %v", got, tt.want)
			}
		})
	}
}
