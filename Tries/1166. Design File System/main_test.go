package main

import "testing"

func TestFileSystem_CreatePath(t *testing.T) {
	type fields struct {
		root *TrieNode
	}
	type args struct {
		path  string
		value int
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   bool
	}{
		{
			name:   "test1",
			fields: fields{root: &TrieNode{next: make(map[string]*TrieNode)}},
			args: args{
				path:  "/leet",
				value: 1,
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			fs := &FileSystem{
				root: tt.fields.root,
			}

			if got := fs.CreatePath("/leet", 1); got != tt.want {
				t.Errorf("1. FileSystem.CreatePath() = %v, want %v", got, tt.want)
			}
			if got := fs.CreatePath("/leet/code", 2); got != tt.want {
				t.Errorf("2. FileSystem.CreatePath() = %v, want %v", got, tt.want)
			}
			if got := fs.get("/leet/code"); got != 2 {
				t.Errorf("3. FileSystem.get() = %v, want %v", got, 2)
			}
			if got := fs.CreatePath("/c/d", 2); got != false {
				t.Errorf("4. FileSystem.CreatePath() = %v, want %v", got, false)
			}
			if got := fs.get("/d"); got != -1 {
				t.Errorf("5. FileSystem.get() = %v, want %v", got, -1)
			}
		})
	}

}
