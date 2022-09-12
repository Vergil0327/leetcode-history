// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/design-tic-tac-toe/
package main

import (
	"testing"
)

func TestTicTacToe_Move(t *testing.T) {
	type args struct {
		row    int
		col    int
		player int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "player1_move_1",
			args: args{0, 0, 1},
			want: false,
		},
		{
			name: "player2_move_1",
			args: args{0, 2, 2},
			want: false,
		},
		{
			name: "player1_move_2",
			args: args{1, 0, 1},
			want: false,
		},
		{
			name: "player2_move_2",
			args: args{0, 1, 2},
			want: false,
		},
		{
			name: "player1_move_3",
			args: args{2, 0, 1},
			want: true,
		},
	}

	this := NewTicTacToe(3)
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := this.Move(tt.args.row, tt.args.col, tt.args.player); got != tt.want {
				t.Errorf("TicTacToe.Move() = %v, want %v", got, tt.want)
			}
		})
	}
}
