package vp

import (
	"testing"
)

func Test_isValid(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "it_should_be_true_1",
			args: args{s: "()"},
			want: true,
		},
		{
			name: "it_should_be_true_2",
			args: args{s: "()[]{}"},
			want: true,
		},
		{
			name: "it_should_be_true_3",
			args: args{s: "(]"},
			want: false,
		},
		{
			name: "it_should_be_true_4",
			args: args{s: "(])["},
			want: false,
		},
		{
			name: "it_should_be_true_5",
			args: args{s: "([])]"},
			want: false,
		},
		{
			name: "it_should_be_true_6",
			args: args{s: "([)]"},
			want: false,
		},
		{
			name: "it_should_be_true_7",
			args: args{s: "("},
			want: false,
		},
		{
			name: "it_should_be_true_8",
			args: args{s: "(}{)"},
			want: false,
		},
		{
			name: "it_should_be_true_9",
			args: args{s: "(([]){})"},
			want: true,
		},
		{
			name: "it_should_be_true_10",
			args: args{s: "){"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValid(tt.args.s); got != tt.want {
				t.Errorf("isValid() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isValidBetter(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "it_should_be_true_1",
			args: args{s: "()"},
			want: true,
		},
		{
			name: "it_should_be_true_2",
			args: args{s: "()[]{}"},
			want: true,
		},
		{
			name: "it_should_be_true_3",
			args: args{s: "(]"},
			want: false,
		},
		{
			name: "it_should_be_true_4",
			args: args{s: "(])["},
			want: false,
		},
		{
			name: "it_should_be_true_5",
			args: args{s: "([])]"},
			want: false,
		},
		{
			name: "it_should_be_true_6",
			args: args{s: "([)]"},
			want: false,
		},
		{
			name: "it_should_be_true_7",
			args: args{s: "("},
			want: false,
		},
		{
			name: "it_should_be_true_8",
			args: args{s: "(}{)"},
			want: false,
		},
		{
			name: "it_should_be_true_9",
			args: args{s: "(([]){})"},
			want: true,
		},
		{
			name: "it_should_be_true_10",
			args: args{s: "){"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValidBetter(tt.args.s); got != tt.want {
				t.Errorf("isValidBetter() = %v, want %v", got, tt.want)
			}
		})
	}
}
